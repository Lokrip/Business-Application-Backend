from django.db.models.signals import post_delete

from django.db import models

from django.core.validators import (

    MinValueValidator,

    MaxValueValidator

)



from clients.models import Client



from .tasks import (

    set_price, 

    set_comment

)



from .receivers import delete_cache_total_sum



class Service(models.Model): 

    name = models.CharField(max_length=50)

    full_price = models.PositiveIntegerField()

    

    updated_at = models.DateTimeField(auto_now=True)

    created_at = models.DateTimeField(auto_now_add=True)

    

    

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.__full_price = self.full_price

    

    def save(self, *args, **kwargs):

        if self.full_price != self.__full_price:

            for subscription in self.subsriptions.all():

                set_price.delay(subscription.id)

                set_comment.delay(subscription.id)

        return super().save(*args, **kwargs)

    

class Plan(models.Model): 

    class PlanTypes(models.TextChoices):

        FULL = 'full', 'Full' 

        STUDENT = 'student', 'Student'

        DISCOUNT = 'discount', 'Discount'



    plan_type = models.CharField(

        choices=PlanTypes.choices,

        max_length=10,

    )

    

    discount_percent = models.PositiveIntegerField(default=0, validators=[

        MinValueValidator(0),

        MaxValueValidator(100),

    ])

    

    updated_at = models.DateTimeField(auto_now=True)

    created_at = models.DateTimeField(auto_now_add=True)

    

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.__discount_percent = self.discount_percent

    

    def save(self, *args, **kwargs):

        if self.discount_percent != self.__discount_percent:

            for subscription in self.subsriptions.all():

                set_price.delay(subscription.id)

                set_comment.delay(subscription.id)

        return super().save(*args, **kwargs)





class Subsription(models.Model): 

    client = models.ForeignKey(

        Client, related_name='subsriptions', on_delete=models.PROTECT)

    service = models.ForeignKey(

        Service, related_name='subsriptions',  on_delete=models.PROTECT)

    plan = models.ForeignKey(

        Plan, related_name='subsriptions',  on_delete=models.PROTECT)

    price = models.PositiveIntegerField(default=0)

    comment = models.CharField(max_length=50, default="", db_index=True)

    

    field_a = models.CharField(max_length=50, default="")

    field_b = models.CharField(max_length=50, default="")

    

    updated_at = models.DateTimeField(auto_now=True)

    created_at = models.DateTimeField(auto_now_add=True)

    

    class Meta:

        indexes = [

            models.Index(fields=[

                "field_a", "field_b"

            ])

        ]

    

    def save(self, *args, **kwargs):

        

        creating = not bool(self.id) 

        result = super().save(*args, **kwargs)

        if creating:

            set_price.delay(self.id)

            
        return result


post_delete.connect(delete_cache_total_sum, sender=Subsription)

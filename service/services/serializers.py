from rest_framework import serializers

from .models import Subsription, Plan



class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'


class SubsriptionSerializer(serializers.ModelSerializer):
    plan = PlanSerializer(read_only=True) 
    client_name = serializers.CharField(source="client.company_name") 
    email = serializers.CharField(source="client.user.email") 
    price = serializers.SerializerMethodField()

    
    def get_price(self, instance):
        return instance.price

    

    class Meta:
        model = Subsription
        fields = (
            'id', 'plan_id', 'client_name', 'email',
            'plan', 'price', 'created_at', 'updated_at'
        ) 

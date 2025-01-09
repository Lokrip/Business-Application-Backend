

from django.db import migrations, models





class Migration(migrations.Migration):



    dependencies = [

        ('services', '0001_initial'),

    ]



    operations = [

        migrations.AddField(

            model_name='subsription',

            name='price',

            field=models.PositiveIntegerField(default=0),

        ),

    ]


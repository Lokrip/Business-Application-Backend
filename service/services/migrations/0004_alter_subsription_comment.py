

from django.db import migrations, models





class Migration(migrations.Migration):



    dependencies = [

        ('services', '0003_subsription_comment'),

    ]



    operations = [

        migrations.AlterField(

            model_name='subsription',

            name='comment',

            field=models.CharField(default='', max_length=50),

        ),

    ]


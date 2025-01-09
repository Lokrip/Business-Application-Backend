

from django.db import migrations, models





class Migration(migrations.Migration):



    dependencies = [

        ('services', '0002_subsription_price'),

    ]



    operations = [

        migrations.AddField(

            model_name='subsription',

            name='comment',

            field=models.CharField(default='Default Text', max_length=50),

            preserve_default=False,

        ),

    ]


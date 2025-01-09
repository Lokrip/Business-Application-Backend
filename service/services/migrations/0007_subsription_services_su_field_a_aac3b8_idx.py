

from django.db import migrations, models





class Migration(migrations.Migration):



    dependencies = [

        ('services', '0006_auto_20241229_1453'),

    ]



    operations = [

        migrations.AddIndex(

            model_name='subsription',

            index=models.Index(fields=['field_a', 'field_b'], name='services_su_field_a_aac3b8_idx'),

        ),

    ]


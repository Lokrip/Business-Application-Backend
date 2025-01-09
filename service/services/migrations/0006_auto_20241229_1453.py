

from django.db import migrations, models





class Migration(migrations.Migration):



    dependencies = [

        ('services', '0005_alter_subsription_comment'),

    ]



    operations = [

        migrations.AddField(

            model_name='subsription',

            name='field_a',

            field=models.CharField(default='', max_length=50),

        ),

        migrations.AddField(

            model_name='subsription',

            name='field_b',

            field=models.CharField(default='', max_length=50),

        ),

    ]


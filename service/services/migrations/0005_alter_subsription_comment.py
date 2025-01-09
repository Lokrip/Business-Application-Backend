

from django.db import migrations, models





class Migration(migrations.Migration):



    dependencies = [

        ('services', '0004_alter_subsription_comment'),

    ]



    operations = [

        migrations.AlterField(

            model_name='subsription',

            name='comment',

            field=models.CharField(db_index=True, default='', max_length=50),

        ),

    ]


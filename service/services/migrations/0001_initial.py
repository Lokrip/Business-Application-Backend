

import django.core.validators

from django.db import migrations, models

import django.db.models.deletion





class Migration(migrations.Migration):



    initial = True



    dependencies = [

        ('clients', '0001_initial'),

    ]



    operations = [

        migrations.CreateModel(

            name='Plan',

            fields=[

                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),

                ('plan_type', models.CharField(choices=[('full', 'Full'), ('student', 'Student'), ('discount', 'Discount')], max_length=10)),

                ('discount_percent', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),

                ('updated_at', models.DateTimeField(auto_now=True)),

                ('created_at', models.DateTimeField(auto_now_add=True)),

            ],

        ),

        migrations.CreateModel(

            name='Service',

            fields=[

                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),

                ('name', models.CharField(max_length=50)),

                ('full_price', models.PositiveIntegerField()),

                ('updated_at', models.DateTimeField(auto_now=True)),

                ('created_at', models.DateTimeField(auto_now_add=True)),

            ],

        ),

        migrations.CreateModel(

            name='Subsription',

            fields=[

                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),

                ('updated_at', models.DateTimeField(auto_now=True)),

                ('created_at', models.DateTimeField(auto_now_add=True)),

                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='subsriptions', to='clients.client')),

                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='subsriptions', to='services.plan')),

                ('service', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='subsriptions', to='services.service')),

            ],

        ),

    ]


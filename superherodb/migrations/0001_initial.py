# Generated by Django 4.1 on 2022-08-19 19:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Superhero',
            fields=[
                ('name', models.CharField(max_length=255, primary_key=True, serialize=False, validators=[django.core.validators.MinLengthValidator(10, 'The name field must contain at least 10 characters')])),
                ('alias', models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(10, 'The alias field must contain at least 10 characters')])),
                ('Species', models.CharField(choices=[('A', 'Angels'), ('H', 'Humans'), ('D', 'Demons'), ('G', 'Gods')], default='D', max_length=1)),
                ('Date_of_Birth', models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(10, 'The Date_of_Birth field must contain at least 10 characters')])),
                ('Age', models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(10, 'The Age field must contain at least 10 characters')])),
                ('Gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1)),
                ('intelligence', models.IntegerField(max_length=2, validators=[django.core.validators.MinLengthValidator(1, 'The intelligence field must contain at least 1 characters')])),
                ('strength', models.IntegerField(max_length=2, validators=[django.core.validators.MinLengthValidator(1, 'The strength field must contain at least 1 characters')])),
                ('speed', models.IntegerField(max_length=2, validators=[django.core.validators.MinLengthValidator(1, 'The speed field must contain at least 1 characters')])),
                ('durability', models.IntegerField(max_length=2, validators=[django.core.validators.MinLengthValidator(1, 'The durability field must contain at least 1 characters')])),
                ('power', models.IntegerField(max_length=2, validators=[django.core.validators.MinLengthValidator(1, 'The power field must contain at least 1 characters')])),
                ('combat', models.IntegerField(max_length=2, validators=[django.core.validators.MinLengthValidator(1, 'The combat field must contain at least 1 characters')])),
                ('tier', models.IntegerField(max_length=2, validators=[django.core.validators.MinLengthValidator(1, 'The tier field must contain at least 1 characters')])),
            ],
        ),
    ]
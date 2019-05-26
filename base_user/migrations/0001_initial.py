# Generated by Django 2.0.1 on 2019-05-23 20:00

import base_user.tools.common
import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(help_text='Tələb olunur. 75 simvol və ya az. Hərflər, Rəqəmlər və @/./+/-/_ simvollar.', max_length=100, unique=True, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Düzgün istifadəçi adı daxil edin.', 'yanlışdır')], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=255, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=255, verbose_name='last name')),
                ('email', models.EmailField(max_length=255, verbose_name='email address')),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to=base_user.tools.common.get_user_profile_photo_file_name)),
                ('gender', models.IntegerField(blank=True, choices=[(1, 'Man'), (2, 'Woman')], null=True, verbose_name='cinsi')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name_plural': 'İstifadəçilər',
                'verbose_name': 'İstifadəçi',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]

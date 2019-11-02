# Generated by Django 2.0.1 on 2019-05-25 22:01

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Adı')),
                ('is_published', models.BooleanField(default=True, verbose_name='Is Published')),
                ('created_at', models.DateTimeField(default=datetime.datetime(2019, 5, 25, 22, 1, 12, 676251, tzinfo=utc), editable=False)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Kafedralar',
                'verbose_name': 'Kafedra',
            },
        ),
        migrations.CreateModel(
            name='Diary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point', models.PositiveIntegerField(verbose_name='Bal')),
                ('day', models.DateField(default=datetime.datetime(2019, 5, 25, 22, 1, 12, 680226, tzinfo=utc), verbose_name='Gün')),
                ('is_published', models.BooleanField(default=True, verbose_name='Is Published')),
                ('created_at', models.DateTimeField(default=datetime.datetime(2019, 5, 25, 22, 1, 12, 680323, tzinfo=utc), editable=False)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Gündəlik qiymətlər',
                'verbose_name': 'Gündəlik qiymət',
            },
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Adı')),
                ('is_published', models.BooleanField(default=True, verbose_name='Is Published')),
                ('created_at', models.DateTimeField(default=datetime.datetime(2019, 5, 25, 22, 1, 12, 670823, tzinfo=utc), editable=False)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Fakültələr',
                'verbose_name': 'Fakültə',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='Adı')),
                ('is_published', models.BooleanField(default=True, verbose_name='Is Published')),
                ('created_at', models.DateTimeField(default=datetime.datetime(2019, 5, 25, 22, 1, 12, 673220, tzinfo=utc), editable=False)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Qruplar',
                'verbose_name': 'Qrup',
            },
        ),
        migrations.CreateModel(
            name='GroupSubject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_published', models.BooleanField(default=True, verbose_name='Is Published')),
                ('created_at', models.DateTimeField(default=datetime.datetime(2019, 5, 25, 22, 1, 12, 678031, tzinfo=utc), editable=False)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group_subjects', to='sms_project.Group')),
            ],
            options={
                'verbose_name_plural': 'Qrup fənnləri',
                'verbose_name': 'Qrup fənni',
            },
        ),
        migrations.CreateModel(
            name='NotParticipating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField(default=datetime.datetime(2019, 5, 25, 22, 1, 12, 681213, tzinfo=utc), verbose_name='Gün')),
            ],
            options={
                'verbose_name_plural': 'Qayıblar',
                'verbose_name': 'Qayıblar',
            },
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='Adı')),
                ('is_published', models.BooleanField(default=True, verbose_name='Is Published')),
                ('created_at', models.DateTimeField(default=datetime.datetime(2019, 5, 25, 22, 1, 12, 672430, tzinfo=utc), editable=False)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Semestrlər',
                'verbose_name': 'Semestr',
            },
        ),
        migrations.CreateModel(
            name='Specialty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Adı')),
                ('is_published', models.BooleanField(default=True, verbose_name='Is Published')),
                ('created_at', models.DateTimeField(default=datetime.datetime(2019, 5, 25, 22, 1, 12, 671620, tzinfo=utc), editable=False)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specialties', to='sms_project.Faculty')),
            ],
            options={
                'verbose_name_plural': 'İxtisaslar',
                'verbose_name': 'İxtisas',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Telefon nömrəsi')),
                ('father_name', models.CharField(max_length=30, verbose_name='Ata adı')),
                ('birth_date', models.DateField(verbose_name='Doğum tarixi')),
                ('admission_date', models.DateField(verbose_name='Qəbul ili')),
                ('admission_point', models.PositiveIntegerField(verbose_name='Qəbul Balı')),
                ('is_published', models.BooleanField(default=True, verbose_name='Is Published')),
                ('created_at', models.DateTimeField(default=datetime.datetime(2019, 5, 25, 22, 1, 12, 674530, tzinfo=utc), editable=False)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='sms_project.Group')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='student', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Tələbələr',
                'verbose_name': 'Tələbə',
            },
        ),
        migrations.CreateModel(
            name='StudentWork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_published', models.BooleanField(default=True, verbose_name='Is Published')),
                ('created_at', models.DateTimeField(default=datetime.datetime(2019, 5, 25, 22, 1, 12, 683064, tzinfo=utc), editable=False)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_works', to='sms_project.Student')),
            ],
            options={
                'verbose_name_plural': 'Tələbənin sərbəst işləri',
                'verbose_name': 'Tələbənin sərbəst işi',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Adı')),
                ('is_published', models.BooleanField(default=True, verbose_name='Is Published')),
                ('created_at', models.DateTimeField(default=datetime.datetime(2019, 5, 25, 22, 1, 12, 675543, tzinfo=utc), editable=False)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Fənnlər',
                'verbose_name': 'Fənn',
            },
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weekday', models.PositiveIntegerField(choices=[(1, 'I'), (2, 'II'), (3, 'III'), (4, 'IV'), (5, 'V')], verbose_name='Həftənin günü')),
                ('lesson_time', models.PositiveIntegerField(choices=[(1, '08:30-10:05'), (2, '10:15-11:50'), (3, '12:00-13:35'), (4, '13:50-15:25'), (5, '15:35-17:10'), (6, '17:20-18:55')], verbose_name='Dərs vaxtı')),
                ('week_type', models.PositiveIntegerField(blank=True, choices=[(1, 'Üst həftə'), (2, 'Alt həftə')], null=True, verbose_name='Həftə')),
                ('subject_type', models.PositiveIntegerField(choices=[(1, 'Mühazirə'), (2, 'Seminar'), (2, 'Laboratoriya')], default=1, verbose_name='Dərs tipi')),
                ('is_published', models.BooleanField(default=True, verbose_name='Is Published')),
                ('created_at', models.DateTimeField(default=datetime.datetime(2019, 5, 25, 22, 1, 12, 679322, tzinfo=utc), editable=False)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('group_subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tables', to='sms_project.GroupSubject')),
            ],
            options={
                'verbose_name_plural': 'Cədvəl',
                'verbose_name': 'Cədvəl',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('father_name', models.CharField(max_length=30, verbose_name='Ata adı')),
                ('is_published', models.BooleanField(default=True, verbose_name='Is Published')),
                ('created_at', models.DateTimeField(default=datetime.datetime(2019, 5, 25, 22, 1, 12, 677042, tzinfo=utc), editable=False)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('department', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='teachers', to='sms_project.Department')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='teacher', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Müəllimlər',
                'verbose_name': 'Müəllim',
            },
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='İşin adı')),
                ('lastday', models.DateField(default=datetime.datetime(2019, 5, 25, 22, 1, 12, 681952, tzinfo=utc), verbose_name='Son Gün')),
                ('is_published', models.BooleanField(default=True, verbose_name='Is Published')),
                ('created_at', models.DateTimeField(default=datetime.datetime(2019, 5, 25, 22, 1, 12, 682050, tzinfo=utc), editable=False)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('group_subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='works', to='sms_project.GroupSubject')),
            ],
            options={
                'verbose_name_plural': 'Sərbəst işlər',
                'verbose_name': 'Sərbəst iş',
            },
        ),
        migrations.AddField(
            model_name='studentwork',
            name='work',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_works', to='sms_project.Work'),
        ),
        migrations.AddField(
            model_name='notparticipating',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='not_participatings', to='sms_project.Student'),
        ),
        migrations.AddField(
            model_name='notparticipating',
            name='table',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='not_participatings', to='sms_project.Table'),
        ),
        migrations.AddField(
            model_name='groupsubject',
            name='semester',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group_subjects', to='sms_project.Semester'),
        ),
        migrations.AddField(
            model_name='groupsubject',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group_subjects', to='sms_project.Subject'),
        ),
        migrations.AddField(
            model_name='groupsubject',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group_subjects', to='sms_project.Teacher'),
        ),
        migrations.AddField(
            model_name='group',
            name='semester',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='sms_project.Semester'),
        ),
        migrations.AddField(
            model_name='group',
            name='specialty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Group', to='sms_project.Specialty'),
        ),
        migrations.AddField(
            model_name='diary',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dairies', to='sms_project.Student'),
        ),
        migrations.AddField(
            model_name='diary',
            name='table',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dairies', to='sms_project.Table'),
        ),
    ]
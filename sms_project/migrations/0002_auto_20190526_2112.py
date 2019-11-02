# Generated by Django 2.0.1 on 2019-05-26 17:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sms_project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 26, 17, 12, 10, 132744, tzinfo=utc), editable=False),
        ),
        migrations.AlterField(
            model_name='diary',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 26, 17, 12, 10, 136794, tzinfo=utc), editable=False),
        ),
        migrations.AlterField(
            model_name='diary',
            name='day',
            field=models.DateField(default=datetime.datetime(2019, 5, 26, 17, 12, 10, 136694, tzinfo=utc), verbose_name='Gün'),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 26, 17, 12, 10, 127358, tzinfo=utc), editable=False),
        ),
        migrations.AlterField(
            model_name='group',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 26, 17, 12, 10, 129825, tzinfo=utc), editable=False),
        ),
        migrations.AlterField(
            model_name='groupsubject',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 26, 17, 12, 10, 134521, tzinfo=utc), editable=False),
        ),
        migrations.AlterField(
            model_name='notparticipating',
            name='day',
            field=models.DateField(default=datetime.datetime(2019, 5, 26, 17, 12, 10, 137840, tzinfo=utc), verbose_name='Gün'),
        ),
        migrations.AlterField(
            model_name='semester',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 26, 17, 12, 10, 129047, tzinfo=utc), editable=False),
        ),
        migrations.AlterField(
            model_name='semester',
            name='name',
            field=models.PositiveIntegerField(max_length=10, verbose_name='Adı'),
        ),
        migrations.AlterField(
            model_name='specialty',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 26, 17, 12, 10, 128251, tzinfo=utc), editable=False),
        ),
        migrations.AlterField(
            model_name='student',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 26, 17, 12, 10, 131053, tzinfo=utc), editable=False),
        ),
        migrations.AlterField(
            model_name='studentwork',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 26, 17, 12, 10, 139772, tzinfo=utc), editable=False),
        ),
        migrations.AlterField(
            model_name='subject',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 26, 17, 12, 10, 132063, tzinfo=utc), editable=False),
        ),
        migrations.AlterField(
            model_name='table',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 26, 17, 12, 10, 135807, tzinfo=utc), editable=False),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 26, 17, 12, 10, 133522, tzinfo=utc), editable=False),
        ),
        migrations.AlterField(
            model_name='work',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 26, 17, 12, 10, 138722, tzinfo=utc), editable=False),
        ),
        migrations.AlterField(
            model_name='work',
            name='lastday',
            field=models.DateField(default=datetime.datetime(2019, 5, 26, 17, 12, 10, 138620, tzinfo=utc), verbose_name='Son Gün'),
        ),
    ]
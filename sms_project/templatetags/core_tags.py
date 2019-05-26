import datetime

from django import template
from django.utils import timezone

from sms_project.models import NotParticipating, Diary

register = template.Library()


@register.simple_tag()
def cell_value(student, date):
    diary_student = Diary.objects.filter(day=date, student=student).last()
    if datetime.datetime(date.year, date.month, date.day) > datetime.datetime.now():
        cell = ''
    elif diary_student:
        cell = diary_student.point
    elif NotParticipating.objects.filter(day=date, student=student).last():
        cell = 'q/b'
    else:
        cell = 'i/e'
    return cell

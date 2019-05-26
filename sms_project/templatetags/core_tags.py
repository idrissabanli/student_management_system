import datetime

from django import template
from django.utils import timezone

from sms_project.models import NotParticipating, Diary, Monitoring

register = template.Library()


@register.simple_tag()
def cell_value(student, date):
    diary_student = Diary.objects.filter(day=date, student=student).last()
    # if datetime.datetime(date.year, date.month, date.day) > datetime.datetime.now():
    #     cell = ''
    if diary_student:
        cell = diary_student.point
    elif NotParticipating.objects.filter(day=date, student=student).last():
        cell = 'q/b'
    else:
        cell = 'i/e'
    return cell


@register.simple_tag()
def total_point(student, group_subject):
    student_monitorings = student.student_monitoring_points.filter(monitoring__group_subject=group_subject)
    monitorings_total = 0
    for student_monitoring in student_monitorings:
        monitorings_total += student_monitoring.point

    monitorings_total = monitorings_total/student_monitorings.count()

    print(monitorings_total)

    diary_points = student.dairies.filter(day__year=timezone.now().year)
    diary_points_total = 0

    for diary_point in diary_points:
        diary_points_total += diary_point.point

    diary_points_total = diary_points_total/diary_points.count() * 2

    print(diary_points_total)

    works = group_subject.works.filter(lastday__year=timezone.now().year)
    work_point = 0
    for work in works:
        work_point += work.student_works.filter(student=student).count()
    print(work_point)
    return "{0:.2f}".format(work_point + diary_points_total + monitorings_total)



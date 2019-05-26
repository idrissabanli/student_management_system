from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from datetime import date, timedelta

# Create your views here.
from sms_project.models import GroupSubject, Table


class DashBoard(LoginRequiredMixin, TemplateView):
    model = GroupSubject
    template_name = 'dashboard.html'

    def dispatch(self, request, *args, **kwargs):
        user = self.request.user
        if user.is_staff:
            url = reverse('admin:index')
            return redirect(url)
        return super(DashBoard, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        if not hasattr(user, 'student'):
            raise PermissionDenied
        student = user.student
        group = student.group
        group_subjects = group.group_subjects.filter(semester=group.semester)
        message_list = []
        if not group_subjects:
            message_list.append('Sizin üçün fənn tapılmadı')
        context['messages'] = message_list
        context['group_subjects'] = group_subjects
        return context


def allsundays(year, weekday, semester_start_month):
    d = date(year, semester_start_month, 22)  # January 1st
    d += timedelta(days=weekday - d.weekday())  # First Sunday
    count = 1
    while count <= 15:
        count += 1
        yield d
        d += timedelta(days=7)


class TableView(LoginRequiredMixin, TemplateView):
    model = Table
    template_name = 'table.html'

    def dispatch(self, request, *args, **kwargs):
        user = self.request.user
        if user.is_staff:
            url = reverse('admin:index')
            return redirect(url)
        return super(TableView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        if not hasattr(user, 'student'):
            raise PermissionDenied
        student = user.student
        group = student.group
        group_subject = group.group_subjects.filter(semester=group.semester, id=kwargs.get('id')).last()
        tables = group_subject.tables.filter()
        dates = []
        semester = group.semester.name
        semester_start_month = 2 if int(semester%2) == 0 else 9
        for table in tables:
            for d in allsundays(timezone.now().year, table.weekday-1, semester_start_month):
                dates.append(d)
        students = group.students.filter(is_published=True)
        context['dates'] = sorted(dates)
        context['students'] = students
        context['group_subject'] = group_subject
        context['year'] = timezone.now().year
        context['per_year'] = 'I' if semester_start_month == 9 else 'II'
        return context

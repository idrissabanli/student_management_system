from django.contrib import admin

# Register your models here.
from sms_project.models import Faculty, Specialty, Semester, Group, Student, Subject, Department, Teacher, GroupSubject, \
    Table, Diary, NotParticipating, Work, StudentWork, Monitoring, StudentMonitoringPoint


class FacultyAdmin(admin.ModelAdmin):
    model = Faculty
    list_display = ('name', 'created_at', 'is_published',)


class SpecialtyAdmin(admin.ModelAdmin):
    model = Specialty
    list_display = ('name', 'created_at', 'is_published',)


class SemesterAdmin(admin.ModelAdmin):
    model = Semester
    list_display = ('name', 'created_at', 'is_published',)


class GroupAdmin(admin.ModelAdmin):
    model = Group
    list_display = ('name', 'specialty', 'semester', 'created_at', 'is_published',)


class StudentAdmin(admin.ModelAdmin):
    model = Student
    list_display = ('user', 'group', 'created_at', 'is_published',)


class SubjectAdmin(admin.ModelAdmin):
    model = Subject
    list_display = ('name', 'created_at', 'is_published',)


class DepartmentAdmin(admin.ModelAdmin):
    model = Department
    list_display = ('name', 'created_at', 'is_published',)


class TeacherAdmin(admin.ModelAdmin):
    model = Teacher
    list_display = ('user', 'department', 'created_at', 'is_published',)


class GroupSubjectAdmin(admin.ModelAdmin):
    model = GroupSubject
    list_display = ('group', 'subject', 'semester', 'teacher', 'created_at', 'is_published',)


class TableAdmin(admin.ModelAdmin):
    model = Table
    list_display = ('group_subject', 'weekday', 'lesson_time', 'week_type', 'subject_type',
                    'created_at', 'is_published',)


class DiaryAdmin(admin.ModelAdmin):
    model = Diary
    list_display = ('student', 'table', 'point', 'day',
                    'created_at', 'is_published',)


class NotParticipatingAdmin(admin.ModelAdmin):
    model = NotParticipating
    list_display = ('student', 'table', 'day', )


class WorkAdmin(admin.ModelAdmin):
    model = Work
    list_display = ('name', 'group_subject', 'lastday',
                    'created_at', 'is_published',)


class StudentWorkAdmin(admin.ModelAdmin):
    model = StudentWork
    list_display = ('student', 'work', 'created_at', 'is_published',)


class MonitoringAdmin(admin.ModelAdmin):
    model = Monitoring
    list_display = ('group_subject', 'date', 'created_at', 'is_published',)


class StudentMonitoringPointAdmin(admin.ModelAdmin):
    model = StudentMonitoringPoint
    list_display = ('monitoring', 'student', 'point', 'created_at', 'is_published',)


admin.site.register(StudentMonitoringPoint, StudentMonitoringPointAdmin)
admin.site.register(Monitoring, MonitoringAdmin)
admin.site.register(StudentWork, StudentWorkAdmin)
admin.site.register(Work, WorkAdmin)
admin.site.register(NotParticipating, NotParticipatingAdmin)
admin.site.register(Diary, DiaryAdmin)
admin.site.register(Table, TableAdmin)
admin.site.register(GroupSubject, GroupSubjectAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Semester, SemesterAdmin)
admin.site.register(Specialty, SpecialtyAdmin)
admin.site.register(Faculty, FacultyAdmin)

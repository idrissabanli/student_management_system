from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

User = get_user_model()

# Create your models here.


class Faculty(models.Model):
    name = models.CharField('Adı', max_length=100, )
    is_published = models.BooleanField(_('Is Published'), default=True, )
    created_at = models.DateTimeField(editable=False, default=timezone.now())
    updated_at = models.DateTimeField(editable=False, auto_now=True)

    class Meta:
        verbose_name = 'Fakültə'
        verbose_name_plural = 'Fakültələr'

    def __str__(self):
        return self.name


class Specialty(models.Model):
    name = models.CharField('Adı', max_length=100, )
    faculty = models.ForeignKey(Faculty, related_name='specialties', on_delete=models.CASCADE)
    is_published = models.BooleanField(_('Is Published'), default=True, )
    created_at = models.DateTimeField(editable=False, default=timezone.now())
    updated_at = models.DateTimeField(editable=False, auto_now=True)

    class Meta:
        verbose_name = 'İxtisas'
        verbose_name_plural = 'İxtisaslar'

    def __str__(self):
        return self.name


class Semester(models.Model):
    name = models.PositiveIntegerField('Adı', max_length=10, )
    is_published = models.BooleanField(_('Is Published'), default=True, )
    created_at = models.DateTimeField(editable=False, default=timezone.now())
    updated_at = models.DateTimeField(editable=False, auto_now=True)

    class Meta:
        verbose_name = 'Semestr'
        verbose_name_plural = 'Semestrlər'

    def __str__(self):
        return str(self.name)


class Group(models.Model):
    name = models.CharField('Adı', max_length=10, )
    specialty = models.ForeignKey(Specialty, related_name='Group', on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, related_name='students', on_delete=models.CASCADE)
    is_published = models.BooleanField(_('Is Published'), default=True, )
    created_at = models.DateTimeField(editable=False, default=timezone.now())
    updated_at = models.DateTimeField(editable=False, auto_now=True)

    class Meta:
        verbose_name = 'Qrup'
        verbose_name_plural = 'Qruplar'

    def __str__(self):
        return self.name


class Student(models.Model):
    group = models.ForeignKey(Group, related_name='students', on_delete=models.CASCADE)
    user = models.OneToOneField(User, related_name='student', on_delete=models.CASCADE)
    phone = models.CharField('Telefon nömrəsi', max_length=20, null=True, blank=True)
    father_name = models.CharField('Ata adı', max_length=30)
    birth_date = models.DateField('Doğum tarixi')
    admission_date = models.DateField('Qəbul ili', )
    admission_point = models.PositiveIntegerField('Qəbul Balı', )
    is_published = models.BooleanField(_('Is Published'), default=True, )
    created_at = models.DateTimeField(editable=False, default=timezone.now())
    updated_at = models.DateTimeField(editable=False, auto_now=True)

    class Meta:
        verbose_name = 'Tələbə'
        verbose_name_plural = 'Tələbələr'

    def __str__(self):
        return self.user.get_full_name()


class Subject(models.Model):
    name = models.CharField('Adı', max_length=100, )
    is_published = models.BooleanField(_('Is Published'), default=True, )
    created_at = models.DateTimeField(editable=False, default=timezone.now())
    updated_at = models.DateTimeField(editable=False, auto_now=True)

    class Meta:
        verbose_name = 'Fənn'
        verbose_name_plural = 'Fənnlər'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('core:table', kwargs={'id': self.id})


class Department(models.Model):
    name = models.CharField('Adı', max_length=100, )
    is_published = models.BooleanField(_('Is Published'), default=True, )
    created_at = models.DateTimeField(editable=False, default=timezone.now())
    updated_at = models.DateTimeField(editable=False, auto_now=True)

    class Meta:
        verbose_name = 'Kafedra'
        verbose_name_plural = 'Kafedralar'

    def __str__(self):
        return self.name


class Teacher(models.Model):
    user = models.OneToOneField(User, related_name='teacher', on_delete=models.CASCADE)
    department = models.OneToOneField(Department, related_name='teachers', on_delete=models.CASCADE)
    father_name = models.CharField('Ata adı', max_length=30)
    is_published = models.BooleanField(_('Is Published'), default=True, )
    created_at = models.DateTimeField(editable=False, default=timezone.now())
    updated_at = models.DateTimeField(editable=False, auto_now=True)

    class Meta:
        verbose_name = 'Müəllim'
        verbose_name_plural = 'Müəllimlər'

    def __str__(self):
        return self.user.get_full_name()


class GroupSubject(models.Model):
    group = models.ForeignKey(Group, related_name='group_subjects', on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, related_name='group_subjects', on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, related_name='group_subjects', on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, related_name='group_subjects', on_delete=models.CASCADE)
    is_published = models.BooleanField(_('Is Published'), default=True, )
    created_at = models.DateTimeField(editable=False, default=timezone.now())
    updated_at = models.DateTimeField(editable=False, auto_now=True)

    class Meta:
        verbose_name = 'Qrup fənni'
        verbose_name_plural = 'Qrup fənnləri'

    def __str__(self):
        return self.group.name + ' subject: ' + self.subject.name


WEEKDAYS = ((1, 'I'), (2, 'II'), (3, 'III'), (4, 'IV'), (5, 'V'))
LESSON_TIMES = ((1, '08:30-10:05'), (2, '10:15-11:50'), (3, '12:00-13:35'), (4, '13:50-15:25'), (5, '15:35-17:10'),
                (6, '17:20-18:55'))
week_type = ((1, 'Üst həftə'), (2, 'Alt həftə'))
SUBJECT_TYPE = ((1, 'Mühazirə'), (2, 'Seminar'), (2, 'Laboratoriya'))


class Table(models.Model):
    group_subject = models.ForeignKey(GroupSubject, on_delete=models.CASCADE, related_name='tables', )
    weekday = models.PositiveIntegerField('Həftənin günü', choices=WEEKDAYS)
    lesson_time = models.PositiveIntegerField('Dərs vaxtı', choices=LESSON_TIMES)
    week_type = models.PositiveIntegerField('Həftə', choices=week_type, null=True, blank=True)
    subject_type = models.PositiveIntegerField('Dərs tipi', choices=SUBJECT_TYPE, default=1)
    is_published = models.BooleanField(_('Is Published'), default=True, )
    created_at = models.DateTimeField(editable=False, default=timezone.now())
    updated_at = models.DateTimeField(editable=False, auto_now=True)

    class Meta:
        verbose_name = 'Cədvəl'
        verbose_name_plural = 'Cədvəl'

    def __str__(self):
        return self.group_subject.group.name + ' subject: ' + self.group_subject.subject.name + ' Həftənin günü:' +\
               str(self.weekday) + ' Dərs vaxtı: ' + str(self.lesson_time)


class Diary(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='dairies', )
    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name='dairies', )
    point = models.PositiveIntegerField('Bal', )
    day = models.DateField('Gün', default=timezone.now())
    is_published = models.BooleanField(_('Is Published'), default=True, )
    created_at = models.DateTimeField(editable=False, default=timezone.now())
    updated_at = models.DateTimeField(editable=False, auto_now=True)

    class Meta:
        verbose_name = 'Gündəlik qiymət'
        verbose_name_plural = 'Gündəlik qiymətlər'

    def __str__(self):
        return self.student.user.get_full_name()


class NotParticipating(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='not_participatings', )
    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name='not_participatings', )
    day = models.DateField('Gün', default=timezone.now())

    class Meta:
        verbose_name = 'Qayıblar'
        verbose_name_plural = 'Qayıblar'

    def __str__(self):
        return self.student.user.get_full_name()


class Work(models.Model):
    name = models.CharField('İşin adı', max_length=255)
    group_subject = models.ForeignKey(GroupSubject, on_delete=models.CASCADE, related_name='works',)
    lastday = models.DateField('Son Gün', default=timezone.now())
    is_published = models.BooleanField(_('Is Published'), default=True, )
    created_at = models.DateTimeField(editable=False, default=timezone.now())
    updated_at = models.DateTimeField(editable=False, auto_now=True)

    class Meta:
        verbose_name = 'Sərbəst iş'
        verbose_name_plural = 'Sərbəst işlər'

    def __str__(self):
        return self.name


class StudentWork(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student_works')
    work = models.ForeignKey(Work,  on_delete=models.CASCADE, related_name='student_works')
    point = models.PositiveIntegerField('Bal', )
    is_published = models.BooleanField(_('Is Published'), default=True, )
    created_at = models.DateTimeField(editable=False, default=timezone.now())
    updated_at = models.DateTimeField(editable=False, auto_now=True)

    class Meta:
        verbose_name = 'Tələbənin sərbəst işi'
        verbose_name_plural = 'Tələbələrin sərbəst işləri'

    def __str__(self):
        return self.student.user.get_full_name() + ' iş:' + self.work.name


class Monitoring(models.Model):
    group_subject = models.ForeignKey(GroupSubject, on_delete=models.CASCADE, related_name='monitorings', )
    date = models.DateField('Gün',)
    is_published = models.BooleanField(_('Is Published'), default=True, )
    created_at = models.DateTimeField(editable=False, default=timezone.now())
    updated_at = models.DateTimeField(editable=False, auto_now=True)

    class Meta:
        verbose_name = 'Monitorinq'
        verbose_name_plural = 'Monitorinqlər'

    def __str__(self):
        return self.group_subject.group.name + ' gün:' + str(self.date)


class StudentMonitoringPoint(models.Model):
    monitoring = models.ForeignKey(Monitoring, on_delete=models.CASCADE, related_name='student_monitoring_points', )
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student_monitoring_points', )
    point = models.PositiveIntegerField('Bal', )
    is_published = models.BooleanField(_('Is Published'), default=True, )
    created_at = models.DateTimeField(editable=False, default=timezone.now())
    updated_at = models.DateTimeField(editable=False, auto_now=True)

    class Meta:
        verbose_name = 'Tələbənin monitorinqi'
        verbose_name_plural = 'Tələbələrin monitorinqləri'

    def __str__(self):
        return self.student.user.get_full_name()
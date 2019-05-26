from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

# example of signal
from sms_project.models import StudentMonitoringPoint, Monitoring


@receiver(post_save,sender=Monitoring,dispatch_uid='monitoring_save')
def monitoring_save(sender, created, **kwargs):
    if created:
        monitoring = kwargs.get('instance')
        students = monitoring.group_subject.group.students.filter(is_published=True)
        for student in students:
            StudentMonitoringPoint.objects.create(monitoring=monitoring, student=student, point=0)
    return True



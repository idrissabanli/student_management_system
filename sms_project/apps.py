from django.apps import AppConfig


class SmsProjectConfig(AppConfig):
    name = 'sms_project'

    def ready(self):
        import sms_project.signals
        import sms_project.tasks

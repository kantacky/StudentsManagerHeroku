from django.db import models

# Create your models here.

from django.conf import settings
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from django.utils import timezone

class LoginRecord(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name = 'User', on_delete = models.PROTECT)
    login_time = models.DateTimeField('LoggedInTime', blank = True, null = True)
    logout_time = models.DateTimeField('LoggedOutTime', blank = True, null = True)

    def __str__(self):
        login_dt = timezone.localtime(self.login_time)
        return '{0} - {1.year}/{1.month}/{1.day} {1.hour}:{1.minute}:{1.second} - {2}'.format(self.user.username, login_dt, self.get_diff_time())

    def get_diff_time(self):
        if not self.logout_time:
            return 'Still Being'
        else:
            td = self.logout_time - self.login_time
            return '{0}h {1}min'.format(td.seconds // 3600, (td.seconds // 60) % 60)


@receiver(user_logged_in)
def user_logged_in_callback(sender, request, user, **kwargs):
    LoginRecord.objects.create(user=user, login_time=timezone.now())


@receiver(user_logged_out)
def user_logged_out_callback(sender, request, user, **kwargs):
    records = LoginRecord.objects.filter(user=user, logout_time__isnull=True)
    if records:
        record = records.latest('pk')
        record.logout_time = timezone.now()
        record.save()

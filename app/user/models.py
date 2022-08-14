from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models import signals
# Create your models here.


class User(AbstractUser):
    pass


class UserProfile(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)
    avatar = models.ImageField(upload_to="avatar/", blank=True)

    def __str__(self):
        return self.user.username


@receiver(signal=signals.post_save, sender=User)
def create_user_profile(instance, **kwargs):
    filtered = UserProfile.objects.filter(user=instance)
    if not filtered.exists():
        UserProfile.objects.create(user=instance)
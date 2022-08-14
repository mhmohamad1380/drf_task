from django.db import models
from user.models import User
import inspect
from django.dispatch import receiver
from django.db.models import signals

# Create your models here.


class Note(models.Model):
    note = models.TextField()
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.note[0:20]


@receiver(signal=signals.post_save, sender=Note)
def change_note_user(instance, **kwargs):
    request = None
    for frame_record in inspect.stack():
        if frame_record[3] == 'get_response':
            request = frame_record[0].f_locals['request']
            break
    else:
        request = None

    note = Note.objects.filter(id=instance.id)
    note.update(user=request.user)


class LikeNote(models.Model):
    likedby = models.ForeignKey(to=User, on_delete=models.CASCADE)
    likednote = models.ForeignKey(to=Note, on_delete=models.CASCADE)

    def __str__(self):
        return (f"{self.likedby.username} {self.likednote.id}")

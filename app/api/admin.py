from django.contrib import admin

from .models import LikeNote, Note

# Register your models here.

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    pass

@admin.register(LikeNote)
class LikeNoteAdmin(admin.ModelAdmin):
    pass


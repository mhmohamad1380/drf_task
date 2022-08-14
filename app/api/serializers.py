from rest_framework.serializers import ModelSerializer, SerializerMethodField
from user.models import UserProfile
from .models import LikeNote, Note


class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = ["note"]


class NoteListSerializer(ModelSerializer):
    def get_user(self, obj):
        return {
            "id": obj.user.id,
            "username": obj.user.username
        }

    user = SerializerMethodField('get_user')

    class Meta:
        model = Note
        fields = "__all__"

class LikeNoteSerializer(ModelSerializer):
    class Meta:
        model = LikeNote
        fields = "__all__"
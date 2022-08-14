

from rest_framework.generics import RetrieveAPIView, CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from .models import LikeNote, Note
from rest_framework.views import APIView
from user.models import UserProfile
from rest_framework.permissions import IsAuthenticated, AllowAny
from .permissions import IsValidUser, IsAuthor
from .serializers import NoteSerializer, UserProfileSerializer, NoteListSerializer
from rest_framework import status
from rest_framework.response import Response
import json
# Create your views here.


class UserProfileAPIView(RetrieveAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsValidUser, ]


class NoteAPIView(CreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated, ]


class NoteListAPIView(ListAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteListSerializer
    permission_classes = [AllowAny,]

class NoteRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteListSerializer
    permission_classes = [IsAuthor,]

class LikeNoteCreateAPIView(APIView):
    permission_classes = [IsAuthenticated,]

    def get(self, request):
        if "note" not in self.request.GET:
            return Response(data={
                "response": "something went error!!!"
            }, status=status.HTTP_404_NOT_FOUND)
        note_id = self.request.GET['note']
        note = Note.objects.filter(id=note_id)
        if not note.exists():
            return Response(data={
                "response": "this note doesn't exist"
            }, status=status.HTTP_404_NOT_FOUND)
        filtered_like_note = LikeNote.objects.filter(likedby=self.request.user, likednote=note.first())
        if not filtered_like_note.exists():
            LikeNote.objects.create(likedby=self.request.user, likednote=note.first())
            return Response(status=status.HTTP_200_OK, data={
                "like": "OK",
                "note_id": note_id
            })
        return Response(status=status.HTTP_400_BAD_REQUEST, data={
            "like": "You have liked this Note before!!!",
            "note_id": note_id
        })

class DislikeNoteCreateAPIView(APIView):
    permission_classes = [IsAuthenticated,]

    def get(self, request):
        if "note" not in self.request.GET:
            return Response(data={
                "response": "something went error!!!"
            }, status=status.HTTP_404_NOT_FOUND)
        note_id = self.request.GET['note']
        note = Note.objects.filter(id=note_id)
        if not note.exists():
            return Response(data={
                "response": "this note doesn't exist"
            }, status=status.HTTP_404_NOT_FOUND)
        filtered_like_note = LikeNote.objects.filter(likedby=self.request.user, likednote=note.first())
        if filtered_like_note.exists():
            filtered_like_note.delete()
            return Response(status=status.HTTP_200_OK, data={
                "dislike": "OK",
                "note_id": note_id
            })
        return Response(status=status.HTTP_400_BAD_REQUEST, data={
            "dislike": "You have disliked this Note before!!!",
            "note_id": note_id
        })
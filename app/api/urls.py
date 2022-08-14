from django.contrib import admin
from django.urls import path, include, re_path
from dj_rest_auth.views import LoginView, LogoutView
from dj_rest_auth.registration.urls import RegisterView, VerifyEmailView
from .views import NoteListAPIView, UserProfileAPIView, NoteAPIView, NoteRetrieveUpdateDestroyAPIView, LikeNoteCreateAPIView,DislikeNoteCreateAPIView

urlpatterns = [
    path("register/", RegisterView.as_view()),
    path("login/", LoginView.as_view()),
    path("logout/", LogoutView.as_view()),
    path('verify-email/',
         VerifyEmailView.as_view(), name='rest_verify_email'),
    path('account-confirm-email/',
         VerifyEmailView.as_view(), name='account_email_verification_sent'),
    re_path(r'^account-confirm-email/(?P<key>[-:\w]+)/$',
            VerifyEmailView.as_view(), name='account_confirm_email'),

    #  User
    path("users/profile/<pk>", UserProfileAPIView.as_view()),
    # Note
    path("notes/create/", NoteAPIView.as_view()),
    path("notes/list/", NoteListAPIView.as_view()),
    path("notes/edit/<pk>", NoteRetrieveUpdateDestroyAPIView.as_view()),
    path("notes/like", LikeNoteCreateAPIView.as_view()),
    path("notes/dislike", DislikeNoteCreateAPIView.as_view()),
]

from django.urls import path

from . import views

urlpatterns = [
    path("<str:email>/", views.ChatMessagesView.as_view(), name="chat"),
]

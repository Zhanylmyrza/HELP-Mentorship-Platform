from rest_framework import serializers

from .models import ChatModel


class ChatModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatModel
        fields = "__all__"

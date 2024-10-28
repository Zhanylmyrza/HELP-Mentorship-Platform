from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from accounts.models import UserAccount
from chat.models import ChatModel
from chat.serializers import ChatModelSerializer


User = get_user_model()


class ChatMessagesView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, email, *args, **kwargs):
        user_obj = UserAccount.objects.get(email=email)  # request.user
        print("user_obj: ", user_obj)
        users = UserAccount.objects.exclude(email=request.user.email)
        print("users: ", users)

        if request.user.id > user_obj.id:
            thread_name = f"chat_{request.user.id}-{user_obj.id}"
        else:
            thread_name = f"chat_{user_obj.id}-{request.user.id}"
        message_objs = ChatModel.objects.filter(thread_name=thread_name)
        print("message_objs: ", message_objs)
        serializer = ChatModelSerializer(message_objs, many=True)
        return Response(serializer.data)

from rest_framework import generics, permissions
from rest_framework.response import Response

from todo_list.bot.models import TgUser
from todo_list.bot.serializers import TgUserSerializer
from todo_list.bot.tg.client import TgClient
from todo_list.todo_list import settings


class VerificationView(generics.GenericAPIView):
    model = TgUser
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TgUserSerializer

    def patch(self, request, *args, **kwargs):
        s:TgUserSerializer = self.get_serializer(data=request.data)
        s.is_valid(raise_exception=True)

        tg_user: TgUser = s.validated_data["tg_user"]
        tg_user.user = self.request.user
        tg_user.save(update_fields=("user",))

        instance_s: TgUserSerializer = self.get_serializer(tg_user)
        TgClient(settings.BOT_TOKEN).send_message(tg_user.chat_id, "[verification_has_been_completed]")
        return Response(instance_s.data)

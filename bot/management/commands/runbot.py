from bot.tg.client import TgClient
from django.core.management import BaseCommand

from todo_list import settings
from bot.models import TgUser
from bot.tg.models import Message


class Command(BaseCommand):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tg_client = TgClient(settings.BOT_TOKEN)a

    def handle_message(self, msg: Message):
        tg_user, _ = TgUser.objects.select_related("user").get_or_create(
            chat_id=msg.chat.id,
            defaults={
                "username": msg.from_.username
            }
        )
        if tg_user.user:
            self.handle_verified_user(msg=msg, tg_user=tg_user)
        else:
            self.handle_unverified_user(msg=msg, tg_user=tg_user)

    def handle(self, *args, **options):
        offset = 0
        while True:
            res = self.tg_client.get_updates(offset=offset)
            for item in res.result:
                offset = item.update_id + 1
                self.tg_client.send_message(chat_id=item.message.chat.id, text=item.message.text)




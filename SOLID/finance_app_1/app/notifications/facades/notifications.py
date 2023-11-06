from notifications.services.formatters import AbstractFormatterService, \
    TelegramFormatterService
from notifications.services.senders import AbstractSenderService, \
    TelegramSenderService


class AbstractNotificationFacade:
    def __init__(
            self,
            sender: AbstractSenderService,
            formatter: AbstractFormatterService,
    ):
        self.sender = sender
        self.formatter = formatter

    def send_transaction_notification(self, to, transaction):
        text = self.formatter.new_transaction(transaction)
        self.sender.send(to, text)

class AbstractNotificationFacade:

    def send_transaction_notifications(self, transactions):
        for transaction in transactions:
            pass


class NotificationService(AbstractNotificationFacade):
    def send_transaction_notifications(self, transaction):
        return




class TelegramNotificationFacade(AbstractNotificationFacade):
    def __init__(self, formatter, sender):
        self.sender = sender
        self.formatter = formatter

    def send_transaction_notifications(self, transaction):
        pass



class TelegramFormatterService:
    def new_transaction(self, transaction):
        return 'Some transaction text for telegram'

class EmailFormatterService:
    def new_transaction(self, transaction):
        return 'Some transaction text for email'

class SMSFormatterService:
    def new_transaction(self, transaction):
        return 'Some transaction text for sms'



class TelegramSenderService:
    def send(self, chat_id, text):
        pass

class EmailSenderService:
    def send(self, email, text):
        pass

class SMSSenderService:
    def send(self, phone, text):
        pass

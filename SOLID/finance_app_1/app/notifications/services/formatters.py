from abc import abstractmethod


class AbstractFormatterService:
    @abstractmethod
    def new_transaction(self, transaction)-> str:
        raise NotImplementedError('Not implemented')


class TelegramFormatterService(AbstractFormatterService):
    def new_transaction(self, transaction):
        return 'Some transaction text for telegram'


class EmailFormatterService(AbstractFormatterService):
    def new_transaction(self, transaction):
        return 'Some transaction text for email'


class SMSFormatterService(AbstractFormatterService):
    def new_transaction(self, transaction):
        return 'Some transaction text for sms'

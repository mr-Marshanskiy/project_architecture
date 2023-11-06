from abc import abstractmethod


class AbstractSenderService:
    @abstractmethod
    def send(self, to, text) -> None:
        raise NotImplementedError('Not implemented')


class TelegramSenderService(AbstractSenderService):
    def send(self, to, text):
        pass


class EmailSenderService(AbstractSenderService):
    def send(self, to, text):
        pass


class SMSSenderService(AbstractSenderService):
    def send(self, to, text):
        pass

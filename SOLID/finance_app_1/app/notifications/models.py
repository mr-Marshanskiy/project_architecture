from accounts.models import Account


class NotificationLimit:
    def __init__(self, account: Account, limit):
        self.account = account
        self.limit = limit


class NotificationOption:
    def __init__(self, user, options, notification_type, status=True):
        self.user = user
        self.options = options
        self.status = status
        self.notification_type = notification_type

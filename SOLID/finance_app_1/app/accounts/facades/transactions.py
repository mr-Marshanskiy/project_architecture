

class TransactionFacade:
    def __init__(
            self,
            notification_service,
            notification_option_service,
            account_limit_service,
            transaction_service,
    ):
        self.notification_service = notification_service
        self.notification_option_service = notification_option_service
        self.account_limit_service = account_limit_service
        self.transaction_service = transaction_service

    def create_transaction(self, validated_data):
        transaction = self.transaction_service.create(validated_data)
        notifications = self.notification_option_service.get_transaction_notifications(transaction)
        self.notification_service.send_transaction_notifications(notifications)
        return transaction

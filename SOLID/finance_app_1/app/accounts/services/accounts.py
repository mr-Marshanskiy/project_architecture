from accounts.models import Account


class TransactionService:
    model = Account

    def create_account(self, validated_data):
        account = None
        # Create a new account
        return account

    def update_account(self, account, validated_data):
        # Update the account
        return account

    def destroy_account(self, account):
        # Destroy the account
        return

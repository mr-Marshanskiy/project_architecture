from currency.models import Currency


class AccountType:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class Account:
    def __init__(self, id, user, name, currency: Currency, account_type: AccountType):
        self.id = id
        self.user = user
        self.name = name
        self.currency = currency
        self.account_type = account_type
        self.balance = 0


class TransactionType:
    def __init__(self, name):
        self.name = name


class Transaction:
    def __init__(
            self,
            id,
            from_account: Account,
            to_account: Account,
            transaction_type: TransactionType,
            amount
    ):
        self.id = id
        self.from_account = from_account
        self.to_account = to_account
        self.transaction_type = transaction_type
        self.amount = amount

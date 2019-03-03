from django.apps import AppConfig


class WalletConfig(AppConfig):
    name = 'transactions'

    def ready(self):
        import transactions.signals
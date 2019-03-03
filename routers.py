from rest_framework.routers import SimpleRouter

from wallet.api.views  import TransactionsViewSet

router_v1 = SimpleRouter(trailing_slash=False)
router_v1.register(r'transactions', TransactionsViewSet, base_name='transactions')

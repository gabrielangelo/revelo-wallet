from django.test import TestCase

from model_mommy import mommy

from ..api.views import TransactionsViewSet
from ..models import Transaction
from core.test_utils import resolve_by_name

class TransactionUrlsViewSetTest(TestCase):
    def setUp(self):
        self.resolve = resolve_by_name('transactions-list')

    def test_resolves_list_url(self):
        self.assertEqual(self.resolve.func.cls, TransactionsViewSet)
    
    def test_resolves_to_list_action(self):
        self.assertIn('get', self.resolve.func.actions) 
        self.assertEqual('list', self.resolve.func.actions['get']) 

    def test_resolves_to_create_action(self):
        self.assertIn('post', self.resolve.func.actions)
        self.assertEqual('create', self.resolve.func.actions['post'])

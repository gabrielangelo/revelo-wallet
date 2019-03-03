from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework.test import APIClient, APITestCase
from rest_framework import status

from core.test_utils import ClientNativeTokenAuthorizationMixin
from model_mommy import mommy
from ..models import Transaction
import json

class TransactionApiTest(ClientNativeTokenAuthorizationMixin, APITestCase):
    def setUp(self):
        self.transaction_params = {
            'value':2.44, 
            'type_transaction':0, 
            'name':'whatever'
        }
        self.user = self.make_user()

        self.url = reverse('transactions-list')
        self.authorized_client = self.make_authorized_client(self.user)
        self.anonymous_client = self.make_anonymous_client()
        
    def test_non_permission_list(self):
        response = self.anonymous_client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_non_permission_create(self):
        response = self.anonymous_client.post(self.url, self.transaction_params, format=u'json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_permission_list_transactions(self):
        response = self.authorized_client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_permission_post_transactions(self):
        response = self.authorized_client.post(self.url, self.transaction_params, format=u'json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def get_status_code_and_payload(self, params):
        response = self.authorized_client.post(self.url, params, format=u'json')
        status_code = response.status_code
        payload = json.loads(response.content.decode('utf-8'))
        return status_code, payload

    def test_status_transaction_with_negative_value(self):
        transaction_negative_params = {
            'value':-10, 
            'type_transaction':0, 
            'name':'whatever'
        }
        status_code, payload = self.get_status_code_and_payload(transaction_negative_params)
        self.assertEqual(status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('value', payload.keys())

    def test_status_transaction_with_invalid_type_transaction_value(self):
        transaction_invalid_type_transaction_params = {
            'value':10, 
            'type_transaction':10, 
            'name':'whatever'
        }
        status_code, payload = self.get_status_code_and_payload(
            transaction_invalid_type_transaction_params
        )
        self.assertEqual(status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('type_transaction', payload.keys())
        
    def test_status_transaction_with_float_value(self):
        transaction_float_value_params = {
            'value':10.98989, 
            'type_transaction':10, 
            'name':'whatever'
        }
        status_code, payload = self.get_status_code_and_payload(
            transaction_float_value_params
        )
        self.assertEqual(status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('value', payload.keys())
    
    def test_status_invalid_currency(self):
        transaction_invalid_currency_value_params = {
            'value':10.98, 
            'type_transaction':0, 
            'name':'whatever', 
            'currency':'whatever'
        }
        status_code, payload = self.get_status_code_and_payload(
            transaction_invalid_currency_value_params
        )
        self.assertEqual(status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('currency', payload.keys())

    def test_payload_value_transaction_low_currency_value_input(self):
        transaction_low_currency_value = {
            'value':10.98, 
            'type_transaction':0, 
            'name':'whatever', 
            'currency':'u$'
        }
        _, payload = self.get_status_code_and_payload(transaction_low_currency_value)
        self.assertEqual(payload['currency'], transaction_low_currency_value['currency'].upper())
    
    def test_payload_value_default_currency_value_input(self):
        transaction_low_currency_value = {
            'value':10.98, 
            'type_transaction':0, 
            'name':'whatever', 
        }
        _, payload = self.get_status_code_and_payload(transaction_low_currency_value)
        self.assertEqual(payload['currency'], 'R$')



    

    
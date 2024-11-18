from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from orders.models import Customer, Order
from unittest.mock import patch
from django.test import TestCase
from unittest.mock import patch
from patientordersystem.utils import send_sms

class CustomerViewTests(APITestCase):

    # Test for adding a customer successfully
    def test_add_customer_success(self):
        url = reverse('add-customer')  # Using the URL pattern name
        data = {
            'name': 'Test Customer',
            'code': 'CUST123',
            'contact_number': '+254700000000',
            'email': 'test@customer.com',
            'insurance_number': 'INS123456'
        }
        
        response = self.client.post(url, data, format='json')

        # Assert the response status code is 201 CREATED
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Verify that the customer is saved in the database
        customer = Customer.objects.get(code='CUST123')
        self.assertEqual(customer.name, 'Test Customer')
        self.assertEqual(customer.contact_number, '+254700000000')

    # Test for adding a customer with invalid data
    def test_add_customer_failure(self):
        url = reverse('add-customer')
        data = {
            'name': '',  # Invalid data (empty name)
            'code': 'CUST124',
            'contact_number': '+254700000000',
            'email': 'invalid@customer.com',
            'insurance_number': 'INS123456'
        }

        response = self.client.post(url, data, format='json')

        # Assert the response status code is 400 BAD REQUEST
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # Test for listing customers (ensure authentication is required)
    def test_list_customers_authenticated(self):
        # Setup a customer
        customer = Customer.objects.create(
            name='Test Customer', 
            code='CUST125', 
            contact_number='+254700000001'
        )
        
        url = reverse('list_customers')  # URL to list customers

        # Authenticate using the token
        # self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)  # Ensure you have a valid token

        response = self.client.get(url)

        # Assert that the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'Test Customer')  # Ensure the customer is listed

class OrderViewTests(APITestCase):

    # Test for adding an order successfully
    def test_add_order_success(self):
        customer = Customer.objects.create(
            name="Test Customer",
            code="CUST123",
            contact_number="+254700000000",
            email="test@customer.com",
            insurance_number="INS123456"
        )

        url = reverse('add-orders')  # Using the URL pattern name
        data = {
            'customer': customer.id,  # Pass the customer's ID for the foreign key field
            'item': 'Test Item',
            'amount': 1000.00,
            'physician_name': 'Dr. Smith'  # Example physician name
        }

        response = self.client.post(url, data, format='json')

        # Assert the response status code is 201 CREATED
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Verify that the order is saved in the database
        order = Order.objects.get(id=response.data['id'])
        self.assertEqual(order.item, 'Test Item')
        self.assertEqual(order.amount, 1000.00)
        self.assertEqual(order.customer_phone, '+254700000000')  # Checking the property indirectly

    # Test for listing orders (ensure authentication is required)
    def test_list_orders_authenticated(self):
        # Set up a customer and an order
        customer = Customer.objects.create(
            name="Test Customer",
            code="CUST125",
            contact_number='+254700000001',
            email="test2@customer.com",
            insurance_number="INS123457"
        )

        order = Order.objects.create(
            customer=customer, 
            item="Test Item",
            amount=1000.00,
            physician_name='Dr. John'
        )

        url = reverse('list-orders')

        # Authenticate using the token if needed
        # self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

        response = self.client.get(url)

        # Assert that the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'Test Item')  # Ensure the order is listed

class SendSMSTests(TestCase):

    @patch('africastalking.SMS.send')
    def test_send_sms_success(self, mock_africastalking_send):
        # Mock the response from Africastalking to simulate a successful SMS send
        mock_africastalking_send.return_value = {
            'SMSMessageData': {
                'Message': 'Sent to 1/1 Total Cost: 0.5',
                'Recipients': [{'cost': '0.5', 'messageId': 'ABC123', 'number': '+254700000000', 'status': 'Success', 'statusCode': 101}]
            }
        }

        # Call the send_sms function
        recipient = "+254700000000"
        message = "Your order has been received."
        response = send_sms(recipient, message)

        # Verify that the mock was called with the expected arguments
        mock_africastalking_send.assert_called_once_with(message, [recipient])

        # Check that the response is as expected
        self.assertEqual(response['SMSMessageData']['Message'], 'Sent to 1/1 Total Cost: 0.5')
        self.assertEqual(response['SMSMessageData']['Recipients'][0]['status'], 'Success')

    @patch('africastalking.SMS.send')
    def test_send_sms_failure(self, mock_africastalking_send):
        # Simulate an exception being raised when trying to send the SMS
        mock_africastalking_send.side_effect = Exception("Network error")

        # Call the send_sms function
        recipient = "+254700000000"
        message = "Your order has been received."
        response = send_sms(recipient, message)

        # Verify that the mock was called once
        mock_africastalking_send.assert_called_once_with(message, [recipient])

        # Check that the response is None, indicating failure
        self.assertIsNone(response)
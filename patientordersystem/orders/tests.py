# from django.test import TestCase

# # Create your tests here.
# import pytest
# from rest_framework import status
# # from rest_framework.test import APIClient
# from django.contrib.auth.models import User
# from .models import Customer, Order
# from unittest.mock import patch


# # @pytest.fixture
# # def user():
# #     user = User.objects.create_user(username='testuser', password='testpassword')
# #     return user


# @pytest.fixture
# def customer():
#     customer = Customer.objects.create(
#         name="James Karanja",
#         code="CUST001",
#         contact_number="+254700206386",
#         email="JamesKaranja@example.com",
#         insurance_number="INS12345"
#     )
#     return customer


# @pytest.fixture
# def order(customer):
#     order = Order.objects.create(
#         customer=customer,
#         item="Test Item",
#         amount=100.00
#     )
#     return order


# # @pytest.fixture
# # def api_client():
# #     return APIClient()


# # Test the AddCustomerView
# @pytest.mark.django_db
# def test_add_customer(api_client):
#     data = {
#         "name": "Joyce Mutinda",
#         "code": "CUST002",
#         "contact_number": "+254700206387",
#         "email": "JoyceMutindae@example.com",
#         "insurance_number": "INS67890"
#     }
#     response = api_client.post("/add_customer/", data, format="json")
#     assert response.status_code == status.HTTP_201_CREATED
#     assert response.data["name"] == "Joyce Mutinda"
#     assert response.data["code"] == "CUST002"


# # Test the ListCustomersView
# @pytest.mark.django_db
# def test_list_customers(api_client, customer, user):
#     api_client.force_authenticate(user=user)
#     response = api_client.get("/list_customers/")
#     assert response.status_code == status.HTTP_200_OK
#     assert len(response.data) > 0
#     assert response.data[0]["name"] == customer.name


# # Test the AddOrderView and SMS sending
# @pytest.mark.django_db
# @patch("patientordersystem.views.send_sms")
# def test_add_order(mock_send_sms, api_client, customer, user):
#     api_client.force_authenticate(user=user)
#     data = {
#         "customer": customer.id,
#         "item": "Test Order",
#         "amount": 150.00
#     }
#     response = api_client.post("/add_order/", data, format="json")
#     assert response.status_code == status.HTTP_201_CREATED
#     assert response.data["item"] == "Test Order"
#     assert response.data["amount"] == 150.00
    
#     # Check if the send_sms function was called
#     mock_send_sms.assert_called_once_with(customer.contact_number, "Thank you for your order #1. Test Order - KSH 150.00. We’ll notify you when it’s ready!")


# # Test the ListOrderView
# @pytest.mark.django_db
# def test_list_orders(api_client, order, user):
#     api_client.force_authenticate(user=user)
#     response = api_client.get("/list_orders/")
#     assert response.status_code == status.HTTP_200_OK
#     assert len(response.data) > 0
#     assert response.data[0]["item"] == order.item

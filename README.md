
# Patient Order Management Service

A Python-based backend application for managing customers and orders. This application supports creating, retrieving, and managing customer and order data via a REST API, and includes secure authentication, SMS notifications, and automated deployment pipelines.

## link to deployed service

https://savannah-patient-order-service.onrender.com/

For testing, you can sign into the deployed application via the link above and use djangos DRF interface, it will automatically store the access token to the browser allowing you to access permission protected views, including add customer and add order views. (The list customer and list order views have been left unprotected for testing).
A lsit of the endpoints has been provided below. 

## Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [System Requirements](#system-requirements)
4. [Installation and Setup](#installation-and-setup)
5. [Usage](#usage)
6. [Database Schema](#database-schema)
7. [API Endpoints](#api-endpoints)
8. [Authentication and Authorization](#authentication-and-authorization)
9. [SMS Notification](#sms-notification)
10. [Testing](#testing)
11. [Deployment](#deployment)
12. [Contributing](#contributing)
13. [License](#license)

---

## Project Overview

This service is a RESTful API for managing customer and order data. It includes simple CRUD operations for customer and order entities, OpenID Connect authentication for secure access, and SMS notifications for customers when a new order is created. 

## Features

- **Customer and Order Management:** Manage customer and order details with minimal fields.
- **RESTful API:** Provides CRUD operations for customer and order management.
- **OpenID Connect Authentication:** Secure access to the API.
- **SMS Notification:** Sends an SMS alert to customers upon order creation using the Africa’s Talking SMS gateway.
- **Continuous Integration/Continuous Deployment (CI/CD):** Automated testing and deployment.
  
## System Requirements

- **Python:** 3.8 or higher
- **Django:** 3.2 or higher
- **Django REST Framework** for API management
- **Africa’s Talking** for SMS gateway (sandbox)
- **OpenID Connect Provider** for secure authentication

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/savannah_patient_order_service.git
cd patientordersystem
```

### 2. Install Dependencies

It is recommended to use a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

### 3. Set Up Environment Variables

Create a `.env` file in the project root with the following details:

```plaintext
# Django settings
SECRET_KEY=your_secret_key
DEBUG=True

# Database configuration
DATABASE_URL=postgres://user:password@localhost:5432/customer_order_db

# Africa's Talking API credentials
AFRICASTALKING_USERNAME=sandbox
AFRICASTALKING_API_KEY=your_africas_talking_api_key

# OpenID Connect provider settings
OIDC_CLIENT_ID=your_client_id
OIDC_CLIENT_SECRET=your_client_secret
OIDC_AUTHORIZATION_URL=https://your-openid-provider.com/auth
OIDC_TOKEN_URL=https://your-openid-provider.com/token
OIDC_USERINFO_URL=https://your-openid-provider.com/userinfo
```

### 4. Apply Database Migrations

```bash
python manage.py migrate
```

### 5. Run the Development Server

```bash
python manage.py runserver
```

The service will now be accessible at `http://127.0.0.1:8000`.

## Usage

### Adding a Customer

You can add a customer through the `/api/customers/add/` endpoint by sending a POST request with JSON data, for example:

```json
{
  "name": "James Bond",
  "code": "CUST007",
  "contact_number": "+25470007007",
  "email": "JamesBond@gmail.com",
  "insurance_number": "INS123456789"
}
```

### Placing an Order

You can add an order through the `/api/orders/add/` endpoint. This action triggers an SMS notification to the customer.

```json
{
  "customer_code": "CUST001",
  "item": "Paracitamol",
  "amount": 50,
  "physician_name":"drhouse"
}
```
## Database Schema

- **Customer**: Stores customer details with fields `name` and `code`, `contact_number`, `email`, `insurance_number`.
- **Order**: Stores order details with fields `customer_code`, `item`, `amount`, and `physician_name`.

## API Endpoints

| Endpoint                   | Method | Description                        |
|----------------------------|--------|------------------------------------|
| `/api/customers/`          | GET    | List all customers                |
| `/api/customers/add/`      | POST   | Add a new customer                |
| `/api/orders/`             | GET    | List all orders                   |
| `/api/orders/add/`         | POST   | Place a new order and send SMS    |

## Authentication and Authorization

The API uses OpenID Connect for secure authentication. To access protected endpoints, users must authenticate via an OpenID Connect provider and obtain an access token. Include this token in the `Authorization` header of your requests:

```plaintext
Authorization: Bearer <access_token>
```
For testing, you can sign into the deployed application, https://savannah-patient-order-service.onrender.com/ and use djangos DRF interface, it will automatically store the access token to the browser allowing you to access permission protected views, including add customer and add order views. The list customer and list order views have been left unprotected for testing.

## SMS Notification

This service uses Africa’s Talking SMS gateway to send a notification to customers upon order creation. Once an order is successfully created, the customer receives an SMS with order details. (For some reason numbers i've tested with seem to have blacklisted Afircastalking from sending messages) Below are sample images from testing with Africa’s Talking sandbox simulator, showcasing message reception:

![Order entry post request sent](patientordersystem/static/images/post_request.png)

![Sandbox Simulator Message Log](patientordersystem/static/images/sms_received.png)

## Testing

### Running Unit Tests

Unit tests are implemented for core functionality, including customer and order creation. To run tests and check code coverage:

```bash
pip install coverage
coverage run manage.py test
coverage report
```

### CI/CD

Continuous Integration (CI) and Continuous Deployment (CD) are set up using GitHub Actions. Every push triggers automated tests, and successful tests trigger deployment to the configured Platform-as-a-Service (PAAS).

## Deployment

The application can be deployed to Render, Heroku, or any PAAS of your choice. Below is an example of deploying to Render:

1. Create a new web service on Render.
2. Set up environment variables as configured in the `.env` file.
3. Set up your database service and add database_url to settings.py file.
4. Trigger a deployment using Render's GitHub integration or CLI.
5. Add the url to list of allowed hosts on settings.py and on AuthO's application interface.

## Contributing
Peter Klaus Orioki - Backend Software Engineer

Contributions are welcome! Please fork the repository and submit a pull request for review.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

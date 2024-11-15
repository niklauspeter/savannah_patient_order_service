"""
URL configuration for patientordersystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from orders.views import AddCustomerView, ListCustomersView, AddOrderView, ListOrderView, login, callback, logout

urlpatterns = [
    path('admin/', admin.site.urls),

    path('oidc/login/', login, name='login'),
    path('oidc/callback/', callback, name='callback'),
    path('oidc/logout/', logout, name='logout'),

    path('api/customers/add/', AddCustomerView.as_view(), name='add-customer'),
    path('api/customers/list', ListCustomersView.as_view(), name='list_customers'),
    path('api/orders/add', AddOrderView.as_view(), name='add-orders'),
    path('api/orders/list', ListOrderView.as_view(), name='list-orders'),
    # path("oidc/", include("mozilla_django_oidc.urls")),
]

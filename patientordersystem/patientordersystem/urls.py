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
# from orders.views import AddCustomerView, ListCustomersView, AddOrderView, ListOrderView, login, callback, logout, register, login_view, logout_view
# from orders.views import AddCustomerView, ListCustomersView, AddOrderView, ListOrderView
from orders.views import HomeView, AuthenticatedHomeView, logout_view, AddCustomerView, ListCustomersView, AddOrderView, ListOrderView
# from users.views import register, login_view, logout_view
from mozilla_django_oidc import views as oidc_views
from orders.views import logout, sendtrialmessage

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     # path('oidc/v1/login/', login, name='login'),
#     # path('oidc/v1/callback/', callback, name='callback'),
#     path('oidc/logout/', logout, name='logout'),

#     path('oidc/login/', oidc_views.OIDCAuthenticationRequestView.as_view(), name='oidc_login'),
#     path('oidc/callback/', oidc_views.OIDCAuthenticationCallbackView.as_view(), name='oidc_authentication_callback'),
#     path('oidc/vi/logout/', oidc_views.OIDCLogoutView.as_view(), name='oidc_logout'),

#     path('trial/', sendtrialmessage, name='trial-message'),
#     path('api/customers/add/', AddCustomerView.as_view(), name='add-customer'),
#     path('api/customers/list/', ListCustomersView.as_view(), name='list_customers'),
#     path('api/orders/add/', AddOrderView.as_view(), name='add-orders'),
#     path('api/orders/list/', ListOrderView.as_view(), name='list-orders'),
#     # path("oidc/", include("mozilla_django_oidc.urls")),
# ]
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('authenticated/', AuthenticatedHomeView.as_view(), name='authenticated_home'),
    path('oidc/login/', oidc_views.OIDCAuthenticationRequestView.as_view(), name='oidc_login'),
    path('oidc/callback/', oidc_views.OIDCAuthenticationCallbackView.as_view(), name='oidc_authentication_callback'),
    path('oidc/vi/logout/', logout_view, name='logout'),
    path('oidc/logout/', logout, name='oidc_logout'),
    path('api/customers/add/', AddCustomerView.as_view(), name='add-customer'),
    path('api/customers/list/', ListCustomersView.as_view(), name='list_customers'),
    path('api/orders/add/', AddOrderView.as_view(), name='add-orders'),
    path('api/orders/list/', ListOrderView.as_view(), name='list-orders'),
]
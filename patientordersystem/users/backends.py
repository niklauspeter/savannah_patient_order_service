# from mozilla_django_oidc.auth import OIDCAuthenticationBackend
# from django.contrib.auth import get_user_model

# User = get_user_model()  # To support custom user models

# class CustomOIDCAuthenticationBackend(OIDCAuthenticationBackend):
#     def get_or_create_user(self, access_token, id_token, payload):
#         """
#         Override get_or_create_user to control the user creation process and avoid passing email twice.
#         """
#         claims = self.get_userinfo(access_token, id_token, payload)
#         email = claims.get("email")
#         if email is None:
#             raise ValueError("Email claim is required")

#         # Try to get the user by email
#         user, created = User.objects.get_or_create(email=email, defaults={
#             'first_name': claims.get("given_name", ""),
#             'last_name': claims.get("family_name", "")
#         })
#         return user

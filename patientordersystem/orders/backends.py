from mozilla_django_oidc.auth import OIDCAuthenticationBackend
from django.contrib.auth.models import User

class CustomOIDCAuthenticationBackend(OIDCAuthenticationBackend):

    def create_user(self, claims):
        """Create a new user given the OpenID Connect claims."""
        user = User.objects.create_user(
            username=claims.get("nickname", claims["sub"]),
            email=claims.get("email"),
        )
        user.save()
        return user
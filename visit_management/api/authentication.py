from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from rest_framework.authentication import TokenAuthentication
from rest_framework import exceptions


class PhoneAuthentication(TokenAuthentication):
    keyword = "Phone"

    def authenticate_credentials(self, key):
        model = get_user_model()
        try:
            user = model.objects.get(phone_number=key)
        except model.DoesNotExist:
            raise exceptions.AuthenticationFailed(_("Invalid token."))

        if not user.is_active:
            raise exceptions.AuthenticationFailed(
                _("User inactive or deleted.")
            )

        return user, None

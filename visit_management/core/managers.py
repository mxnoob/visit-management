from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import UserManager


class WorkerManager(UserManager):
    def _create_user(self, phone_number, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not phone_number:
            raise ValueError("The given phone number must be set")
        email = self.normalize_email(email)
        user = self.model(
            phone_number=phone_number, email=email, **extra_fields
        )
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(
        self, phone_number, email=None, password=None, **extra_fields
    ):
        super().create_user(phone_number, email, password, **extra_fields)

    def create_superuser(
        self, phone_number, email=None, password=None, **extra_fields
    ):
        super().create_superuser(phone_number, email, password, **extra_fields)

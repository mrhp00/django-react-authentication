from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    # Any extra fields would go here
    # فبلد ها اضافی را اینجا تعریف کنید
    def __str__(self):
        return self.email
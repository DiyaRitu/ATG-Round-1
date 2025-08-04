# models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

# Extending Django’s built-in AbstractUser model to add custom fields
class CustomUser(AbstractUser):
    # User type selection for conditional dashboard logic
    USER_TYPE_CHOICES = (
        ('doctor', 'Doctor'),
        ('patient', 'Patient')
    )
    user_type = models.CharField(
        max_length=10,
        choices=USER_TYPE_CHOICES,
        help_text="Select whether the user is a Doctor or Patient"
    )

    # Profile picture upload — stored in MEDIA_ROOT/profiles/
    profile_picture = models.ImageField(
        upload_to='profiles/',
        null=True,
        blank=True,
        help_text="Optional. Upload a square profile image."
    )

    # Address-related fields
    address_line1 = models.CharField(max_length=255, help_text="Street address or building info")
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)

    def __str__(self):
        # Display username with user type
        return f"{self.username} ({self.user_type})"

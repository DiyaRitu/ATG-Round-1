# forms.py

from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm

# Custom signup form extending Django's built-in UserCreationForm
class CustomUserForm(UserCreationForm):
    # Customizing password fields with Tailwind classes
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'w-full px-3 py-2 border border-gray-300 rounded-md',
            'placeholder': 'Enter Password'
        }),
        label="Password"
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'w-full px-3 py-2 border border-gray-300 rounded-md',
            'placeholder': 'Confirm Password'
        }),
        label="Confirm Password"
    )

    class Meta:
        model = CustomUser  # Custom user model defined in models.py

        # Fields to display on the signup form
        fields = [
            'first_name', 'last_name', 'username', 'email',
            'profile_picture', 'user_type', 'address_line1',
            'city', 'state', 'pincode'
        ]

        labels = {
    'first_name': 'First Name',
    'last_name': 'Last Name',
    'address_line1': 'Address',
    'user_type': 'Registering As',
        }


        # Apply consistent styling using Tailwind CSS to each input field
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md',
                'placeholder': 'First Name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md',
                'placeholder': 'Last Name'
            }),
            'username': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md',
                'placeholder': 'Username'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md',
                'placeholder': 'Email Address'
            }),
            'profile_picture': forms.ClearableFileInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md'
            }),
            'user_type': forms.Select(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md'
            }),
            'address_line1': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md',
                'placeholder': 'Address Line 1'
            }),
            'city': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md',
                'placeholder': 'City'
            }),
            'state': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md',
                'placeholder': 'State'
            }),
            'pincode': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md',
                'placeholder': 'Pincode'
            }),
        }

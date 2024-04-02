# In accounts/models.py
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Add any custom fields or methods here
    pass

# Specify unique related_name arguments for 'groups' and 'user_permissions' fields
CustomUser._meta.get_field('groups').related_name = 'accounts_customuser_groups'
CustomUser._meta.get_field('user_permissions').related_name = 'accounts_customuser_permissions'

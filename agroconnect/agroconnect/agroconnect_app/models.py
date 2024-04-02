from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    visitor_type = models.CharField(max_length=20)

    # Specify unique related names for groups and user_permissions
    groups = models.ManyToManyField('auth.Group', related_name='custom_user_groups', related_query_name='custom_user')
    user_permissions = models.ManyToManyField('auth.Permission', related_name='custom_user_permissions', related_query_name='custom_user')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'visitor_type']

    def get_by_natural_key(self, username):
        return self.get(username=username)

    def has_perm(self, perm, obj=None):
        # Your permission logic here
        return True

    def has_module_perms(self, app_label):
        # Your module-level permission logic here
        return True

    @property
    def is_authenticated(self):
        return True
    
    @property
    def is_anonymous(self):
        return False

    def __str__(self):
        return self.username

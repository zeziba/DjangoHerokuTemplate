from django.contrib.auth.models import AbstractUser, UserManager, User, PermissionsMixin
from django.db import models

class AccountManager(UserManager):
    def create_user(self, username, email, password=None, **kwargs) -> User:
        account = super(AccountManager, self).create_user(username=email, email=email, password=password, **kwargs)

        return account

    def create_superuser(self, username, email, password, **kwargs) -> User:
        account = super(AccountManager, self).create_superuser(username=email, email=email, password=password, **kwargs)

        return account

class Account(AbstractUser, PermissionsMixin):
    display_name = models.CharField(max_length=50, blank=True)
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        
    objects: UserManager = AccountManager()

    def __str__(self) -> str:
        return f"{self.display_name}"
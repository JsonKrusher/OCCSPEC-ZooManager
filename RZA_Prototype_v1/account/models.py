from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class AccountManager(BaseUserManager):
    def create_user(self, full_name, email, password=None):
        if not full_name or not email:
            raise ValueError('No full name or email was provided!')
        
        email = self.normalize_email(email)
        
        customer = self.model(
            full_name=full_name,
            email=email
        )
        customer.set_password(password)
        
        customer.save(using=self._db)
        
        return customer
    
    def create_superuser(self, full_name, email, password=None):
        if not full_name or not email:
            raise ValueError('No full name or email was provided!')
        
        email = self.normalize_email(email)
        
        admin = self.model(
            full_name=full_name,
            email=email,
            is_staff=True,
            is_admin=True
        )
        admin.set_password(password)
        
        admin.save(using=self._db)
        
        return admin


class Account(AbstractBaseUser):
    user_id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=64)
    email = models.EmailField(unique=True)
    last_login = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    def has_module_perms(self, perm, obj=None):
        return self.is_staff
    
    def has_perm(self, perm):
        return self.is_admin

    def __str__(self) -> str:
        return f"{self.user_id} | {self.email} | Admin Status: {self.is_admin} | Last Login = {self.last_login}"

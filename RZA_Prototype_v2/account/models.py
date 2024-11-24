from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class AccountManager(BaseUserManager):
    def create_user(self, full_name, email, password=None):
        # Check if full name or email was provided
        if not full_name or not email:
            # Return error as these are requried
            raise ValueError('No full name or email was provided!')
        
        # Lowercase the domain of the email
        email = self.normalize_email(email)
        
        # Setup new customer Model
        customer = self.model(
            full_name=full_name,
            email=email
        )
        # Set the password for the new Customer Model
        customer.set_password(password)
        
        # Save the new Customer Model
        customer.save(using=self._db)
        
        # Return the new Customer to server
        return customer
    
    def create_superuser(self, full_name, email, password=None):
        # Check if full name or email was provided
        if not full_name or not email:
            # Return error as these are requried
            raise ValueError('No full name or email was provided!')
        
        # Lowercase the domain of the email
        email = self.normalize_email(email)
        
        # Setup new customer Model
        admin = self.model(
            full_name=full_name,
            email=email,
            is_staff=True,
            is_admin=True
        )
        # Set the password for the new Admin Model
        admin.set_password(password)
        
        # Save the new Admin Model
        admin.save(using=self._db)
        
        # Return the new Admin to server
        return admin


class Account(AbstractBaseUser):
    # Generate a unique user_id
    user_id = models.AutoField(primary_key=True)
    # Users full name
    full_name = models.CharField(max_length=64)
    # Users email
    email = models.EmailField(unique=True)
    # When the account last login was
    last_login = models.DateTimeField(auto_now=True)
    # Is the account active
    is_active = models.BooleanField(default=True)
    # Is staff/admin depends on permissions given
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    # Use the Custom AccountManager to handle user creation
    objects = AccountManager()

    # The user should sign-in with email
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    def has_module_perms(self, perm, obj=None):
        return self.is_staff
    
    def has_perm(self, perm):
        return self.is_admin

    def __str__(self) -> str:
        return f"{self.user_id} | {self.email} | Admin Status: {self.is_admin} | Last Login = {self.last_login}"

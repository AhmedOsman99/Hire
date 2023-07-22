from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# Create your models here.

class UserManager(BaseUserManager):
    
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, password= None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_jioned = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True)
    
    objects = UserManager()

    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = []

    def __str__(self) -> str:
        return self.email


class JobSeeker(models.Model):
    # user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="job_seeker")
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="job_seeker")
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=20)
    birth_date = models.DateField()
    title = models.CharField(max_length=200)
    bio = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=20)
    user_type = models.CharField(default="job_seeker" , max_length=255)


class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="company")
    company_name = models.CharField(max_length=200)
    industry = models.CharField(max_length=255)
    about = models.TextField()
    phone = models.CharField(max_length=20)
    user_type = models.CharField(default="company" , max_length=255)

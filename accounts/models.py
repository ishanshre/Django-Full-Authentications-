from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django_extensions.db.fields import AutoSlugField
from django.utils.translation import gettext_lazy as _

# Create your models here.


class User(AbstractUser):
    class Gender(models.TextChoices):
        MALE = "MALE", 'MALE'
        FEMALE = "FEMALE", 'FEMALE'
        OTHERS = "OTHERS", 'OTHERS'
    date_of_birth = models.DateField(default=timezone.now)
    gender = models.CharField(max_length=10, choices=Gender.choices, blank=True, null=True)
    slug = AutoSlugField(_('slug'), max_length=50, unique=True, populate_from=('username','last_name'))

    def __str__(self):
        return self.username



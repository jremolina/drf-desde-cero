from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
  email = models.EmailField(unique= True) # establecer el correo electrónico como único
  web_site = models.URLField(max_length=200, blank=True)
  # pass

  USERNAME_FIELD = 'email' # establecer el correo electrónico como el campo de nombre de usuario para iniciar sesión
  REQUIRED_FIELDS = [] # establecer el campo de nombre de usuario como obligatorio al crear un nuevo usuario


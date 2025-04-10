from django.db import models
from django.contrib.auth.models import User

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    middle_name = models.CharField(max_length=100, verbose_name='Отчество', default='')
    phone = models.CharField(max_length=20, blank=True, verbose_name='Телефон')
    
    def __str__(self):
        return f"{self.user.last_name} {self.user.first_name} {self.middle_name}" 
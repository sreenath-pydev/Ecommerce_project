from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class customers(models.Model):
    LIVE = 1
    DELETE = 0
    DELETE_CHOICE = ((LIVE,'Live'),(DELETE,'Delete'))
    name = models.CharField(max_length=200)
    address = models.TextField()
    user =models.OneToOneField(User,on_delete=models.CASCADE,related_name='related_user')
    phone = models.CharField(max_length=10)
    delete_status = models.DateTimeField(auto_now_add=True)
    update_status = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

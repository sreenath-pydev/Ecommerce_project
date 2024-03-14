from django.db import models

# Create your models here.
class products(models.Model):
    LIVE = 1
    DELETE = 0
    DELETE_CHOICE = ((LIVE,'Live'),(DELETE,'Delete'))
    title = models.CharField(max_length=200)
    price = models.FloatField()
    descriptions = models.TextField()
    image = models.ImageField(upload_to='media/')
    priority = models.IntegerField(default=0)
    delete_status = models.IntegerField(choices=DELETE_CHOICE,default=LIVE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
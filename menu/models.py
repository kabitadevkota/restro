from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Menu(models.Model):
    CATEGORY = (("0", "Launch"),("1", "Deserts"),("2", "Drinks"),("3","Main Dishes"))
    name = models.CharField(max_length=50)
    description = models.TextField(verbose_name='description')
    category = models.CharField(choices=CATEGORY, max_length=2)
    price = models.IntegerField()
    cookname= models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    make_on= models.DateField(auto_now_add=True)
    updated_make= models.DateField(auto_now=True)
    cover_image = models.ImageField(upload_to='uploads')

    class Meta:
        verbose_name_plural = "Menus"

    def __str__(self):
        return self.name
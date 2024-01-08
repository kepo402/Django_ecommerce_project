from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
class Order(models.Model):
    orderitems = models.ManyToManyField(Cart)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.get_username()

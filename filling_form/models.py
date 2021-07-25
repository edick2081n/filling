from django.db import models

class Form(models.Model):
    user_name = models.CharField("название", max_length=50)
    user_phone = models.CharField("телефон", max_length=50)
    user_email = models.CharField("адрес", max_length=50)
    order_date = models.DateField("дата")
    description = models.TextField("описание")


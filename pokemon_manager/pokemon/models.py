from django.db import models

class Trainer(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=10) #とりあえず10文字
    password = models.CharField(max_length=50) #どのくらい必要かわからないのでとりあえず50
    user_id = models.EmailField(max_length=254) # とりあえずマックスの長さ

    class Meta:
        ordering = ['created']
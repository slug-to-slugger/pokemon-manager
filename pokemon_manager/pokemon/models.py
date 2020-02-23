from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Trainer(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=10)  # とりあえず10文字
    password = models.CharField(max_length=50)  # どのくらい必要かわからないのでとりあえず50
    user_id = models.EmailField(max_length=254)  # とりあえずマックスの長さ

    class Meta:
        ordering = ['created']


class Partner(models.Model):
    GENDER_CHOICES = (
        (1, 'オス'),
        (2, 'メス'),
        (3, 'その他'),
    )

    name = models.CharField(max_length=10)  # とりあえず10文字
    special_skill = models.CharField(max_length=255)  # とりあえず255文字
    gender = models.IntegerField(choices=GENDER_CHOICES, blank=False, null=False, default=1)
    # 努力値
    h = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(252)], blank=False, null=False, default=0)
    a = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(252)], blank=False, null=False, default=0)
    b = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(252)], blank=False, null=False, default=0)
    c = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(252)], blank=False, null=False, default=0)
    d = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(252)], blank=False, null=False, default=0)
    s = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(252)], blank=False, null=False, default=0)
    pokemon_id = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(890)], blank=False, null=False, default=1)
    # user_info = models.
    created_at = models.DateTimeField(auto_now_add=True)  # レコードが追加された時にその時間を保存します
    updated_at = models.DateTimeField(auto_now=True)  # レコードが更新されたタイミングで現在時間が保存されます。

    class Meta:
        ordering = ['created_at']

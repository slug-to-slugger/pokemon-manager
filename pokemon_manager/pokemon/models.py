from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from rest_framework.authtoken.models import Token


class Trainer(AbstractBaseUser, PermissionsMixin):

    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        max_length=255,
        unique=True,
        default='',
        validators=[username_validator],
        error_messages={
            'unique': ("A user with that username already exists."),
        },
    )
    login_id = models.EmailField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    EMAIL_FIELD = 'login_id'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['login_id']

    class Meta:
        ordering = ['created']

    def clean(self):
        super().clean()
        self.login_id = self.__class__.objects.normalize_email(self.login_id)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Pokemon(models.Model):
    guide_num = models.CharField(max_length=255, null=False)
    name = models.CharField(max_length=255, null=False)
    type1 = models.CharField(max_length=255, null=True, default='')
    type2 = models.CharField(max_length=255, null=True, default='')
    ability1 = models.CharField(max_length=255, null=True, default='')
    ability2 = models.CharField(max_length=255, null=True, default='')
    hidden_ability = models.CharField(max_length=255, null=True, default='')
    hp = models.IntegerField(null=False)
    attack = models.IntegerField(null=False)
    defence = models.IntegerField(null=False)
    special_attack = models.IntegerField(null=False)
    special_defence = models.IntegerField(null=False)
    speed = models.IntegerField(null=False)
    total = models.IntegerField(null=False)


class Partner(models.Model):
    GENDER_CHOICES = (
        (1, 'オス'),
        (2, 'メス'),
        (3, 'その他'),
    )

    name = models.CharField(max_length=10)  # とりあえず10文字
    # 特性
    ability = models.CharField(max_length=255)  # とりあえず255文字
    # 性格
    character = models.CharField(max_length=255)
    # 性別
    gender = models.IntegerField(choices=GENDER_CHOICES, blank=False, null=False, default=1)
    # 努力値
    h = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(252)], blank=False, null=False, default=0)
    a = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(252)], blank=False, null=False, default=0)
    b = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(252)], blank=False, null=False, default=0)
    c = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(252)], blank=False, null=False, default=0)
    d = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(252)], blank=False, null=False, default=0)
    s = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(252)], blank=False, null=False, default=0)
    created_at = models.DateTimeField(auto_now_add=True)  # レコードが追加された時にその時間を保存します
    updated_at = models.DateTimeField(auto_now=True)  # レコードが更新されたタイミングで現在時間が保存されます。

    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, related_name="Partners", null=True)
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)

    class Meta:
        ordering = ['created_at']

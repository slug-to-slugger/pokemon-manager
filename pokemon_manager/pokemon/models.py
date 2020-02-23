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


class Partner(models.Model):
    GENDER_CHOICES = (
        (1, 'オス'),
        (2, 'メス'),
        (3, 'その他'),
    )

    ATTRIBUTE_CHOICES = (
        (0, "なし"),
        (1, 'ノーマル'),
        (2, '炎'),
        (3, '水'),
        (4, '電'),
        (5, '草'),
        (6, '氷'),
        (7, '格'),
        (8, '毒'),
        (9, '地'),
        (10, '飛'),
        (11, '超'),
        (12, '虫'),
        (13, '岩'),
        (14, '霊'),
        (15, '竜'),
        (16, '悪'),
        (17, '鋼'),
        (18, '妖'),
    )

    name = models.CharField(max_length=10)  # とりあえず10文字
    special_skill = models.CharField(max_length=255)  # とりあえず255文字
    gender = models.IntegerField(choices=GENDER_CHOICES, blank=False, null=False, default=1)
    # 属性
    attribute1 = models.IntegerField(choices=ATTRIBUTE_CHOICES, blank=False, null=False, default=1)
    attribute2 = models.IntegerField(choices=ATTRIBUTE_CHOICES, blank=True, null=True, default=0)  # attribute1と重複しないようにvali
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

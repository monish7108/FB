import re
from django.db import models
from django.core import validators
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import UserManager



class UserInfo(AbstractBaseUser, PermissionsMixin):
    class Meta:
        app_label = 'FB'
        db_table = "UserInfo"

    UID = models.AutoField(primary_key=True)
    username = models.CharField(_('username'), max_length=30, unique=True,
                                help_text=_('Required. 30 characters or fewer. Letters, numbers and '
                                            '@/./+/-/_ characters'),
                                validators=[
                                    validators.RegexValidator(re.compile('^[ \w.@+-]+$'),
                                                              _('Enter a valid username.'), 'invalid')
                                ])
    password = models.CharField(max_length=30)
    first_name = models.CharField(_('full name'), max_length=25, blank=True)
    last_name = models.CharField(_('short name'), max_length=25, blank=True)
    email = models.EmailField(_('email address'), max_length=100, unique=True, default="a@b.com")
    is_staff = models.BooleanField(_('staff status'), default=False,
                                   help_text=_('Designates whether the user can log into this admin '
                                               'site.'))
    is_active = models.BooleanField(_('active'), default=True,
                                    help_text=_('Designates whether this user should be treated as '
                                                'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def get_full_name(self):
        return self.first_name

    def get_short_name(self):
        return self.username

    def __str__(self):
        return self.username



class PostsByUser(models.Model):
    UID = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class FriendList(models.Model):
    user = models.ForeignKey(UserInfo, related_name="user" ,on_delete=models.CASCADE)
    friend = models.ForeignKey(UserInfo, related_name="friend", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)


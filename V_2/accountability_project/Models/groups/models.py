from django.db import models
from django.db.models.base import Model
from django.db.models.fields.related import ForeignKey
from Models.users.models import User
from simple_history.models import HistoricalRecords



class Post(models.Model):
    """ Model definitions for post table"""
    user_owner = ForeignKey(User,
                            on_delete=models.CASCADE,
                            null=False,
                            blank=False,
                            related_name='user')
    contents = models.TextField('contents', max_length=255, blank=False, null=False)
    images = models.ImageField(upload_to='assets/images/groups/',
                               blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Unicode representation of post table."""
        return f'{self.user_owner} {self.created_at} {self.updated_at}'



class Group(models.Model):
    """Model definition for groups Table."""

    user_owner = models.ForeignKey(User, default=1, on_delete=models.CASCADE, blank=False, null=False)
    group_name = models.CharField('group name', max_length=200, unique=True)
    theme = models.CharField('theme group', max_length=50)
    description = models.TextField('description', max_length=255, blank=True, null=True)
    post = models.ForeignKey(Post, on_delete = models.CASCADE, blank=True, null=True)
    users = models.ManyToManyField(User, related_name='users', blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    historical = HistoricalRecords()

    class Meta:
        """Meta definition for MODELNAME."""

        verbose_name = 'Group'
        verbose_name_plural = 'Groups'


    USERNAME_FIELD = 'group_name'
    REQUIRED_FIELDS = ['group_name', 'theme']

    def natural_key(self):
        return (self.group_name)

    def __str__(self):
        """Unicode representation of MODELNAME."""
        return f'{self.group_name} {self.theme} {self.created_at} {self.updated_at}'


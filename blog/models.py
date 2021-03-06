import re
from django.conf import settings
from django.db import models
from django.forms import ValidationError
# Create your models here.
def lnglat_validator(value):
    if not re.match(r'^(\d+\.?\d*),(\d+\.?\d*)$', value):
        raise ValidationError('Invalid LngLat Type')


class Post(models.Model):
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published'),
        ('w', 'Withdrawn'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=100, verbose_name='제목',
        help_text='포스팅의 제목을 입력해주세요. 최대 100자 내외.')
    tags = models.CharField(max_length=100, blank=True)
    content = models.TextField(verbose_name='내용')
    lnglat = models.CharField(max_length=50, blank=True,
        validators=[lnglat_validator],
        help_text='위도/경도 포맷으로 입력')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tag_set = models.ManyToManyField('Tag', blank=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post)
    author = models.CharField(max_length=20)
    messages = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)


    def __str__(self):
        return self.name

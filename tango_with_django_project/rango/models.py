from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', default="profile_images/default.png", blank=True)

    def __str__(self):
        return self.user.username


class Category(models.Model):
    NAME_MAX_LENGTH = 128
    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
        if self.views < 0:
            self.views = 0

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Page(models.Model):
    TITLE_MAX_LENGTH = 128
    URL_MAX_LENGTH = 200

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=TITLE_MAX_LENGTH)
    content = models.TextField(null=True)
    url = models.URLField()
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    is_show = models.BooleanField(default=1, choices=((0, 'Hide'), (1, 'Show')),
                                  help_text="This field will automatically switch to 'Hide' when you click to modify it, please pay attention to whether you want to modify it")
    image = models.ImageField(upload_to='page_images')
    time = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super(Page, self).save(*args, **kwargs)
        if self.content is None:
            self.content = 'you must type something'

    class Meta:
        verbose_name_plural = 'Pages'
        ordering = ["-time", ]

    def __str__(self):
        return self.title


class Commit(models.Model):
    COMMENT_MAX_LENGTH = 150

    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    comment = models.CharField(max_length=COMMENT_MAX_LENGTH)

    def __str__(self):
        return self.comment

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField


# Create your models here.
class BlogProfile(models.Model):
    name = models.CharField(max_length=50)
    carousel1 = models.ImageField(upload_to='carousel')
    carousel2 = models.ImageField(upload_to='carousel')
    carousel3 = models.ImageField(upload_to='carousel')
    carousel4 = models.ImageField(upload_to='carousel')

    def __str__(self):
        return str(self.name)

class Category(models.Model):
    category = models.CharField(max_length=50)
    slug = models.SlugField()

    def __str__(self):
        return str(self.category)



class Blog_Post(models.Model):
    writer = models.ForeignKey(User, on_delete = models.CASCADE, related_name='author')
    category = models.ForeignKey(Category, on_delete = models.CASCADE, related_name='author')
    image = models.ImageField(upload_to = 'img')
    title = models.CharField(max_length= 200)
    liked = models.ManyToManyField(User, default=None, blank=True, related_name='liked')
    body = models.TextField(blank=True, null=True)
    postbody = RichTextField()
    music = models.FileField(blank=True, null=True)
    slug = models.SlugField()
    trendsongs = models.BooleanField()
    mostviewed = models.BooleanField()
    featured = models.BooleanField()
    newpost = models.BooleanField()
    created_on = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.title)

    def save(self,*arg,**kwargs):
        self.slug = slugify(self.title)
        super(Blog_Post,self).save(arg,kwargs)

    def num_likes(self):
        return self.liked.all().count()


LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    post = models.ForeignKey(Blog_Post, on_delete = models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default='Like', max_length=10)

    def __str__(self):
        return str(self.post)


class Comment(models.Model):
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Blog_Post, on_delete = models.CASCADE, related_name='comments')
    body = models.TextField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.commenter.username


class Visitor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.user.username



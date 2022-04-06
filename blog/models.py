from django.db import models

from django.contrib.auth import get_user_model
from django.urls import reverse


# Create your models here.
class IPAddress(models.Model):
    ip_address = models.GenericIPAddressField(verbose_name='آدرس آی پی')

    def __str__(self):
        return self.ip_address


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('accounts.CustomeUser', on_delete=models.CASCADE)
    body = models.TextField()

    hits = models.ManyToManyField(IPAddress, blank=True,related_name='hits', verbose_name='بازدیدها')
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail-post', args=[str(self.id)])

class Comment(models.Model):
    comment = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.comment
    
    def get_absolute_url(self):
        return reverse('blog:detail-post', args=[str(self.id)])


class MyModel(models.Model):
    title = models.CharField(max_length=200)
    phone = models.IntegerField(null=True)
    
    def __str__(self):
        return self.title
    

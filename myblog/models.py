from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.html import strip_tags

import markdown



class Category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    #biaoti
    title=models.CharField(max_length=70)

    #zhengwen
    body=models.TextField()

    #chuangjian he xiugai shijian
    created_time=models.DateTimeField()
    modified_time=models.DateTimeField()

    #zhaiyao
    excerpt=models.CharField(max_length=200,blank=True)

    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    tags=models.ManyToManyField(Tag,blank=True)

    author=models.ForeignKey(User,on_delete=models.CASCADE)

    views=models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('myblog:detail',kwargs={'pk':self.pk})

    def increase_views(self):
        self.views+=1
        self.save(update_fields=['views'])

    def save(self,*args,**kwargs):
        if not self.excerpt:
            md=markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
                ])
            self.excerpt=strip_tags(md.convert(self.body)[:54])
        super(Post,self).save(*args,**kwargs)

    class Meta:
        ordering=['-created_time']


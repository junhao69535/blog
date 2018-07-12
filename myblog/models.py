from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.html import strip_tags
from DjangoUeditor.models import UEditorField
import markdown



class Category(models.Model):
    name=models.CharField(u"分类",max_length=100)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name=models.CharField(u"标签",max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    #biaoti
    title=models.CharField(u"标题",max_length=70)

    #zhengwen
    body=UEditorField(u"文章正文",height=300,width=1000,default=u'',blank=True,imagePath="uploads/myblog/images/",toolbars='besttome',filePath='uploads/myblog/files/')

    #chuangjian he xiugai shijian
    created_time=models.DateTimeField(u"创建时间")
    modified_time=models.DateTimeField(u"修改时间")

    #zhaiyao
    excerpt=models.CharField(u"摘要",max_length=200,blank=True)

    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    tags=models.ManyToManyField(Tag,blank=True)

    author=models.ForeignKey(User,on_delete=models.CASCADE)

    views=models.PositiveIntegerField(u"阅读数",default=0)

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


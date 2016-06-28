from django.db import models

# Create your models here.

class Tag(models.Model):
    tag_name = models.CharField(max_length=64)

    def __str__(self):
        return self.tag_name
    
class Article(models.Model):
    title = models.CharField(max_length = 100)  #博客题目
    category = models.CharField(max_length = 50, blank = True)  #博客标签
    create_time = models.DateTimeField(auto_now_add = True)  #博客日期
    tag = models.ManyToManyField(Tag, blank=True)  # 博客标签 可为空
    edit_time = models.DateTimeField(auto_now = True)#博客最近一次修改日期
    content = models.TextField(blank = True, null = True)  #博客文章正文
    hidden = models.BooleanField(blank = True)#博客存在状态
    article_author = models.CharField(default='whx',max_length=128)

    #python2使用__unicode__, python3使用__str__
    def __str__(self) :
        return self.title

    class Meta:  #按时间下降排序
        ordering = ['-create_time']
        

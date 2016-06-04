from django.db import models

# Create your models here.
class Tag(models.Model):
    title = models.CharField(max_length=30)

    def __unicode__(self):
        return self.title


class Question(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    tags = models.ManyToManyField(Tag, related_name='questions')
    sf_id = models.CharField(max_length=16, default='0') #　加上这个可以记住问题在sf的位置，方便以后更新或者其他操作
    update_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title


class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers')
    content = models.TextField()

    def __unicode__(self):
        return 'To question %s' % self.question.title
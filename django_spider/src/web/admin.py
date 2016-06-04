from django.contrib import admin

# Register your models here.
from web.models import Tag, Question, Answer

admin.site.register(Tag)
admin.site.register(Question)
admin.site.register(Answer)
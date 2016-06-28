from django import forms
from django.contrib import admin
from pagedown.widgets import AdminPagedownWidget

from blog.models import Article, Tag


# Register your models here.
class ArticleForm(forms.ModelForm):
    content = forms.CharField(widget=AdminPagedownWidget())
    #注意此处的content就是markdown编辑器所在，但不会保存数据，只供预览
    class Meta:
        model = Article
        fields = '__all__'


class ArticleAdmin(admin.ModelAdmin):
    # 管理后台显示字段
    list_display=['title','category','create_time','edit_time','article_author','hidden']
    # 使用ArticleForm 预览 markdown 编辑文字效果
    form = ArticleForm
    # 搜索字段
    search_fields = ('title','category','article_author',)
    # 列式选择过滤
    list_filter = ('edit_time','article_author','category',)
    
    def save_model(self, request, obj, form, change):
        admin.ModelAdmin.save_model(self, request, obj, form, change)

admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag)


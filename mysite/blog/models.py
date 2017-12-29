from django.db import models
from django.contrib.contenttypes.models import ContentType

# Create your models here.
class Artical(models.Model):
    title = models.CharField("标题", max_length=200)
    author = models.CharField("作者", max_length=50)
    pub_date = models.DateTimeField("创建时间", auto_now_add=True)
    mod_date = models.DateTimeField("修改时间", auto_now=True)
    content = models.TextField("内容")
    is_show = models.BooleanField("是否可见", default=False)

    favorite = models.IntegerField("收藏", default=0)
    thumbsup = models.IntegerField("支持", default=0)
    thumbsdown = models.IntegerField("不支持", default=0)
    
    class Meta:
        db_table = "artical"

    def __str__(self):
        return self.title

class NewFavorite(models.Model):
    object_id = models.IntegerField()
    content_type = models.ForeignKey(ContentType)
    author = models.CharField(max_length=50, default="wato")
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "new_favorite"

    def __str__(self):
        #return self.content_type.name + " " + self.content_type.model + " " + self.object_id
        return self.content_type.model

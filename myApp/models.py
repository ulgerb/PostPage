from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(("Başlık"), max_length=100)
    text_info = models.TextField(("Post açıklaması"), max_length=200)
    text = models.TextField(("Post Yazısı"))
    date = models.DateTimeField(("Paylaşım Tarihi"),  auto_now_add=True)
    yazar = models.CharField(verbose_name = 'Yazar adı', max_length=100)
    image = models.FileField(upload_to='')
    
    def __str__(self): # burası adminde gözükücek panel adı
        show = 'Başlık: '+ self.title
        show += ', Yazar: ' + self.yazar
        return show


class Comment(models.Model):
    post = models.ForeignKey("myApp.Post", verbose_name=("Post"), on_delete=models.CASCADE, related_name = 'comments')
    name = models.CharField(("Ad"), max_length=50)
    text = models.TextField(("Yorum"))
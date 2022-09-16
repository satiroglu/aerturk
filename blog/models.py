from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from tinymce import models as tinymce_models


STATUS = (
    (0, "Taslak"),
    (1, "Yayınla")
)

COMMENT_STATUS = (
    (0, "Onay Bekliyor"),
    (1, "Onaylandı")
)

class Category(models.Model):
    # Category
    name = models.CharField(verbose_name="Kategori Adı", max_length=200, unique=True)
    slug = models.SlugField(verbose_name="Slug", max_length=200, unique=True)
    description = models.TextField(verbose_name="Açıklama")

    # Other
    createdOn = models.DateTimeField(verbose_name="Oluşturulma Tarihi", auto_now_add=True)
    updatedOn = models.DateTimeField(verbose_name="Güncellenme Tarihi", auto_now=True)
    status = models.IntegerField(verbose_name="Durum", choices=STATUS, default=1)

    class Meta:
        ordering = ['-createdOn']
        verbose_name = 'Kategori'
        verbose_name_plural = 'Kategoriler'


    def __str__(self):
        return self.name


class Post(models.Model):
    # Post
    title = models.CharField(verbose_name="Başlık", max_length=200, unique=True)
    slug = models.SlugField(verbose_name="Slug", max_length=200, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Kategori")
    author = models.ForeignKey(User, on_delete= models.CASCADE, related_name="blog_posts", verbose_name="Yazar")
    content = tinymce_models.HTMLField(verbose_name="Yazı")

    # SEO
    seoTitle = models.CharField(verbose_name="SEO Başlık", max_length=200)
    seoKeywords = models.CharField(verbose_name="Anahtar Kelimeler", max_length=300)
    seoDescription = models.TextField(verbose_name="SEO Açıklama")

    # Other
    createdOn = models.DateTimeField(verbose_name="Oluşturulma Tarihi", auto_now_add=True)
    updatedOn = models.DateTimeField(verbose_name="Güncellenme Tarihi", auto_now=True)
    status = models.IntegerField(verbose_name="Durum", choices=STATUS, default=0)

    class Meta:
        ordering = ['-createdOn']
        verbose_name = 'Yazı'
        verbose_name_plural = 'Yazılar'

    def __str__(self):
        return self.title

class Comment(models.Model):
    # Post
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="Yazı")
    author = models.CharField(verbose_name="Yorum Yazan", max_length=200)
    email = models.CharField(verbose_name="Email", max_length=200)
    comment = models.TextField(verbose_name="Yorum")

    # Other
    createdOn = models.DateTimeField(verbose_name="Oluşturulma Tarihi", auto_now_add=True)
    updatedOn = models.DateTimeField(verbose_name="Güncellenme Tarihi",auto_now=True)
    status = models.IntegerField(verbose_name="Onay durumu", choices=COMMENT_STATUS, default=0)

    class Meta:
        ordering = ['-createdOn']
        verbose_name = 'Yorum'
        verbose_name_plural = 'Yorumlar'

    def __str__(self):
        return self.author


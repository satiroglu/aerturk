from django.db import models
from tinymce import models as tinymce_models


STATUS = (
    (0, "Taslak"),
    (1, "Yayınla")
)
MENU_LOCATION = (
    ('0', "Navbar"),
    ('1', "Footer")
)


class Page(models.Model):
    # Page
    title = models.CharField(verbose_name="Başlık", max_length=200, unique=True)
    slug = models.SlugField(verbose_name="Slug", max_length=200, unique=True)
    photo = models.ImageField(verbose_name="Fotoğraf", null=True, blank=True, upload_to='blog-images')
    location = models.CharField(verbose_name="Menü Konumu", max_length=1, choices=MENU_LOCATION, default='0')
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
        verbose_name = 'Sayfa'
        verbose_name_plural = 'Sayfalar'

    def __str__(self):
        return self.title
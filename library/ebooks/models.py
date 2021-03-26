import os
import uuid

from django.conf import settings
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models, IntegrityError
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

LANGUAGE_CHOICE = {
    ("O'zbek","O'zbek"),
    ('English','English'),
    ('Russian',"Russian"),
    ('Français',"Français"),
    ('Deutsche',"Deutsche"),
    ('Türkçe',"Türkçe"),
}

WATERMARK = "[library.uz]"

def pdf_path(instance, filename):
    ext = instance.pdf.url.split('.')[-1]
    path = f"ebooks/pdf/{instance.author}-{instance.title} {instance.publication_date} {WATERMARK}.{ext}"
    base_dir = f"{settings.BASE_DIR}{settings.MEDIA_URL}{path}"
    return path

def epub_path(instance, filename):
    ext = instance.pdf.url.split('.')[-1]
    path = f"ebooks/epub/{instance.author}-{instance.title} {instance.publication_date} {WATERMARK}.{ext}"
    base_dir = f"{settings.BASE_DIR}{settings.MEDIA_URL}{path}"
    return path

def djvu_path(instance, filename):
    ext = instance.pdf.url.split('.')[-1]
    path = f"ebooks/djvu/{instance.author}-{instance.title} {instance.publication_date} {WATERMARK}.{ext}"
    base_dir = f"{settings.BASE_DIR}{settings.MEDIA_URL}{path}"
    return path

def mobi_path(instance, filename):
    ext = instance.pdf.url.split('.')[-1]
    path = f"ebooks/mobi/{instance.author}-{instance.title} {instance.publication_date} {WATERMARK}.{ext}"
    base_dir = f"{settings.BASE_DIR}{settings.MEDIA_URL}{path}"
    return path

def doc_path(instance, filename):
    ext = instance.pdf.url.split('.')[-1]
    path = f"ebooks/doc/{instance.author}-{instance.title} {instance.publication_date} {WATERMARK}.{ext}"
    base_dir = f"{settings.BASE_DIR}{settings.MEDIA_URL}{path}"
    return path

class AbstractBook(models.Model):
    publisher = models.ForeignKey(User,on_delete=models.DO_NOTHING)

    author = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    language = models.CharField(max_length=10,choices=LANGUAGE_CHOICE,default='uz')

    cover_image = models.ImageField(upload_to="cover_images/")
    pages = models.PositiveSmallIntegerField(blank=True)
    isbn10 = models.CharField(max_length=10, blank=True)
    isbn13 = models.CharField(max_length=14, blank=True)
    publication_date = models.DateField(blank=True) 
    review = models.TextField(blank=True)

    slug = models.SlugField(max_length=255,unique=True,blank=True)
    added_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.author}: {self.title}"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.title}-{self.id}")
        super(AbstractBook, self).save(*args, **kwargs)


class Ebook(AbstractBook):
    pdf = models.FileField(upload_to=pdf_path, blank=True)
    djvu = models.FileField(upload_to=djvu_path, blank=True)
    epub = models.FileField(upload_to=epub_path, blank=True)
    mobi = models.FileField(upload_to=mobi_path, blank=True)
    doc = models.FileField(upload_to=doc_path, blank=True)

    def clean(self):
        if not (self.pdf or self.djvu or self.epub or self.mobi or self.doc):
            raise ValidationError(_('Ebook cannot be None! Please upload at least one'))
    class Meta:
        ordering = ('updated_at',)

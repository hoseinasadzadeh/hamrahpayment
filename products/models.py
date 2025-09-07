from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    parent = models.ForeignKey(
        'self', verbose_name=_('parent'), blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(_('title'), max_length=50)
    description = models.CharField(_('description'), blank=True)
    avatar = models.ImageField(
        _('avatar'), blank=True, upload_to='upload/category/')
    is_enable = models.BooleanField(_('enable'), default=True)
    created_time = models.DateTimeField(_('created time'), auto_now_add=True)
    updated_time = models.DateTimeField(_('updated time'), auto_now=True)

    class Meta:
        db_table = 'categories'
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


class Product(models.Model):
    title = models.CharField(_('title'), max_length=50)
    description = models.CharField(_('description'), blank=True)
    avatar = models.ImageField(
        _('avatar'), blank=True, upload_to='upload/product/')
    is_enable = models.BooleanField(_('enable'), default=True)
    Categories = models.ManyToManyField(
        Category, verbose_name=_('Categories'), blank=True)
    created_time = models.DateTimeField(_('created time'), auto_now_add=True)
    updated_time = models.DateTimeField(_('updated time'), auto_now=True)

    class Meta:
        db_table = 'products'
        verbose_name = _('Product')
        verbose_name_plural = _('Products')


class File(models.Model):
    product = models.ForeignKey(Product, verbose_name=_(
        'product'), on_delete=models.CASCADE)
    title = models.CharField(_('title'), max_length=50)
    file = models.FileField(_('file'), upload_to='upload/file/')
    description = models.CharField(_('description'), blank=True)
    avatar = models.ImageField(
        _('avatar'), blank=True, upload_to='upload/files/%Y/%m/%d/')
    is_enable = models.BooleanField(_('enable'), default=True)
    created_time = models.DateTimeField(_('created time'), auto_now_add=True)
    updated_time = models.DateTimeField(_('updated time'), auto_now=True)

    class Meta:
        db_table = 'files'
        verbose_name = _('File')
        verbose_name_plural = _('Files')

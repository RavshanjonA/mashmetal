from django.db.models import Model, CharField, DateTimeField, TextField, SlugField, DecimalField, \
    BooleanField
from django.utils.text import slugify

class BaseModel(Model):
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    description = TextField(null=True, blank=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    title = CharField(max_length=256)
    slug = SlugField(unique=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.title)
        super().save(force_insert, force_update, using, update_fields)

    class Meta:
        db_table = "category"
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Product(BaseModel):
    name = CharField("называния", max_length=128)
    size = CharField("размер", max_length=8)
    clen = SlugField("длина", max_length=256)
    nton = CharField("норма в тоннах", max_length=256)
    price = DecimalField(max_digits=15, decimal_places=2)
    is_active = BooleanField(default=True)
    is_discount = BooleanField(default=False)

    class Meta:
        db_table = "product"
        verbose_name = "Product"
        verbose_name_plural = "Products"

from django.db import models

class ProductQuerySet(models.query.QuerySet):
    def featured(self):
        return self.filter(featured=True, active=True)
    def active(self):
        return self.filter(active=True)
class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self.db)
    def get_by_id(self,id):
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None
    def all(self):
        return self.get_queryset().active()
    def featured(self):
        return self.get_queryset().featured()
class Product(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=5)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', null=True)
    featured = models.BooleanField(default=False)
    active = models.BooleanField(default = True)

    objects= ProductManager()

    def __str__(self):
        return self.title


from django.db import models

class product(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=5)

    def __str__(self):
        return self.title


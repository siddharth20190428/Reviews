from django.db import models

class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)
    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value': self.max_value}
        defaults.update(**kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)

# Create your models here.
class Product_Mobile(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50) 
    category = models.CharField(max_length=50, default="")
    brand = models.CharField(max_length=30)
    release_date = models.DateField()
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to="reviews/images", default="")
    description = models.CharField(max_length=1000)
    design = IntegerRangeField(min_value=1, max_value=10)
    camera = IntegerRangeField(min_value=1, max_value=10)
    battery = IntegerRangeField(min_value=1, max_value=10)
    performance = IntegerRangeField(min_value=1, max_value=10)
    value_for_money = IntegerRangeField(min_value=1, max_value=10)
    m_slug = models.CharField(max_length=120, default="mobile=")

    def __str__(self):
        return self.product_name
    
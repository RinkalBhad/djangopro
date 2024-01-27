from django.db import models

# Create your models here.
class Product_mst(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)

    def __str__(self):
        return self.product_name

class Product_sub_cat(models.Model):
    product = models.ForeignKey(Product_mst, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/')
    model = models.CharField(max_length=100)
    ram = models.CharField(max_length=50)

    def __str__(self):
        return self.product.product_name
import uuid
from django.db import models

# Create your models here.

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Name = models.CharField(max_length=100, unique=True)
    CostPerUnit =models.DecimalField(max_digits=100,decimal_places=2)
    Quantity = models.IntegerField()
    SellingPrice = models.DecimalField(max_digits=100,decimal_places=2)

    def __str__(self):
        return "<id={} name={}>".format(
            self.id, self.Name
        )

class Customer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Name = models.CharField(max_length=100)
    Email = models.EmailField()
    Address = models.CharField(max_length=100)
    ##TODO: modify the max_length of the phone nunber.
    PhoneNumber = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return "<id={} name={}>".format(
            self.id, self.Name
        )

class Supplier(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Name = models.CharField(max_length=100)
    Email = models.EmailField(max_length=70)
    Address = models.CharField(max_length=100)
    PhoneNumber = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return "<id={} name={}>".format(
            self.id, self.Name
        )

class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    DatePlaced  = models.DateTimeField(unique=True)
    Customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    def __str__(self):
        return "<id={} CustomerName={}>".format(
            self.id, self.Customer
        )

class PO(models.Model):
    class Meta:
        unique_together = (('Order', 'Product'),)
    Order = models.ForeignKey(Order, on_delete=models.PROTECT)
    Product = models.ForeignKey(Product, on_delete=models.PROTECT)
    Quantity = models.IntegerField()

    def __str__(self):
        return "<order={} product={}>".format(
            self.Order, self.Product
        )

class PS(models.Model):

    Product = models.ForeignKey(Product, on_delete=models.PROTECT)
    Supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT)
    DatePlaced = models.DateTimeField()
    Quantity = models.IntegerField()

    def __str__(self):
        return "<product={} supplier={}>".format(
            self.Product, self.Supplier
        )

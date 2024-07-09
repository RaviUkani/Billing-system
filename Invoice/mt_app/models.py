from django.db import models

class Customer(models.Model):
    costomer_name = models.CharField(max_length=20)
    costomer_address = models.CharField(max_length=20)
    costomer_phone = models.IntegerField()

    def __str__(self):
        return str(f"{self.costomer_name} + {self.costomer_address} + {self.costomer_phone}") 
    
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,null=True, blank=True)
    order_date = models.DateTimeField()

    def __str__(self):
        return str(f"{self.customer} + {self.order_date}")
    
class Item(models.Model):
    order = models.ForeignKey(Order,on_delete =models.CASCADE, null = True, blank=True)
    item_name = models.CharField(max_length=20)
    item_price = models.IntegerField()
    item_quantity = models.IntegerField()

    def __str__(self):
        return str(f"{self.order} + {self.item_name} + {self.item_price} + {self.item_quantity}")

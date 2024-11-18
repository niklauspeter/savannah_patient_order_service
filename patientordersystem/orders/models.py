from django.db import models

    
class Customer(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=50, unique=True)  # Unique customer identifier
    contact_number = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)
    insurance_number = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.code})"

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="orders")
    item = models.CharField(max_length=100)  
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    physician_name = models.CharField(max_length=100, blank=True, null=True)  
    

    def __str__(self):
        return f"Order {self.item} for {self.customer.name}"
    @property
    def customer_phone(self):
        return self.customer.contact_number

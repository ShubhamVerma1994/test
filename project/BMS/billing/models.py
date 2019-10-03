from django.db import models

# Create your models here.

_PAYMENT_CHOICES = [
    ('UPI', 'UPI Mode'),
    ('CASH', 'Cash Payment'),
    ('CARD', 'Card Payment') 

] # It takes a tuple of payment method. As we are starting with _  it is not supposed to be outside class , can be accessible only inside the class. Global variables

class Customer (models.Model):
	full_name= models.CharField(max_length = 50)
	email = models.EmailField()
	mobile = models.CharField(max_length=50)

	def __str__(self):
		return self.full_name


class Product(models.Model):
	product_id = models.AutoField(primary_key = True)
	name = models.CharField(max_length = 50)
	price = models.IntegerField()
	max_price = models.FloatField()
	quantity = models.IntegerField()
	updated = models.DateTimeField(auto_now = True)
	updated_quantity = models.IntegerField(default = 0)

	def __str__(self):
		return self.name

class Transaction(models.Model): #customer is foreign key

	customer_concerned = models.ForeignKey(Customer, on_delete = models.CASCADE) # linking this to customer table e.g. like starbazar ask mobile number to extract the data of the customer registered earlier

	products_selected = models.ManyToManyField(Product, through= 'TransactionProductMapper') # many to many where a customer can buy many number of products (but not quantity), cutomer can do many transactions (many to many)

	mode_of_payment = models.CharField(max_length = 50, choices = _PAYMENT_CHOICES) #create _PAYMENT_CHOICE outside class as global variables and declare choice = here
	
	def _calculate_total_fare(self):
		products = [ p['price'] for p in self.products_selected.values() ]
		return sum(products)

	total_amount = property(_calculate_total_fare)

	def __str__(self):
		return self.customer_concerned.full_name

class TransactionProductMapper(models.Model):
	product = models.ForeignKey(Product, on_delete = models.CASCADE)
	transaction = models.ForeignKey(Transaction, on_delete = models.CASCADE)
	quantity = models.IntegerField()

	# def __str__(self):
	# 	return self.product.name


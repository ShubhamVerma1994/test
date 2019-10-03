
from django.db import models
from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Transaction, Product, Customer 



@receiver(post_save, sender=Transaction)
def send_invoice(sender, instance, created, **kwargs):
	if created:
		#print(instance.products_selected)
		body_message= '''
		Thank for using Our service.
		here is the invoice of your last transations''' + 'And You paid through ' + instance.mode_of_payment
		send_mail('Invoice | Billing management System', body_message, 'admin@tfortime.site', [instance.customer_concerned.email])


@receiver(post_save, sender = Transaction.products_selected.through)
def updateInventory(sender, instance, created, **kwargs):
	if created:
		existing_quantity = instance.product.quantity
		purchased_quantity = instance.quantity
		new_quantity = existing_quantity - purchased_quantity
		Product.objects.filter(product_id = 
		instance.product.product_id).update(updated_quantity = 
	    new_quantity)



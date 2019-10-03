from django.contrib import admin
from .models import Customer, Product, Transaction, TransactionProductMapper

# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
	search_fields = ['full_name']
	list_display = ['id', 'full_name', 'email', 'mobile']

admin.site.register(Customer, CustomerAdmin)

class ProductAdmin(admin.ModelAdmin):
	date_hierarchy = 'updated'
	list_display = ['product_id', 'name', 'max_price', 'quantity', 'updated_quantity' ]

admin.site.register(Product, ProductAdmin)

class TransactionInline(admin.TabularInline):

	model = TransactionProductMapper
	extra = 2


class TransactionManager(admin.ModelAdmin):
	list_display = ['id', 'customer_concerned',
	'mode_of_payment']
	search_fields = ['mode_of_payment']
	list_filter = ['mode_of_payment']
	action_on_top = True
	inlines = [TransactionInline]
	exclude = ['products_selected']
	readonly_fields = ['total_amount']
	autocomplete_fields = ['customer_concerned']


admin.site.register(Transaction,TransactionManager)
admin.site.register(TransactionProductMapper)

admin.site.site_header = 'Billing Management System'

admin.site.index_title = 'BMS Administration'
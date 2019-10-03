from django.shortcuts import render
from .forms import CustomerForm
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
# Create your views here.


def addCustomer(request):
	if request.method=="POST":
		form = CustomerForm(request.POST or None)
		if form .is_valid():
			form.save()
		return HttpResponseRedirect('/billing')
	else:
		form = CustomerForm()
	return render(request, 'add-customer.html', {'form1':form})


def index(request):
	query = Article.objects.all()
	#query = ['e1', 'e2', 'e3']
	p = Paginator(query, 1) # 1 here is 1 element per page
	try:
		page_number = request.GET.get('page')
		page_object = p.page(page_number)
	except:
		page_object = p.page(1)
	return render(request, 'index.html', {'page_object': page_object()})


	
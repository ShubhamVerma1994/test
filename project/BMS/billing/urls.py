from django.conf.urls import url
from billing import views


urlpatterns = [
   url(r'^signup/', views.addCustomer)
]
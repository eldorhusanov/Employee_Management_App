from django.conf.urls import url

from . import views

app_name = 'emp'

urlpatterns = [
    url(r'^api/employees', views.employees_list_all, name='index'),
]
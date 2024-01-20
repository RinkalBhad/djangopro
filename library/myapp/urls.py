from django.contrib import admin
from django.urls import path,include
from myapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.index,name='index'),
    path("addbook/",views.addbook),
    path("edit/<int:id>",views.edit),
    path("delete/<int:id>",views.delete),
]

from . import views
from django.urls import include, path

# Wire up our API using automatic URL routing.

urlpatterns = [
    path('create_invoice/', views.create_invoice),
    path('get_invoice/<int:pk>', views.get_invoice),
    path('make_payment/<int:pk>', views.make_payment),
]
from django.urls import path

from .views import home, mavzular_list, themes_view, mavzular_update, mavzular_delete
urlpatterns = [
    path('yangilash/<int:pk>/', mavzular_update, name='yangilash'),
    path('ochirish/<int:pk>/', mavzular_delete, name='yangilash'),
    path('mavzular_list/', mavzular_list, name='mavzular'),
    path('qoshish/', themes_view, name='qoshish'),
    path('', home, name='home')
]


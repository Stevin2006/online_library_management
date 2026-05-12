from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='book_home'),
    path('add/',views.add_book,name='book_add'),
    path('edit/<int:book_id>/',views.update_book,name='book_edit'),
    path('delete/<int:book_id>/',views.delete_book,name='book_delete'),
]
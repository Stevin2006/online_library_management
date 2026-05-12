from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='lib_home'),
    path('lib_add/',views.add_barrow,name='lib_add'),
    path('lib_edit/<int:library_id>',views.edit_barrow,name='lib_edit'),
    path('lib_delete/<int:library_id>',views.delete_barrow,name='lib_delete'),
]
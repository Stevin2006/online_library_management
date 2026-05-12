from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='stud_home'),
    path('add_student/',views.add_student,name='stud_add'),
    path('edit_student/<int:student_id>',views.edit_student,name='stud_edit'),
    path('delete_student/<int:student_id>',views.delete_student,name='stud_delete'),
]
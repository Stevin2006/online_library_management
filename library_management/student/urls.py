from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet

router = DefaultRouter()
router.register(r'student',StudentViewSet)

urlpatterns = [
    path('',views.index,name='stud_home'),
    path('add_student/',views.add_student,name='stud_add'),
    path('edit_student/<int:student_id>',views.edit_student,name='stud_edit'),
    path('delete_student/<int:student_id>',views.delete_student,name='stud_delete'),
    path('api/',include(router.urls)),
]
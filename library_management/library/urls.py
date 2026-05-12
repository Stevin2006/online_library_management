from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
from .views import LibraryViewSet

router = DefaultRouter()
router.register(r'library', LibraryViewSet)

urlpatterns = [
    path('',views.index,name='lib_home'),
    path('lib_add/',views.add_barrow,name='lib_add'),
    path('lib_edit/<int:library_id>',views.edit_barrow,name='lib_edit'),
    path('lib_delete/<int:library_id>',views.delete_barrow,name='lib_delete'),
    path('api/',include(router.urls)),
]
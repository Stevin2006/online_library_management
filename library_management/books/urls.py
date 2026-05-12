from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

router = DefaultRouter()
router.register(r'books',BookViewSet)

urlpatterns = [
    path('',views.index,name='book_home'),
    path('add/',views.add_book,name='book_add'),
    path('edit/<int:book_id>/',views.update_book,name='book_edit'),
    path('delete/<int:book_id>/',views.delete_book,name='book_delete'),
    path('api/',include(router.urls)),
]
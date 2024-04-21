from django.urls import path
from store import views

urlpatterns = [
    path('', views.store, name='store'),
    path('index', views.index, name='index'),
    path('book/<int:book_id>', views.book_details, name='book_details')
]
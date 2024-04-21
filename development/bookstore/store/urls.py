from django.urls import path
from store import views

urlpatterns = [
    path('', views.store, name='store'),
    path('index', views.index, name='index'),
    path('book/<int:book_id>', views.book_details, name='book_details'),
    path('add/<int:book_id>', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:book_id>', views.remove_from_cart, name='remove_from_cart'),
    path('cart', views.cart, name='cart'),
]
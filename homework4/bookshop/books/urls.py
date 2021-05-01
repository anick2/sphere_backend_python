from django.urls import path
from .views import save_book, get_books, book_info, home

urlpatterns = [
    path('', home),
    path('save/', save_book),
    path('info/', get_books),
    path('info/<int:book_id>', book_info),
]


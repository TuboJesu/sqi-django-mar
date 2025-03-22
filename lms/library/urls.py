from django.urls import path

from . import views

app_name = 'library'

urlpatterns = [
    path('all-authors/', views.all_authors, name='authors'),
    path('book-signings/', views.book_signings, name='book_signings'),
    path('all-books/', views.all_books, name='all_books'),
    path('book-detail/<int:book_id>/', views.book_detail, name='book_detail'),


]
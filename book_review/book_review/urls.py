from django.urls import path
from . import views

app_name = "book_review"


urlpatterns = [
    path('',views.home, name="home"),
    path('all-book/', views.book_list, name="book_list"),
    path('book-detail/<int:book_id>/', views.book_detail, name="book_detail"),
    path('create-review/<int:book_id>/', views.review_creation, name="create_review"),
]
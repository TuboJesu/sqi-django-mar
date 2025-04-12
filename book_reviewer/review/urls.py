from django.urls import path


from . import views

app_name = "review"

urlpatterns = [
    path('list/books/', views.book_list, name="book_list"),
    path('book/detail/<int:book_id>/', views.book_detail, name="book_detail"),
    path('book/detail/manual/<int:book_id>/', views.book_detail_manual, name="book_detail_manual"),
]
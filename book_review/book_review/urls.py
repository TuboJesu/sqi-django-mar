from django.urls import path
from . import views

app_name = "book_review"


urlpatterns = [
    path('',views.home, name="home"),
    path('all-book/', views.book_list, name="book_list"),
    path('book-detail/<int:book_id>/', views.book_detail, name="book_detail"),
    path('create-review/<int:book_id>/', views.review_creation, name="create_review"),
    path('manual-create-review/<int:book_id>/', views.manual_review_creation, name="manual_create_review"),
    path('update-review/<int:review_pk>/', views.update_review, name="update_review"),
    path('manual-update-review/<int:review_id>/', views.update_review_with_form_dot_form, name="update_review_manual"),
    path('confirm-delete-review/<int:review_id>/', views.confirm_delete, name="confirm_delete"),
    path('delete-review/<int:review_id>/', views.delete_Review, name="delete"),

]

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .models import Book, Review
from .forms import ReviewForm, ReviewManualForm

# Create your views here.
def book_list(request):
    all_books = Book.objects.all()
    return render(request, "review/book-list.html", {"books": all_books})

def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    reviews_for_book = Review.objects.filter(book=book)
    reviews_for_book = book.reviews.all()
    review_form = ReviewForm()


    if request.method == "POST":
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.book = book
            review.save()
            # return redirect(reverse("review:book_detail", kwargs={"book_id": book.id}))
            return redirect("review:book_detail", pk=book.id)

    context = {
        "book": book,
        "reviews": reviews_for_book,
        "form": review_form
    }
    return render(request, "review/book-detail.html", context)


def book_detail_manual(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    # reviews_for_book = Review.objects.filter(book=book)
    reviews_for_book = book.reviews.all()
    review_form = ReviewManualForm()

    if request.method == "POST":
        review_form = ReviewManualForm(request.POST)
        if review_form.is_valid():
            cleaned_data = review_form.cleaned_data
            reviewer_name = cleaned_data.get('reviewer_name')
            rating = cleaned_data.get('rating')
            comment = cleaned_data.get("comment")

            Review.objects.create(book=book, reviewer_name=reviewer_name, rating=rating, comment=comment)
            return redirect("review:book_detail_manual", pk=book.id)

    context = {
        "book": book,
        "reviews": reviews_for_book,
        "form": review_form
    }
    return render(request, "review/book-detail-manual.html", context)




from django.shortcuts import render, get_object_or_404


from library.models import Book
from authors.models import Author

# Create your views here.
def all_authors(request):
    return render(request, "library/all-authors.html")


def book_signings(request):
    return render(request, "library/book-signings.html")


def all_books(request):

    all_books = Book.objects.order_by("-title")

    all_books_after_2000 = Book.objects.filter(published_on__gt = "2000-01-01")
    
    first_author = Author.objects.first()

    books_greater_than_200_and_before_1990 = Book.objects.filter(num_of_pages__gt = 200, published_on__lt = "1990-01-01")

    print(all_books)

    context = {

        "all_books": all_books,
        "all_books_after_2000": all_books_after_2000,
        "first_author": first_author,
        "books_greater_than_200_and_before_1990": books_greater_than_200_and_before_1990
    }

    return render(request, "library/all-authors.html", context)

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, "library/book_detail.html", {"book": book})
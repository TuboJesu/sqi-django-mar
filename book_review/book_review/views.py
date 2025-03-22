from django.shortcuts import render, get_object_or_404, redirect

from .models import Book, Review

from .forms import ReviewForm

def home(request):
    return render(request, "book_review/home.html")

def book_list(request):

    books = Book.objects.all()
    context = {
        "books": books
    }
    return render(request, "book_review/book_list.html", context)

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, "book_review/book_detail.html", {"book": book})

def review_creation(request, book_id):
    
    book = Book.objects.get(id=book_id)
    review_form = ReviewForm()
    
    if request.method == "POST":
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False) 
            review.book = book                       
            review.save()                            
            return redirect('book_review:book_detail', book_id=book.id)
    
    context = {

        "form": review_form,
        "book": book
    }
    
    return render(request, 'book_review/review_creation.html', context)


# Create your views here.

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse


from .models import Book, Review

from .forms import ReviewForm, ManualReviewForm, UpdateForm, UpdateManualForm

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
    
    return render(request, 'book_review/book_detail.html', context)

def manual_review_creation(request, book_id):
    
    book = Book.objects.get(id=book_id)
    review_form = ManualReviewForm()
    
    if request.method == "POST":
        review_form = ManualReviewForm(request.POST)
        if review_form.is_valid():
            cleaned_data = review_form.cleaned_data
            reviewer_name = cleaned_data.get('reviewer_name')
            rating = cleaned_data.get('rating')
            comment = cleaned_data.get('comment')
            Review.objects.create(book=book, reviewer_name=reviewer_name, rating=rating, comment=comment)
                                 
            return redirect('book_review:book_detail', book_id=book.id)
    
    context = {

        "form": review_form,
        "book": book
    }
    
    return render(request, 'book_review/review_creation.html', context)

def update_review(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    update_review_form = UpdateForm(instance=review)

    if request.method == "POST":
        update_review_form = UpdateForm(request.POST, instance=review)
        if update_review_form.is_valid():
            new_review = update_review_form.save(commit=False)
            new_review.reviewer_name = review.reviewer_name
            new_review.book = review.book
            new_review.save()
            return redirect(reverse('book_review:book_detail', kwargs={"book_id": review.book.id}))
    
    context = {

        "review": review,
        "form": update_review_form
    }

    return render(request, "book_review/update_review.html", context)

def update_review_with_form_dot_form(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    update_form = UpdateManualForm(initial={
            "rating": review.rating,
            "comment": review.comment
    })

    if request.method == "POST":
        update_form = UpdateManualForm(request.POST)
        if update_form.is_valid():
            cleaned_data = update_form.cleaned_data
            review.rating = cleaned_data.get('rating')
            review.comment = cleaned_data.get('comment')
            review.save()
            return redirect(reverse('book_review:book_detail', kwargs={"book_id": review.book.id}))

    context = {

        "review": review,
        "form": update_form
    }

    return render(request, "book_review/update_review_manual.html", context)



def confirm_delete(request, review_id):
    review = get_object_or_404(Review, pk=review_id)

    return render(request, "book_review/confirm_delete.html", {"review":review})


def delete_Review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)

    if request.method == "POST":
        review.delete()
        return redirect(reverse('book_review:book_detail', kwargs={"book_id": review.book.id}))
    



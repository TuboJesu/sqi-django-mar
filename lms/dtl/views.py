from django.shortcuts import render

# Create your views here.

def cart(request):

    context = {
        "user": "Jesu",
        "cart": ["tomato", "strawberry", "vanilla Ice Cream", "burger", "cake"],
        "is_favorite": True,
        "no_of_items": 5,
    }

    return render(request, "dtl/cart.html", context)

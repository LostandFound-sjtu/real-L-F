from django.shortcuts import render, redirect

from item.models import Item

# Create your views here.


# Home Page View

def index(request):
    # 2nd Div
    lost_item = Item.objects.filter(category="L").all()[:3]
    # End 2 div

    # table
    recent_item_item = Item.objects.filter(category="F").all()[:3]

    # Found Post Count Post
    b = Item.objects.filter(category="F").all()

    # Lost Post Count
    d = Item.objects.filter(category="L").all()

    context = {

        'lost_item': lost_item,
        'recent_found_item': recent_item_item,

        # Total Post Count
        'b': b,
        'd': d,

    }
    return render(request, 'index.html', context)


# Reward Function


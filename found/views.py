from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from item.models import Item
from .forms import  FoundItemModelForm
from tag.models import Tag
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def make(request,kind_name_slug):
    #  哇  动态ajax居然是可以实现的  哈哈！
    #tmp_tag=Tag.objects.filter(slug=kind_name_slug)
    #print(tmp_tag)
    found_item = Item.objects.filter(
        Q(tmp_slug=kind_name_slug) &
        Q(category='F')
    )
    #lost_item = Item.objects.filter(tag=tmp_tag)
    #print(lost_item)
    context_dict = {'found_item':found_item,
                    'type':'Found',}
    #print(context_dict)
    return render(request, 'make.html', context_dict)

def found(request):
    found_item = Item.objects.filter(category='F').all()
    search = request.GET.get('q')

    if search:

        found_item = Item.objects.filter(
            Q(status__icontains=search) |
            Q(name__icontains=search) |
            Q(category__icontains=search) |
            Q(location__icontains=search) |
            Q(phone_number__icontains=search) |
            Q(identification_mark__icontains=search) |
            Q(secret_information__icontains=search)
        )

    all_tag=Tag.objects.all()
    context = {
        'found_item': found_item,
        'all_tag':all_tag,
    }
    return render(request, 'found.html', context)



# Found Item Details

def found_item_details(request, id):
    f_item = get_object_or_404(Item, id=id)
    related_found_item = Item.objects.filter(location__icontains='dhaka')
    context = {
        'f_item': f_item,
        'related_found_item': related_found_item
    }


    return render(request, 'found-item-details.html', context)



@login_required(login_url='/login/')
def create_found_item(request):
    if request.method == 'POST':
        form = FoundItemModelForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.add_message(request, messages.SUCCESS, 'Post successfully complete')
            return redirect('/found/')
    else:
        form = FoundItemModelForm()

    context = {
        'form': form
    }
    return render(request, 'found-form.html', context)

# Found Item Update View

@login_required(login_url='/login/')
def found_item_update(request, id):
    fi_update = get_object_or_404(Item, id=id)
    form = FoundItemModelForm(request.POST or None, request.FILES or None, instance=fi_update)
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.SUCCESS, 'Update successfully complete')
        return redirect('found')
    context = {
        'form': form
    }
    return render(request, 'found-form.html', context)


# Found Item Delete

@login_required(login_url='/login/')
def found_item_delete(request, id):
    fi_delete = get_object_or_404(Item, id=id)
    if request.method == "POST":
        fi_delete.delete()
        messages.add_message(request, messages.WARNING, 'Delete successfully complete')
        return redirect('found')
    context = {
        'fi_delete': fi_delete
    }
    return render(request, 'found-item-delete.html', context)
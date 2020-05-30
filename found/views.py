from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from item.models import Item
from .forms import  FoundItemModelForm
from tag.models import Tag
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
from comment.models import ItemComment
from comment.forms import CommentForm
from django.core.mail import send_mail
from django.conf import settings
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
        'fi_delete': fi_delete,
        'id': id
    }
    return render(request, 'found-item-delete.html', context)

# Found Item Details
@login_required(login_url='/login/')
def found_item_details(request, id):
    f_item = get_object_or_404(Item, pk=id)
    f_item_content_type = ContentType.objects.get_for_model(f_item)
    comments = ItemComment.objects.filter(content_type=f_item_content_type, object_id=id, parent=None)
    context = {
        'f_item': f_item,
        'comments': comments.order_by('-comment_time'),
        'comment_form': CommentForm(
            initial={'content_type': f_item_content_type, 'object_id': id, 'reply_comment_id': 0})
    }
    return render(request, 'found-item-details.html', context)


def found_item_send_mail(request, id):
    l_item = get_object_or_404(Item, id=id)
    l_name = l_item.name
    l_address = l_item.mail_address
    message = "您在Lost&Found网站上所上传的 " + l_name + " 是否已近找到失主，如果找到的话烦请及时删除帖子"
    send_mail('Lost&Found 失物提醒邮件', message, settings.EMAIL_FROM,
    [l_address], fail_silently=False)
    context={
        'id' :id
    }

    return render(request, 'found_item_mail.html',context)

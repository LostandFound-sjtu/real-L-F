from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from item.models import Item
from lost.forms import LostItemModelForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from tag.models import Tag
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings


# Create your views here.
def make(request,kind_name_slug):
    #  哇  动态ajax居然是可以实现的  哈哈！
    #tmp_tag=Tag.objects.filter(slug=kind_name_slug)
    #print(tmp_tag)
    lost_item = Item.objects.filter(
        Q(tmp_slug=kind_name_slug) &
        Q(category='L')
    )
    #lost_item = Item.objects.filter(tag=tmp_tag)
    #print(lost_item)
    context_dict = {'lost_item':lost_item,
                    'type':'Lost',}
    #print(context_dict)
    return render(request, 'make.html', context_dict)
#  下面这个是主界面的展示函数
def lost(request):
    #  数据库内部匹配
    lost_item = Item.objects.filter(category='L').all()
    search = request.GET.get('q')
    #  这个内部搜索可以暂时留在这里，内部搜索实现
    all_tag = Tag.objects.all()
    if search:
        lost_item = Item.objects.filter(
            Q(status__icontains=search) |
            Q(name__icontains=search) |
            Q(category__icontains=search) |
            Q(location__icontains=search) |
            Q(phone_number__icontains=search) |
            Q(identification_mark__icontains=search) |
            Q(secret_information__icontains=search)
        )

    #  想要展示的标签，在前端需要映射到网址动态显示
    #  在lost_item里面已经拥有了丢失标签
    context = {
        'lost_item': lost_item,
        'all_tag':all_tag,
    }
    return render(request, 'lost.html', context)





#  下面是丢失物品的展示
@login_required(login_url='/login/')
def lost_item_details(request, id):
    l_item = get_object_or_404(Item, id=id)
    context = {
        'l_item': l_item
    }
    return render(request, 'lost-item-details.html', context)




#  丢失物品的表单
@login_required(login_url='/login/')
def create_lost_item(request):
    if request.method == 'POST':
        form = LostItemModelForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.add_message(request, messages.SUCCESS, 'Post successfully Created')
            return redirect('/lost/')
    else:
        form = LostItemModelForm()
    context = {
        'form': form
    }
    return render(request, 'lost-form.html', context)



# Lost Item Update

@login_required(login_url='/login/')
def lost_item_update(request, id):
    l_item_update = get_object_or_404(Item, id=id)
    form = LostItemModelForm(request.POST or None , instance=l_item_update)
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.SUCCESS, 'Update successfully complete')
        return redirect('/lost/')
    context = {
        'form': form
    }
    return render(request, 'lost-form.html', context)

# Lost Item Delete

@login_required(login_url='/login/')
def lost_item_delete(request, id):
    l_item_delete = get_object_or_404(Item, id=id)
    if request.method == "POST":
        l_item_delete.delete()
        messages.add_message(request, messages.WARNING, 'Post successfully Deleted')
        return redirect('/lost/')
    context = {
        'f_item_delete': l_item_delete
    }
    return render(request, 'lost_item_delete.html', context)

def data_refresh(request):
    tags = serializers.serialize("json", Tag.objects.all())
    context = {
        "all_tag": tags,
    }
    return JsonResponse(context)

def lost_item_send_mail(request, id):
    l_item = get_object_or_404(Item, id=id)
    l_name = l_item.name
    l_address = l_item.mail_address
    message = "您在Lost&Found网站上所上传的 " + l_name + " 有了新动态"
    send_mail('Lost&Found 失物提醒邮件', message, settings.EMAIL_FROM,
    [l_address], fail_silently=False)

    return render(request, 'lost_item_mail.html')

from django.shortcuts import render

import item.models as models
from django.db.models import Q

# item-0-0 :All
# item-0-1 :All Keys
# item-1-0 :All Found Items
# etc.
def multi_search(request, *args, **kwargs):
    request_path = request.path
    real_class_list = ['F', 'L']
    class_list = ['0', '1', '2']
    tag_list = ['0', '1', '2', '3', '4','5','6','7','8','9']
    class_id = kwargs.get('class_id')
    tag_id = kwargs.get('tag_id')
    item_list = []
    if class_id == '0' and tag_id != '0':
        print('s1')
        item_list = models.Item.objects.filter(tag=tag_list[int(tag_id)])

    elif class_id !='0' and tag_id == '0':
        print('s2')
        item_list = models.Item.objects.filter(category=real_class_list[int(class_id) - 1])
    elif class_id == '0' and tag_id == '0':
        print('s3')
        item_list = models.Item.objects.all()
    elif class_id !='0' and tag_id !='0':
        print('s4')
        item_list = models.Item.objects.filter(Q(category__icontains=real_class_list[int(class_id) - 1]) &
                                               Q(tag=tag_list[int(tag_id)])
                                               )
    return render(request, 'multi_search.html',{'class_list':class_list,
                                                'tag_list':tag_list,
                                                'item_list':item_list,
                                                'current_url':request_path})


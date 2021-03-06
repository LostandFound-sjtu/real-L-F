from django import template
from django.utils.safestring import mark_safe
register = template.Library()


@register.simple_tag
def action(current_url, item,index):

    url_part_list = current_url.split('-')

    if index == 2:
        list = ['全部','钥匙','学生卡','书','手机','自行车','钱包','水杯','MP3','充电宝']
        if item == url_part_list[2]:
             temp = "<a href='%s' class='active'>%s</a>"
        else:
            temp = "<a href='%s'>%s</a>"

        url_part_list[index] = item #拼接对应位置的部分url
    else:
        list = ['全部','拾物', '失物']
        if item == url_part_list[index]:
            temp = "<a href='%s' class='active'>%s</a>"
        else:
            temp = "<a href='%s'>%s</a>"

        url_part_list[index] = item

    ur_str = '-'.join(url_part_list)  #拼接整体url
    temp = temp %(ur_str, list[int(item)]) #生成对应的a标签
    return mark_safe(temp)  #返回安全的html

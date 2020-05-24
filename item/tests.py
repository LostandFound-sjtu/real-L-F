from django.test import TestCase
from .models import Item
from tag.models import Tag
# Create your tests here.

#  这里的测试用例貌似不太好写
class TagTestCase(TestCase):
    def setUp(self):
        Tag.objects.create(name="key")
        Tag.objects.create(name="idcard")
        Tag.objects.create(name="money")
        Tag.objects.create(name="vallet")
        Tag.objects.create(name="somethin")
        Tag.objects.create(name="cloth")
        Tag.objects.create(name="cat")
    def test_is_Tag_exist(self):
        key = Tag.objects.get(name="key")
        idcard = Tag.objects.get(name="idcard")
        self.assertEqual(key.name,"key")
        self.assertEqual(idcard.name,"idcard")

# class ItemTest(TestCase):
#     def setUp(self):
#         Item.objects.create(
#             status='lost',
#
#             name = 'sjtu'
#         )
#     def make_test(self):
#         emm=Item.objects.get(status='lost')
#         self.assertEqual(emm.status,'emm')



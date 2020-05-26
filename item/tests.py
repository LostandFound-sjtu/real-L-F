from django.test import TestCase
from item.models import Item
from tag.models import Tag
from home.models import MyUser
import unittest
from django.test import Client

# Create your tests here.

class ItemTest(TestCase):

    def setUp(self):
        #c = Client()

        #c.login(username='admin', password='sjtu-admin')
        MyUser.objects.create_user(username='hh', phone_number='13578946200', gender='M', email='1293018434@qq.com',password='asdad')
        Tag.objects.create(name = '手机')
        Item.objects.create(status='test', user = MyUser.objects.get(username='hh'), name='phone', 
                            
                            category = 'F',
                            location = 'nn',
                            phone_number = '111',
                            mail_address = '1932798582@qq.com',
                            image = ' ',
                            identification_mark = 'aa',
                            secret_information = 'aa',
                            tag = Tag.objects.get(name = '手机')
                            )
                      

    def test_email_successful(self):
        item1 = Item.objects.get(name='phone')
        mail = item1.get_mail()
        self.assertEqual(mail, '1932798582@qq.com')
        
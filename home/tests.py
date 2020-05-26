from django.test import TestCase,Client
from .models import MyUser
from django.contrib.auth.models import AbstractUser

# Create your tests here.

class IndexTset(TestCase):
    def test_index(self):
        #测试index视图
        response = self.client.get('/index/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

class LoginTest(TestCase):
    #测试登陆动作
    def setUp(self):
        MyUser.objects.create_user(username='hh', phone_number='13578946200', gender='M', email='1293018434@qq.com',password='asdad')
        MyUser.objects.create_user(username='hhh', phone_number='13468746200', gender='F', email='pip@sjtu.edu.cn', password='qwer1234')

    def test_model(self):
        #测试添加用户
        user_1 = MyUser.objects.get(username='hhh')
        user_2 = MyUser.objects.get(username='hh')
        self.assertEqual(user_1.gender, 'F')
        self.assertEqual(user_2.phone_number, "13578946200")

    def test_login_null(self):
        #用户名，密码为空
        test_data= {'username':'', 'password':''}
        response = self.client.post('/login/', data=test_data)
        self.assertEqual(response.status_code, 200)
        str = "用户名或密码错误"
        self.assertIn(str.encode(),response.content)

    def test_login_error(self):
        test_data = {'username': 'abc', 'password': '123'}
        response = self.client.post('/login/', data=test_data)
        str = "用户名或密码错误"
        self.assertIn(str.encode(), response.content)

    def test_login_action_success(self):
        #登录成功
        test_data = {'username': 'hhh', 'password': 'qwer1234'}
        response = self.client.post('/login/', data=test_data)
        self.assertEqual(response.status_code, 200)





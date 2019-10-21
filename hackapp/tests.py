import unittest
from django.test import TestCase, Client
from .models import User, Posts, Comments 
from .form import UserCreationFormSpec

#Client to test views 
class UrlTests(unittest.TestCase):
    def setUp(self):
        self.client = Client()
    
    def test_home(self):
        response = self.client.get('/home/')
        self.assertEqual(response.status_code, 200)
        
    def test_welcome(self):
        response = self.client.get('/welcome/')
        self.assertEqual(response.status_code, 200)
        
    def test_new(self):
        response = self.client.get('/newest/')
        self.assertEqual(response.status_code, 200)
        
    def test_newest_comments(self):
        response = self.client.get('/newestcomments/')
        self.assertEqual(response.status_code, 200)
        
    def test_signup(self):
        response = self.client.get('/signup/')
        self.assertEqual(response.status_code, 200)
        
    def test_login(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)
    
    def test_logout(self):
        response = self.client.get('/logout/')
        self.assertEqual(response.status_code, 200)
        
class ModelsTest(TestCase):
    
    def create_user(self, username="TestMan", email="just@test.com", password="1234fake"):
        return User.objects.create(username=username,email=email,password=password)
    
    def test_user_creation(self):
        testman = self.create_user()
        self.assertTrue(isinstance(testman, User))
        
    def test_user_can_create_post(self):
        testman = self.create_user()
        testpost = Posts.objects.create(author=testman, title="Just a test", body="Learning UnitTest so that my resume can be sharp")
        self.assertIs(testpost.author, testman)
        
    def test_user_can_leave_comment_on_post(self):
        testman = self.create_user()
        testpost = Posts.objects.create(author=testman, title="Just a test", body="Learning UnitTest so that my resume can be sharp")
        testcomment = Comments.objects.create(author=testman, post=testpost, body="I'm just testing you")
        self.assertIs(testcomment.author, testman)
        self.assertIs(testcomment.post, testpost)
        
class FormTest(TestCase):

    def test_form(self):
        data = {'username': 'Testman', 'email':'just@test.com', 'password1': '1234fake', 'password2': '1234fake'}
        form = UserCreationFormSpec(data=data)
        self.assertIs(form.is_valid(), True)
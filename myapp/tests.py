from django.test import TestCase

# Create your tests here.
from django.contrib.auth import get_user_model

class Myapp(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'laithhussein',
            email = 'laithalsanory9919@gmail.com',
            password = '123123123'
        )
    def test_create_new_user(self):
        self.assertEquals(self.user.email,'laithalsanory9919@gmail.com')
        self.assertEquals(self.user.username,'laithhussein')
    def test_duplicate_emails(self):
        try:
            self.user2 = get_user_model().objects.create_user(
                username = 'laithhussein',
                email = 'laithalsanory9919@gmail.com',
                password = '123123123'
            )
        except:
            print(' email is exist')
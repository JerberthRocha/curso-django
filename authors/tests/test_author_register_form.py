import imp
from django.test import TestCase
from authors.forms import RegisterForm
from parameterized import parameterized

class AuthorRegisterFormUnitTest(TestCase):
    @parameterized.expand([
        ('username','Your username'),
        ('email','Your e-mail'),
        ('first_name','Ex.: Michael'),
        ('last_name','Ex.: Scofield'),
        ('password','Your password'),
        ('confirm_password','Repeat your password'),
    ])
    def test_first_name_placeholder_is_correct(self, field, placeholder):
        form = RegisterForm()
        current_placeholder = form[field].field.widget.attrs['placeholder']
        self.assertEqual(current_placeholder, placeholder)
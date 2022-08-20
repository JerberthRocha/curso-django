from django import forms
from django.contrib.auth.models import User


def add_attr(field, attr_name, attr_new_value):
    existing_attr = field.widget.attrs.get(attr_name, '')
    field.widget.attrs[attr_name] = f'{existing_attr} {attr_new_value}'.strip()


def add_placeholder(field, placeholder_value):
    field.widget.attrs['placeholder'] = placeholder_value


class RegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields['username'], 'Your username')
        add_placeholder(self.fields['email'], 'Your e-mail')
        add_placeholder(self.fields['first_name'], 'Ex.: Michael')
        add_placeholder(self.fields['last_name'], 'Ex.: Scofield')

    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Your password.'
        }),
        error_messages={
            'required': 'Password must not be empty'
        },
        help_text=(
            'Password must have at least one uppercase letter,'
            'one lowercase letter and one number. The length should be'
            'at least 8 characters.'
        )
    )

    cofirm_password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Repeat your password.'
        }),
        error_messages={
            'required': 'Password must not be empty'
        },
    )

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
        ]

        labels = {
            'username': 'Username',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'E-mail',
            'password': 'Password',
        }

        help_texts = {
            'email': 'The e-mail must be valid.'
        }

        error_messages = {
            'username': {
                'required': 'This field must not be empty',
            },
            'password': {
                'required': 'This field must not be empty',
            }
        }

        widgets = {
            'password': forms.PasswordInput(attrs={
                'placeholder': 'Your password'
            }),
        }

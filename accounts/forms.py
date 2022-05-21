from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import get_user_model  # ユーザーモデルを取得するため
from .models import CustomUser
from allauth.account.forms import LoginForm, SignupForm

# # ユーザーモデル取得
# User = get_user_model()


# '''ログイン用フォーム'''


class MyLoginForm(LoginForm):

    # bootstrap4対応
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label


'''サインアップ用フォーム'''


class MySignupForm(SignupForm):

    # class meta:
    #     model = CustomUser
    #     fields = ('last_name', 'first_name', 'email', 'username',)

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['required'] = ''

            # オートフォーカスとプレースフォルダーの設定

            print(field.label)
            if field.label == '姓':
                field.widget.attrs['autofocus'] = ''
                field.widget.attrs['placeholder'] = '田中'
            elif field.label == '名':
                field.widget.attrs['placeholder'] = '一郎'
            elif field.label == 'メールアドレス':
                field.widget.attrs['placeholder'] = '***@gmail.com'

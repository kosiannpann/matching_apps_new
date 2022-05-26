from django.shortcuts import render, redirect
# from .forms import LoginForm, SignupForm
from django.contrib.auth.views import LoginView
from django.views import generic

'''プロフィール画面'''


def myprofile(request):
    return render(request, 'accounts/myprofile.html')


# '''ログイン'''


# class Login(LoginView):
#     from_class = LoginForm
#     template_name = 'account/login.html'


# '''サインアップ'''


# class Signup(generic.CreateView):
#     template_name = 'account/signup.html'
#     form_class = SignupForm

#     def form_valid(self, form):
#         user = form.save()
#         return redirect('account:signup_done')

#     # データ送信
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["process_name"] = "Sign up"
#         return context

from django.shortcuts import render, resolve_url
# from .forms import LoginForm, SignupForm
# from django.contrib.auth.views import LoginView
# vfrom django.views import generic
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import DetailView
from .models import CustomUser

'''プロフィール画面'''


def myprofile(request):
    return render(request, 'accounts/myprofile.html')


'''いつかプロフィールを制限する機能を実装する'''
# class OnlyYouMixin(UserPassesTestMixin):
#    raise_exception = False     # set True if raise 403_Forbidden

#    def test_func(self):
#        user = self.request.user
#        return user.pk == self.kwargs['pk'] or user.is_superuser


# class MyprofileView(OnlyYouMixin, DetailView):
#    model = CustomUser
#    template_name = 'accounts/myprofile.html'

#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        pass  # 必要に応じて処理を追加
#        return context

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

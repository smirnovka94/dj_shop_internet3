from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth.views import LoginView as BaseLoginView, PasswordResetView, PasswordResetDoneView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, FormView, UpdateView


from users.forms import UserForm, VerificationForm, UserChangeForm
from users.models import User
import random
import string
import copy

random_key = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
_key = copy.copy(random_key)


class LoginView(BaseLoginView):
    template_name = 'users/login.html'


class LogoutView(BaseLogoutView):
    pass


class RegisterView(CreateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('users:verification')
    template_name = 'users/register.html'

    def form_valid(self, form):
        self.object = form.save()
        verification_link = "http://127.0.0.1:8000/users/register/users/verification/"

        send_mail(
            subject='Поздравляем с регистрацией',
            message=f'Для завершения регистрации перейдите по ссылке: {verification_link} \n'
                    f'Для прохождения верификации скопируйте ключ: {_key}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.object.email]
        )
        return super().form_valid(form)


class UserVerificationView(FormView):
    form_class = VerificationForm
    success_url = reverse_lazy('main:home')
    template_name = 'users/user_verification.html'

    def post(self, request, *args, **kwargs):
        key_post = request.POST.get('key_post')
        if _key == key_post:
            return redirect('users:login')
        else:
            return render(request, 'users/user_verification.html', {'error_message': 'Ключи не совпадают'})


# _____________________________________________________________________
# _____________________________________________________________________
# _____________________________________________________________________

def resert(request):
    if request.method == "POST":
        User.objects.get(email='email')
        User.objects.password = _key
        print(_key)
    return render(request, 'users/user_detail.html')


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    success_url = reverse_lazy("users:login")
    template_name = 'register_without_password.html'
    form_class = UserForm

    # User.objects.get(email='email')
    # User.objects(password = _key)

    # def form_valid(self, form):
    #     user = form.save(commit=True)
    #     user.is_active = True
    #     token = secrets.token_urlsafe(nbytes=8)
    #
    #     user.token = token

    def get_object(self, queryset=None):
        return self.request.user


def send_new_password(request):
    # if request.method == "POST":
    email = request.POST.get('email')
    print(email)
    send_mail(
        subject='Вы сменили пароль!',
        message=f'Ваш новый пароль: {_key}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email]
    )
    request.user.set_password(_key)
    request.user.save()
    return redirect(reverse('users:login'))


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, user)
            return redirect(reverse('company:Dashboard'))
        else:
            return redirect(reverse('accounts:change_password'))
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'accounts/change_password.html', args)


class UserResetView(PasswordResetView):
    template_name = 'register_without_password.html'
    success_url = reverse_lazy("users:login")
    form_class = UserForm


class UserReset_password_sent(PasswordResetDoneView):
    pass

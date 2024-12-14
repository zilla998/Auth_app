from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import CustomUserCreationForm


class SingUpView(CreateView):
    """
    Представление для регистрации нового пользователя
    """
    form_class = CustomUserCreationForm
    template_name = 'users/singup.html'
    success_url = reverse_lazy('login')
    extra_context = {'title': 'Регистрация'}

    def form_valid(self, form):
        # Добавляем сообщение об успешной регистрации
        messages.success(self.request, 'Регистрация успешно завершена!')
        return super().form_valid(form)
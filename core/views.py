from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy

from core.forms import FormContato
from core.models import Funcionario, Servico, Cargo
from django.views.generic import FormView


class IndexView(FormView):
    template_name = "index.html"
    form_class = FormContato
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        # context = super(IndexView, self).get_context_data(**kwargs) -- Outra forma de herdar
        contexto['funcionarios'] = Funcionario.objects.order_by("?").all()  # Ordena os funcionários de forma aleatória
        contexto['servicos'] = Servico.objects.all()
        return contexto

    def form_valid(self, form):
        form.send_email()
        messages.success(self.request, 'E-mail enviado com sucesso!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Erro ao enviar o email')
        return super().form_invalid(form)

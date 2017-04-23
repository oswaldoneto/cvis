from django import views
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls.base import reverse
from django.views.generic.edit import FormView

from simple.forms import InputForm
from simple.logic import count_vocabulary


class AnalyzeView(FormView):
    form_class = InputForm
    template_name = 'simple.html'
    success_url = 'analyze'


    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            self.form_valid(form)
            context = self.get_context_data(**kwargs)
            context['data'] = count_vocabulary(form.cleaned_data['text'] )
            return render(self.request, self.template_name, context)
        else:
            return self.form_invalid(form, **kwargs)


    def form_valid(self, form):
        x = form.cleaned_data['text']
        return super(AnalyzeView, self).form_valid(form)
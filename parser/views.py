from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from . import models, parser, forms


class RezkaListView(generic.ListView):
    model = models.ParserModel
    template_name = 'parser/rezka_list.html'
    context_object_name = 'rezka'

    def get_queryset(self):
        return models.ParserModel.objects.all()

class GetParsingForm(generic.FormView):
    template_name = "parser/rezka_form.html"
    form_class = forms.ParserForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parser_data()
            return HttpResponse('<h1>Parsing is successful!</h1><a href="/film_list/">Перейти к фильмам</a>')
        else:
            return super(GetParsingForm, self).post(request, *args, **kwargs)

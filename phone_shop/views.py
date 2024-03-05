from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from . import models, forms


# C.R.U.D. - CREATE READ UPDATE DELETE

# Обновление
class UpdatePhoneView(generic.UpdateView):
    template_name = 'phones/update_phone.html'
    form_class = forms.PhoneShopForm
    success_url = '/'

    def get_object(self, **kwargs):
        phone_id = self.kwargs.get('id')
        return get_object_or_404(models.PhoneShop, id=phone_id)

    def form_valid(self, form):
        return super(UpdatePhoneView, self).form_valid(form=form)


# def update_phone_view(request, id):
#     phone_id = get_object_or_404(models.PhoneShop, id=id)
#     if request.method == 'POST':
#         form = forms.PhoneShopForm(request.POST, instance=phone_id)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('<h1>Успешно изменен в БД</h1><a href="/">Все телефоны</a>')
#     else:
#         form = forms.PhoneShopForm(instance=phone_id)
#     return render(request, template_name='phones/update_phone.html',
#                   context={'form': form, 'phone_id': phone_id})


# Удаление
class DeletePhoneView(generic.DeleteView):
    template_name = 'phones/confirm_delete.html'
    success_url = '/'

    def get_object(self, **kwargs):
        phone_id = self.kwargs.get('id')
        return get_object_or_404(models.PhoneShop, id=phone_id)


# def delete_phone_view(request, id):
#     phone_id = get_object_or_404(models.PhoneShop, id=id)
#     phone_id.delete()
#     return HttpResponse('<h1>Успешно удален в БД</h1> <a href="/">Все телефоны</a> ')


# Создание
class CreatePhoneView(generic.CreateView):
    template_name = 'phones/create_phone.html'
    form_class = forms.PhoneShopForm
    success_url = '/good/'

    def form_valid(self, form):
        return super(CreatePhoneView, self).form_valid(form=form)


def good_request(request):
    return render(request, template_name='phones/good.html',
                  context={'good': models.PhoneShop})


# def create_phone_view(request):
#     if request.method == 'POST':
#         form = forms.PhoneShopForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('<h1>Успешно добавлен в БД</h1> <a href="/">Все телефоны</a> ')
#     else:
#         form = forms.PhoneShopForm()
#     return render(request, template_name='phones/create_phone.html',
#                   context={'form': form})


# не полная информация
class PhoneShopView(generic.ListView):
    template_name = 'phones/phone_list.html'
    context_object_name = 'phone'
    model = models.PhoneShop

    def get_queryset(self):
        return self.model.objects.all()


# def phone_shop_view(request):
#     if request.method == 'GET':
#         phone = models.PhoneShop.objects.all()
#         return render(request, template_name='phones/phone_list.html',
#                       context={'phone': phone})


# детальная информация об объекте

class PhoneShopDetailView(generic.DetailView):
    template_name = 'phones/phone_detail.html'
    context_object_name = 'phone_id'

    def get_object(self, **kwargs):
        phone_id = self.kwargs.get('id')
        return get_object_or_404(models.PhoneShop, id=phone_id)


# def phone_shop_detail_view(request, id):
#     if request.method == 'GET':
#         phone_id = get_object_or_404(models.PhoneShop, id=id)
#         return render(request, template_name='phones/phone_detail.html',
#                       context={'phone_id': phone_id})

class SearchView(generic.ListView):
    template_name = 'phones/phone_list.html'
    context_object_name = 'phone'
    paginate_by = 5

    def get_queryset(self):
        return models.PhoneShop.objects.filter(title__icontains=self.request.GET.get("q"))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["q"] = self.request.GET.get("q")
        return context

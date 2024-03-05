from django.views import generic
from . import models


class AllProductListView(generic.ListView):
    template_name = 'lesson8/all_products.html'
    context_object_name = 'all_products'
    model = models.Product

    def get_queryset(self):
        return self.model.objects.filter().order_by('-id')


class OfficeProductListView(generic.ListView):
    template_name = 'lesson8/office_products.html'
    context_object_name = 'office_products'
    model = models.Product

    def get_queryset(self):
        return self.model.objects.filter(tag__name='для офиса').order_by('-id')

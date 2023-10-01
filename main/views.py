from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from main.forms import ProductForm, VersionForm
from main.models import Product, Version


def home(request):
    context = {
        'object_list': Product.objects.all(),
        'title': 'Skystore',
        'title_comments': 'Skystore - это отличный вариант выбора товара на любой вкус!'
    }
    return render(request, 'main/home.html', context)

def contacts(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}): {message}')
    return render(request, 'main/contacts.html')


class ProductListView(ListView):
    model = Product
    template_name = 'main/home.html'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'main/product.html'

class ProductCreatelView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'main/product_form.html'

    def get_success_url(self):
        return reverse('main:home')

class ProductUpdatelView(UpdateView):
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse('main:product', args=[self.kwargs.get('pk')])
    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            formset = VersionFormset(self.request.POST, instance=self.object)
        else:
            formset = VersionFormset(instance=self.object)
        context_data['formset'] = formset

        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)




class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('main:home')

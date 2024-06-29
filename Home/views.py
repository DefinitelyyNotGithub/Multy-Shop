from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView, CreateView, ListView
from .models import Contact, AboutUs_Model, FAQs_model
from .forms import ContactForm
from Product.models import ProductModel, SiteTitleBanner, Category
from django.db.models import Q

class HomeView(TemplateView):
    template_name = 'Home/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        context['banner'] = SiteTitleBanner.objects.all()
        context['product'] = ProductModel.objects.all()
        return context


class ContactView(CreateView):
    template_name = 'Home/contact.html'
    form_class = ContactForm

    def form_valid(self, form):
        form.save()
        return redirect('Home:home')


class AboutUsView(TemplateView):
    template_name = 'Home/about_us.html'

    def get_context_data(self, **kwargs):
        context = super(AboutUsView, self).get_context_data(**kwargs)
        context['obj'] = AboutUs_Model.objects.last()
        return context


class HelpView(TemplateView):
    template_name = 'Home/help.html'


class FAQsView(ListView):
    model = FAQs_model
    template_name = 'Home/FAQs.html'

    def get_context_data(self, *args, **kwargs):
        context = super(FAQsView, self).get_context_data(**kwargs)
        context['obj'] = FAQs_model.objects.all()
        return context


def search(request):
    searched = request.GET.get('searched')
    searched = ProductModel.objects.filter(Q(title__icontains=searched) | Q(product_description__icontains=searched))
    if searched:
        return render(request, 'product/product_list.html', {'obj': searched})
    else:
        return render(request, 'product_not_found.html', {})

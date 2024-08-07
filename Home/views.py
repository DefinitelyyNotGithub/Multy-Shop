from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView, CreateView, ListView
from .models import Contact, AboutUs_Model, FAQs_model
from .forms import ContactForm
from Product.models import ProductModel, SiteTitleBanner, Category, DiscountPrice, RecentlyViewedProducts
from django.db.models import Q


class HomeView(TemplateView):
    template_name = 'Home/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        if len(Category.objects.filter(on_first_page=True)) >= 12:
            twelve_cats = Category.objects.filter(on_first_page=True)[:12]
        else:
            twelve_cats = Category.objects.all()[:12]
        context['featured_products'] = ProductModel.objects.order_by('-sell_count').distinct()[:8]
        context['category'] = twelve_cats
        context['banner'] = SiteTitleBanner.objects.all()
        context['product'] = ProductModel.objects.all()
        context['global_off'] = DiscountPrice.objects.filter(apply_to_all_products=True, is_active=True).last()

        # if self.request.is_authenticated:
        #     recently_viewed = RecentlyViewedProducts.objects.filter(user=self.request.user).order_by('-date').dis[:8]
        #     context['recent_viewed'] = [item.product for item in recently_viewed]

        active_discounts = DiscountPrice.objects.filter(is_active=True)
        context['active_discounts'] = ProductModel.objects.filter(discount__in=active_discounts)
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

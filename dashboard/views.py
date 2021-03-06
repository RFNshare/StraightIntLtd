from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import *

from customer.models import *
from sell.models import *
from .forms import *


# Create your views here.


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/dashboard.html'

    def get(self, request):
        labels = []
        data = []
        invoice = Invoice.objects.all()
        total_customer = Customer.objects.all().count()
        total_invoices = Invoice.objects.all().count()
        for item in invoice:
            labels.append(item.name)
            data.append(item.balance)
        # context = super().get_context_data(**kwargs)
        ctx = {
            'qs': invoice,
            'labels': labels,
            'data': data,
            'total_customer': total_customer,
            'total_invoices': total_invoices
        }
        return render(request, self.template_name, ctx)


class ProfileView(LoginRequiredMixin, DetailView):
    template_name = 'dashboard/profile.html'
    model = User


# class ProfileUpdateView(UpdateView):
#     template_name = 'dashboard/profile_update.html'
#     model = Profile
#     form_class = ProfileUpdateForm

def profile_update(request, pk):
    player, created = Profile.objects.get_or_create(staff=request.user)
    user_form = UserUpdateForm(instance=request.user)
    profile_form = ProfileUpdateForm(instance=request.user.profile)
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('dashboard:profile', pk=pk)
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'dashboard/profile_update.html', context)

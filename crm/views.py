from django.utils import timezone
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from . import models
from . import forms
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView


def list_clients(request):
    clients = models.Client.objects.all()
    return render(request, 'crm/list_clients.html', {'clients': clients})


@login_required
def list_calls(request):
    calls = models.Call.objects.order_by('publish')
    return render(request, 'crm/list_calls.html', {'calls': calls})


def list_reminders(request):
    reminders = models.Reminder.objects.order_by('deadline')
    return render(request, 'crm/list_reminders.html', {'reminders': reminders})


def list_deals(request):
    deals = models.Deal.objects.order_by('publish')
    return render(request, 'crm/list_deals.html', {'deals': deals})


class DetailClient(DetailView):
    model = models.Client
    template_name = 'crm/detailed_client.html'
    context_object_name = 'client'


class DetailCall(DetailView):
    model = models.Call
    template_name = 'crm/detailed_call.html'
    context_object_name = 'call'


class DetailDeal(DetailView):
    model = models.Deal
    template_name = 'crm/detailed_deal.html'
    context_object_name = 'deal'


class DetailReminder(DetailView):
    model = models.Reminder
    template_name = 'crm/detailed_reminder.html'
    context_object_name = 'reminder'


@login_required
def create_client(request):
    error = ''
    if request.method == 'POST':
        form = forms.ClientForm(request.POST)
        if form.is_valid():
            new_client = form.save(commit=False)
            new_client.author = request.user
            new_client.save()
            return redirect('list_clients')
        else:
            error = 'Форма заполнена неверно'
    form = forms.ClientForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'crm/create_client.html', data)


@login_required
def create_call(request):
    error = ''
    if request.method == 'POST':
        form = forms.CallForm(request.POST)
        if form.is_valid():
            new_call = form.save(commit=False)
            new_call.author = request.user
            new_call.save()
            return redirect('list_calls')
        else:
            error = 'Форма заполнена неверно'
    form = forms.CallForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'crm/create_call.html', data)


@login_required
def create_deal(request):
    error = ''
    if request.method == 'POST':
        form = forms.DealForm(request.POST)
        if form.is_valid():
            new_deal = form.save(commit=False)
            new_deal.author = request.user
            new_deal.save()
            return redirect('list_deals')
        else:
            error = 'Форма заполнена неверно'
    form = forms.DealForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'crm/create_deal.html', data)


@login_required
def create_reminder(request):
    error = ''
    if request.method == 'POST':
        form = forms.ReminderForm(request.POST)
        if form.is_valid():
            new_reminder = form.save(commit=False)
            new_reminder.author = request.user
            new_reminder.save()
            return redirect('list_reminders')
        else:
            error = 'Форма заполнена неверно'
    form = forms.ReminderForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'crm/create_reminder.html', data)


class RegisterUser(FormView):
    form_class = forms.RegistrationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'

    def form_valid(self, form):
        form.save()
        return super(RegisterUser, self).form_valid(form)


class ClientUpdate(UpdateView):
    model = models.Client
    template_name = 'crm/create_client.html'
    form_class = forms.ClientForm


class CallUpdate(UpdateView):
    model = models.Call
    template_name = 'crm/create_call.html'
    form_class = forms.CallForm


class DealUpdate(UpdateView):
    model = models.Deal
    template_name = 'crm/create_deal.html'
    form_class = forms.DealForm


class ReminderUpdate(UpdateView):
    model = models.Reminder
    template_name = 'crm/create_reminder.html'
    form_class = forms.ReminderForm


class CallDelete(DeleteView):
    model = models.Call
    template_name = 'crm/delete_page.html'
    success_url = reverse_lazy('list_calls')


class DealDelete(DeleteView):
    model = models.Deal
    template_name = 'crm/delete_page.html'
    success_url = reverse_lazy('list_deals')


class ReminderDelete(DeleteView):
    model = models.Reminder
    template_name = 'crm/delete_page.html'
    success_url = reverse_lazy('list_reminders')


def homepage(request):
    text = "Планы на сегодня"
    startdate = timezone.now()
    enddate = startdate + timezone.timedelta(days=1)

    reminders = models.Reminder.objects.filter(deadline__range=[startdate, enddate])
    data = {
        'text': text,
        'reminders': reminders,
        'startdate': startdate,
    }
    return render(request, 'crm/homepage.html', data)


def homepageweek(request):
    text = "Планы на неделю"
    startdate = timezone.now()
    enddate = startdate + timezone.timedelta(days=7)
    reminders = models.Reminder.objects.filter(deadline__range=[startdate, enddate]).order_by('deadline')
    data = {
        'text': text,
        'reminders': reminders,
        'startdate': startdate,
    }
    return render(request, 'crm/homepage.html', data)


def homepagelate(request):
    text = "Просроченые события!"
    startdate = timezone.now()
    sdate = startdate - timezone.timedelta(days=14)
    enddate = startdate + timezone.timedelta(days=7)

    reminders = models.Reminder.objects.filter(deadline__range=[sdate, startdate]).order_by('deadline')
    data = {
        'text': text,
        'reminders': reminders,
        'startdate': startdate,
    }
    return render(request, 'crm/homepage.html', data)

from django.shortcuts import render
from .models import Items, Customer
from .forms import ItemsForm, CustomerForm, AddressForm, NotesForm, OtherDetailsForm


def index(request):
    return render(request, 'app/index.html')


def purchase(request):
    return render(request, 'app/purchase.html')


def settings(request):
    return render(request, 'app/settings.html')


def reports(request):
    return render(request, 'app/reports.html')


def items(request):
    if request.method == 'POST':
        form = ItemsForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            sku = form.cleaned_data['sku']
            instance.save()
            print(sku)
    else:
        form = ItemsForm()
        print('error')
    instance = {
        'form': form
    }
    return render(request, 'app/items.html', instance)


def contact(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
    else:
        form = CustomerForm()
        print('error')
    instance = {
        'form': form
    }
    return render(request, 'app/contact.html', instance)


def creditnotes(request):
    return render(request, 'app/sales/creditnotes.html')


def deliverychallans(request):
    return render(request, 'app/sales/deliverychallans.html')


def estimates(request):
    return render(request, 'app/sales/estimates.html')


def invoices(request):
    return render(request, 'app/sales/invoices.html')


def paymentrecevied(request):
    return render(request, 'app/sales/paymentrecevied.html')


def recurringinvoices(request):
    return render(request, 'app/sales/recurringinvoices.html')


def retainerinvoice(request):
    return render(request, 'app/sales/retainerinvoice.html')


def salesorders(request):
    return render(request, 'app/sales/salesorders.html')

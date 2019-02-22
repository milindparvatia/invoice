from django.shortcuts import render
from .models import Items, Customer
from .forms import ItemsForm, CustomerForm, AddressForm, NotesForm, OtherDetailsForm


def index(request):
    return render(request, 'app/index.html')


def settings(request):
    return render(request, 'app/settings.html')


def reports(request):
    return render(request, 'app/reports.html')


# def items(request):
#     if request.method == 'POST':
#         form = ItemsForm(request.POST)
#         if form.is_valid():
#             instance = form.save(commit=False)
#             sku = form.cleaned_data['sku']
#             instance.save()
#             print(sku)
#     else:
#         form = ItemsForm()
#         print('error')
#     instance = {
#         'form': form
#     }
#     return render(request, 'app/items.html', instance)


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


def manual(request):
    return render(request, 'app/Accountant/manual.html')


def chatacc(request):
    return render(request, 'app/Accountant/chatacc.html')


def currency(request):
    return render(request, 'app/Accountant/currency.html')


def translocking(request):
    return render(request, 'app/Accountant/translocking.html')


def bills(request):
    return render(request, 'app/purchase/bills.html')


def expenses(request):
    return render(request, 'app/purchase/expenses.html')


def paymade(request):
    return render(request, 'app/purchase/paymade.html')


def purchaseorders(request):
    return render(request, 'app/purchase/purchaseorders.html')


def recurringbills(request):
    return render(request, 'app/purchase/recurringbills.html')


def recurringexpenses(request):
    return render(request, 'app/purchase/recurringexpenses.html')


def vendorcredit(request):
    return render(request, 'app/purchase/vendorcredit.html')


def items(request):
    return render(request, 'app/items/items.html')


def inventoryad(request):
    return render(request, 'app/items/inventoryad.html')


def pricelist(request):
    return render(request, 'app/items/pricelist.html')


def banking(request):
    return render(request, 'app/banking.html')

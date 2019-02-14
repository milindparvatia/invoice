from django.shortcuts import render
from .models import Items, Customer
from .forms import ItemsForm, CustomerForm


def index(request):
    puserdata = Items.objects.all().values()
    image = puserdata[0]['profile_pic']
    instance = {
        'image': image,
    }
    return render(request, 'app/index.html', instance)


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
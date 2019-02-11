from django.shortcuts import render
from .models import Items
from .forms import ItemsForm


def index(request):
    return render(request, 'app/index.html')


def purchase(request):
    return render(request, 'app/purchase.html')


def settings(request):
    return render(request, 'app/settings.html')


def reports(request):
    return render(request, 'app/reports.html')


def items(request):
    return render(request, 'app/items.html')


def contact(request):
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
    return render(request, 'app/contact.html', instance)

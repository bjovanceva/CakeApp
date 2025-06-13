from lib2to3.fixes.fix_input import context

from django.shortcuts import render, redirect

from cake_app.forms import CakeForm
from cake_app.models import Cake


# Create your views here.

def index(request):
    cakes=Cake.objects.all()
    context={'cakes_list': cakes}
    return render(request, 'index.html', context)

def add_cake(request):
    if request.method=='POST':
        form=CakeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')


    else:
        form=CakeForm()
        return render(request, 'add_cake.html', context={'form': form})

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from bank.forms import PersonForm


@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def person_create(request, template_name='crud/create.html'):
    form = PersonForm(request.POST or None)
    if form.is_valid():
        person = form.save(commit=False)
        person.user = request.user
        person.save()
        return redirect('home')
    return render(request, template_name, {'form':form})


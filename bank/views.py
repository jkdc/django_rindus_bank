from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from bank.forms import PersonForm
from bank.models import Person


@login_required
def home(request):
    if request.user.is_authenticated:
        accounts = Person.objects.filter(admin_person=request.user.pk)
        return render(request, 'home.html', {'people_list': accounts})
    return redirect('login')

@login_required
def person_create(request, template_name='crud/create.html'):
    form = PersonForm(request.POST or None)
    if form.is_valid():
        person = form.save(commit=False)
        person.admin_person = request.user
        person.save()
        return redirect('home')
    return render(request, template_name, {'form':form})


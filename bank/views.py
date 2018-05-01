from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

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

@login_required
def person_update(request, pk, template_name='crud/create.html'):
    if request.user.is_authenticated:
        person = get_object_or_404(Person, pk=pk)
    form = PersonForm(request.POST or None, instance=person)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, template_name, {'form':form})

@login_required
def person_delete(request, pk, template_name='crud/delete_confirmation.html'):
    if request.user.is_authenticated:
        person= get_object_or_404(Person, pk=pk)
    if request.method=='POST':
        person.delete()
        return redirect('home')
    return render(request, template_name, {'object':person})

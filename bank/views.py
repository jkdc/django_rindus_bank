from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from bank.forms import PersonForm, AccountForm
from bank.models import Person, Account


@login_required
def home(request):
    if request.user.is_authenticated:
        accounts = Person.objects.filter(admin_person=request.user.pk)
        return render(request, 'home.html', {'people_list': accounts})
    return redirect('login')

#CRUD: Person
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
    return render(request, template_name, {'object':person.first_name + " " + person.last_name})

@login_required
def person_read(request, pk, template_name='crud/show.html'):
    if request.user.is_authenticated:
        person = get_object_or_404(Person, pk=pk)
        accounts = Account.objects.filter(person=person)
        return render(request, template_name, {'person':person, 'accounts':accounts})
    return render(request, template_name)

#CRUD: Account
@login_required
def account_create(request, pk, template_name='crud/create.html'):
    form = AccountForm(request.POST or None)
    if form.is_valid():
        person= get_object_or_404(Person, pk=pk)

        account = form.save(commit=False)
        account.person = person
        account.save()
        return redirect('home')
    return render(request, template_name, {'form':form})

@login_required
def account_update(request, pk, template_name='crud/create.html'):
    if request.user.is_authenticated:
        account = get_object_or_404(Account, pk=pk)
    form = AccountForm(request.POST or None, instance=account)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, template_name, {'form':form})


@login_required
def account_delete(request, pk, template_name='crud/delete_confirmation.html'):
    if request.user.is_authenticated:
        account= get_object_or_404(Account, pk=pk)
    if request.method=='POST':
        account.delete()
        return redirect('home')
    return render(request, template_name, {'object': account.iban})

@login_required
def account_read(request, pk, template_name='crud/show_account.html'):
    if request.user.is_authenticated:
        account = get_object_or_404(Account, pk=pk)
        return render(request, template_name, {'account':account})
    return render(request, template_name)
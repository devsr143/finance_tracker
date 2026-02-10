from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Transaction
from .forms import TransactionForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})



def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
    else:
        form = AuthenticationForm()

    return render(request, "login.html", {"form": form})



def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def transaction_create(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            return redirect('dashboard')
    else:
        form = TransactionForm()

    return render(request, 'update.html', {'form': form})


@login_required
def dashboard(request):
    transactions = Transaction.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'transactions': transactions})


@login_required
def transaction_update(request, id):
    transaction = Transaction.objects.get(
        id=id,
        user=request.user
    )

    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = TransactionForm(instance=transaction)

    return render(request, 'update.html', {'form': form})




@login_required
def transaction_delete(request, id):
    transaction = Transaction.objects.get(
        id=id,
        user=request.user
    )

    if request.method == 'POST':
        transaction.delete()
        return redirect('dashboard')

    return render(request, 'delete.html', {'transaction': transaction})

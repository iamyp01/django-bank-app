from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
# Create your views here.


def home(request):
    return render(request, 'accounts/home.html')

def customers(request):
    customers = Customer.objects.all()
    return render(request, 'accounts/customers.html', {'customers':customers})

def transfers(request):
    transfers = Transfer.objects.all()
    return render(request, 'accounts/transfers.html', {'transfers':transfers})

def customerDetail(request, pk):
    customer = Customer.objects.get(pk=pk)
    return render(request, 'accounts/customerDetail.html',{'customer':customer})

def createTransfers(request, pk):
    user = Customer.objects.get(pk=pk)
    customers = Customer.objects.all()
    if request.method == 'POST':
        send_to_name = request.POST.get('account_type')
        send_to = Customer.objects.get(pk=send_to_name)
        amount = request.POST.get('amount')
        if int(amount) <= user.current_balance:
            user.current_balance = user.current_balance - int(amount)
            user.total_tranfers = user.total_tranfers + 1
            user.save()
            send_to.current_balance = send_to.current_balance + int(amount)
            send_to.save()
            transfer = Transfer(send_by=user, send_to=send_to, amount=amount)
            transfer.save()
            messages.success(request, f'You have successfully made a transfer of {amount} to {send_to.first_name} {send_to.last_name}')
            return redirect('transfers')
        else:
            messages.error(request, 'You have unsufficient funds to make this transfer')
            
    return render(request, 'accounts/createTransfers.html', {'customers':customers, 'user':user})

def credits(request):
    return render(request, 'accounts/credits.html')
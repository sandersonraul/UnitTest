from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Category, Expense
# Create your views here.
@login_required(login_url='/authentication/login')
def index(request):
  return render(request, 'index.html')

@login_required
def add_expense(request):
  categories = Category.objects.all()
  context = {
    'categories': categories,
    'values': request.POST
  }
  if request.method == 'GET':
    return render(request, 'add_expense.html', context)

  if request.method == 'POST':
    amount = request.POST['amount']

    if not amount:
      messages.error(request, 'Amount is required')
      return render(request, 'add_expense.html', context)
    description = request.POST['description']
    date = request.POST['expense_date']
    category = request.POST['category']

    if not description:
        messages.error(request, 'description is required')
        return render(request, 'add_expense.html', context)

    Expense.objects.create(owner=request.user, amount=amount, date=date,
                            category=category, description=description)
    messages.success(request, 'Expense saved successfully')

    return redirect('expenses')

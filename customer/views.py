from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Customer, Order, Payment

@login_required
def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customer/customer_list.html', {'customers': customers})

@login_required
def order_list(request):
    orders = Order.objects.all()
    return render(request, 'customer/order_list.html', {'orders': orders})

@login_required
def payment_list(request):
    payments = Payment.objects.all()
    return render(request, 'customer/payment_list.html', {'payments': payments})

# def student_list(request):
#     students = Student.objects.all()
#     return render(request, 'home/student_list.html', {'students': students})

# def student_detail(request, student_id):
#     student = get_object_or_404(Student, id=student_id)
#     return render(request, 'home/student_detail.html', {'student': student})

# Check if the user is a superuser



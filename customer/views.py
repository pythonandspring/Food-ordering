from django.shortcuts import render
from django.views.generic.list import ListView
from django.shortcuts import render, get_object_or_404
# from .models import Student
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from random import choice
from customer.models import customerUser, Feedback, Contact
from django.shortcuts import render, redirect
from django.http import JsonResponse
from customer.models import State, City, Place
from django.contrib.auth import get_user_model
# Create your views here.

User = get_user_model()

def loginUser(request):

    
    if request.method == 'POST':
        User = get_user_model()
        username = request.POST.get('email')
        password = request.POST.get('password')
        
        # if not User.objects.filter(email = username).exists():
        #     messages.error(request,'Username is not in database')
        #     return redirect('login')

        user = authenticate(username=username, password=password)
        print(user)
        if user is None:
            messages.error(request,'Invalid Password or Username')
            return redirect('login')
        elif user.is_delivery:
            messages.error(request,'You are Registered as delivery')
            return redirect('login')
        elif user.is_restaurant:
            messages.error(request,'You are Registered as restaurant')
            return redirect('login')
        else:
            login(request,user)
            messages.success(request,'Successfully Login')
            render(request,'authentication/login.html')
            return redirect('menu')


        
    return render(request,'authentication/login.html')

def registerUser(request):
    states = State.objects.all()
    if request.method == 'POST':
        
        User = get_user_model()
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        state_id = request.POST.get('state')
        city_id = request.POST.get('city')
        place_id = request.POST.get('place')
        
        state = State.objects.get(id=state_id)
        city = City.objects.get(id=city_id)
        place = Place.objects.get(id=place_id)

        if customerUser.objects.filter(email= email).exists():
            messages.error(request,'User Already Exist in the System')
            return redirect('login')
        hashed_password = make_password(password)


        try:
            user = customerUser.objects.create(
                name=name,
                email=email,
                username=email,
                password=hashed_password,
                is_user=True,
                  state=state, 
                city=city, 
                place=place
            )
            user.save()
            messages.success(request,'Successfully Registered')
            return redirect('login')
        except:
            messages.error(request,'Error!! Try Again')
            

    return render(request,'authentication/register.html', {'states': states})

def forgetPassword(request):
    return render(request,'authentication/forgetPassword.html')

def logoutUser(request):
    User = get_user_model()
    logout(request)
    return render(request,'authentication/logout.html')

def feedback_form(request):

    if request.method == 'POST':
        print("entered")
        
        comments=request.POST.get('comment')
        try:
            Fb = Feedback() 
            Fb.stars = 0
            Fb.comments = comments
            Fb.save()
            return render(request, 'thank_you.html')  # Render the thank you page
        except:
            return HttpResponse('<h1>Sorry!</h1><p>There is an issue</p>')
    return render(request,'feedback.html')

def index(request):
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        contact.name = name
        contact.email = email
        contact.subject = subject
        contact.save()
        return render(request, 'thank_you.html')  # Render the thank you page
    return render(request, 'contact.html')

def Home(request):
    return render(request,'home.html')


def load_cities(request):
    state_id = request.GET.get('state_id')
    cities = City.objects.filter(state_id=state_id).values('id', 'name')
    return JsonResponse(list(cities), safe=False)

def load_places(request):
    city_id = request.GET.get('city_id')
    places = Place.objects.filter(city_id=city_id).values('id', 'name')
    return JsonResponse(list(places), safe=False)

# def student_list(request):
#     students = Student.objects.all()
#     return render(request, 'home/student_list.html', {'students': students})

# def student_detail(request, student_id):
#     student = get_object_or_404(Student, id=student_id)
#     return render(request, 'home/student_detail.html', {'student': student})

# class customerListView(generic.ObjectListView):
#     queryset = Provider.objects.annotate(
#         count_circuits=count_related(Circuit, 'provider')
#     )
#     filterset = filtersets.ProviderFilterSet
#     filterset_form = forms.ProviderFilterForm
#     table = tables.ProviderTable

# class customerView(GetRelatedModelsMixin, generic.ObjectView):
#     queryset = Provider.objects.all()

#     def get_extra_context(self, request, instance):
#         return {
#             'related_models': self.get_related_models(request, instance),
#         }

# class customerEditView(generic.ObjectEditView):
#     queryset = Provider.objects.all()
#     form = forms.ProviderForm


# class customerDeleteView(generic.ObjectDeleteView):
#     queryset = Provider.objects.all()


from django.shortcuts import render, redirect
from django.http import JsonResponse
from new_app.models import State, City, Place, UserLocation

def location_view(request):
    states = State.objects.all()
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        state_id = request.POST.get('state')
        city_id = request.POST.get('city')
        place_id = request.POST.get('place')
        
        state = State.objects.get(id=state_id)
        city = City.objects.get(id=city_id)
        place = Place.objects.get(id=place_id)
        
        UserLocation.objects.create(user_name=user_name, state=state, city=city, place=place)
        return redirect('location')
    
    return render(request, 'new_app/location.html', {'states': states})

# def location_view(request):
#     states = State.objects.all()
#     return render(request, 'new_app/location.html', {'states': states})

def load_cities(request):
    state_id = request.GET.get('state_id')
    cities = City.objects.filter(state_id=state_id).values('id', 'name')
    return JsonResponse(list(cities), safe=False)

def load_places(request):
    city_id = request.GET.get('city_id')
    places = Place.objects.filter(city_id=city_id).values('id', 'name')
    return JsonResponse(list(places), safe=False)
from django.shortcuts import render
import json
import urllib.request
# Create your views here.


def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        res = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q=' +
                                     city + '&appid=f3f2026f24b869e058c3a224d2f4ba07').read()
        json_data = json.loads(res)
        kelvin = int(json_data['main']['temp'])
        cent = kelvin-273

        data = {
            'city': city,
            'country_code': str(json_data['sys']['country']),
            'coordinate': str(json_data['coord']['lon'])+' ' + str(json_data['coord']['lat']),
            'temp': str(json_data['main']['temp'])+'k',
            'temp2': str(cent)+'c',
            'pressure': str(json_data['main']['pressure']),
            'humidity': str(json_data['main']['humidity']),
        }
    else:
        city = ''
        data = {}

    return render(request, 'index.html', data)

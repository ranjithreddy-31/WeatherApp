from django.shortcuts import render,redirect
import requests
def first(request):
    return render(request,'w.html')
def index(request):
    if request.method=='POST':
        url='http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=271d1234d3f497eed5b1d80a07b3fcd1'
        url1='https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference=CnRtAAAATLZNl354RwP_9UKbQ_5Psy40texXePv4oAlgP4qNEkdIrkyse7rPXYGd9D_Uj1rVsQdWT4oRz4QrYAJNpFX7rzqqMlZw2h2E2y5IKMUZ7ouD_SlcHxYq1yL4KbKUv3qtWgTK0A6QbGh87GB3sscrHRIQiG2RrmU_jF4tENr9wGS_YxoUSSDrYjWmrNfeEHSGSc3FyhNLlBU&key=AIzaSyBpkhR7TDDPpd_weQ-dDoqcBwd6uMtXwAE'
        city=request.POST['C'] 
        r=requests.get(url.format(city)).json()
        city_weather={
            'city':city,
            'temp':r['main']['temp'],
            'description':r['weather'][0]['description'],
            'icon':r['weather'][0]['icon']

        }
        return render(request,"weather.html",{'c':city_weather})
    else:
        return redirect('/weather')


# Create your views here.

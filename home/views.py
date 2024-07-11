from django.shortcuts import render,redirect, HttpResponse
from .models import User, Case
from django.contrib import messages
import asyncio,requests,json

# Create your views here.
def home(request):
    return render(request, 'home.html')

def data_input(request):
    if request.method == 'POST':
        data=request.POST
        f_name = str(data.get('f_name')).capitalize()
        l_name = str(data.get('l_name')).capitalize()
        m_no=data.get('m_no')
        govt_id=data.get('govt_id')
        name=f_name+" "+l_name
        if User.objects.filter(govt_id=govt_id).exists():
            return redirect(profile, govt_id)
        messages.warning(request, 'User is Not Present in the Database')
        return redirect(profile,govt_id)
    return render(request, 'data_form.html')

def profile(request,id):
    response=asyncio.run(search(id))
    if response.status_code==404:
        pbj={"name":None,"age":None,"Gender":None,"total_cases":None,"cases_names":None,"address":None}
        return render(request, 'profile.html', pbj)
    response=json.loads(response.content.decode('utf-8'))
    data=resp_to_dict(response)
    #i want to print the data in the console from dict data response
    name=data['name']
    age=data['age']
    Gender=data['Gender']
    total_cases=data['total_cases']
    cases_names=data['cases_names']
    address=data['address']
    pbj={"name":name,"age":age,"Gender":Gender,"total_cases":total_cases,"cases_names":cases_names,"address":address}
    return render(request, 'profile.html', pbj)

async def search(id):
    url=f"http://localhost:8000/search/{id}/"
    response=(requests.get(url))
    return (response)

def resp_to_dict(response):
    response=response[1:-1]
    response=json.loads(response)
    response=response['fields']
    return response
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
import requests
# Create your views here.

class banklist(APIView):
    def get(self,request,bank_name,city):
        bank_ins = Branch.objects.filter(bank=Bank.objects.get(bank_name = bank_name),city = City.objects.get(city_name = city))
        serializer = Branchserialzer(bank_ins,many=True)
        return Response(serializer.data)

class branchlist(APIView):
    def get(self,request,ifsc):
        branch_ins = Branch.objects.filter(ifsc_code=ifsc)
        serializer = Branchserialzer(branch_ins,many=True)
        return Response(serializer.data)

def homepage(request):
    context = dict()
    context['bank'] = Bank.objects.all()
    context['city'] = City.objects.all()
    active = "bank"
    host_name = request.get_host()
    if request.method == 'POST':
        ifsc = request.POST.get('ifsc_code')
        bank_name = request.POST.get('b_name')
        city = request.POST.get('c_name')

        if ifsc is not None:

            url = f"http://{host_name}/branch/{ifsc}"
            data = requests.get(url)
            active = "ifsc"
            
        else:
            url = f"http://{host_name}/bank/{bank_name}/{city}"
            data = requests.get(url)
            active = "bank"
            
        
        context['data'] = data.json()
    context['active'] = active
    return render(request,'bankapp/homepage.html',context)
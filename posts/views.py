from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse

# Create your views here.
class HelloWorld(View):
    def get(self,request):
        data ={
            'name' : 'Jhonny Remolina',
            'age' : 45,
            'codes' : ['Python','Django','React']
        }
        return render(request,'hello_world.html', context=data)
from django.shortcuts import render
from django.views import View
from .models import Jobs
# Create your views here.
class Home(View):
    def get(self,request):
        q=Jobs.objects.all()
        con_dic={'records':q}
        return render(request,'home.html',context=con_dic)
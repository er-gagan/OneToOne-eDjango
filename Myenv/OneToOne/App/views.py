from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from .models import Singer,Song
# Create your views here.
def home(request):
    data = Song.objects.all()
    return render(request,'pages/home.html',{'data':data})

# @csrf_exempt
# def submit(request):
#     if request.method == 'POST':
#         Name = request.POST['Name']
#         Email = request.POST['Email']
#         Singer(Name = Name, Email = Email).save()
#         msg = "Singer data stored successfully"
#         return render(request,'pages/home.html',{'msg':msg})
#     else:
#         return HttpResponse("<h1>404 - Not Found</h1>")
from django.shortcuts import render
#from django.http import HttpResponse
# Create your views here.
#def male_learn(request):
 #   return HttpResponse("hello sis")

#def male_code(request):
 #   return HttpResponse("999")    

def version_typewrite(request):
    return render(request,'maleone.html')  
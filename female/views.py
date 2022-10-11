from django.shortcuts import render
 # from django.http import HttpResponse
# Create your views here.

# def female_learn(request):
  #  return HttpResponse("hello bro")

# def female_code(request):
  #  return HttpResponse("789")     

def learn_djangotype(request):
    return render(request,'femaleone.html')  
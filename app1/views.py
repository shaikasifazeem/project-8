from django.shortcuts import render
def sri(request):
    d={'Name':'shaik Asif','Age':21,'Mob':9398867596}
    return render(request,'sri.html',context=d)

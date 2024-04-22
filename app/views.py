from django.shortcuts import render, redirect
import ObjectMeasurement

def home(request):
    if request.method == 'POST':
        img = request.FILES['file']
        if img:
            ObjectMeasurement.start_process(img)
        else:
            return redirect('/start')
    return render(request, "home.html")

def start(request):
    ObjectMeasurement.start_process()
    return render(request, "start.html")

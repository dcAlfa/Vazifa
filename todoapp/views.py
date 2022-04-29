from django.shortcuts import render, redirect
from.models import *
def asosiy(request):
    return render(request, "Asosiy.html")
def student(request):
    if request.method=="POST":
        Student.objects.create(
            ism = request.POST.get('ismi'),
            yosh = request.POST.get('y'),
            kurs = request.POST.get('ismi'),
            s_raqam = request.POST.get('ismi')),
        return redirect("/studentlar/")

    soz = request.GET.get("qidirish")
    if soz==None or soz=="":
        S = Student.objects.filter().order_by('ism')
    else:
        S = Student.objects.filter(ism=soz)
    return render(request, "Studentlar.html", {"hammasi":S})
def project(request):
    P = Project.objects.all()
    return render(request, "Rejalar.html", {"hammasi":P})
def reja_o(request, son):
    Project.objects.get(id=son).delete()
    return redirect("/rejalar/")



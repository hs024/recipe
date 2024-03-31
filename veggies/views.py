from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def recipe(request):
    if request.method=="POST":
        data=request.POST
        name=data.get("name")
        description=data.get("description")
        # img=data.get("img")
        img=request.FILES.get("img")
        # print(data)
        # print(img)
        Recipe.objects.create(
            name=name,
            description=description,
            img=img
            )
        return redirect("/")
    queryset=Recipe.objects.all()

    if request.GET.get("search"):
        print(request.GET.get("search"))
        queryset=queryset.filter(name__icontains=request.GET.get("search"))
    context={"receipes":queryset}
    return render(request,"index.html",context=context)


def delete_ref(request,id):
    queryset=Recipe.objects.get(id=id)
    queryset.delete()
    return redirect("/")

def update_ref(request,id):
    queryset=Recipe.objects.get(id=id)
    if request.method=="POST":
        data=request.POST
        name=data.get("name")
        description=data.get("description")
        # img=data.get("img")
        img=request.FILES.get("img")
        queryset.name=name
        queryset.description=description
        if  img:
            queryset.img=img
        queryset.save()
        return redirect("/")
    context={"receipes":queryset}
    return render(request,"update.html",context=context)



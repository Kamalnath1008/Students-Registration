from django.shortcuts import render,redirect,HttpResponse
from students_app.models import Students
from students_app.forms import StudentsForm

# Create your views here.
def home(request):
    if request.method=="POST":
        form=StudentsForm(request.POST)
        a=request.POST.get('Email')
        b=request.POST.get('Password')
        if(a=="admin@gmail.com" and b=="12345"):
            return redirect("profile.html")
        elif a and b:
            form=Students.objects.all()
            for i in form:
                if i.Email==a and i.Password==b:
                    print(i.Email,i.Password)
                    form=Students.objects.get(id=i.id)
                    return render(request,'stdprofile.html',{'form':form})
            else:
                return HttpResponse("Plese Enter a valid mail and password")
    else:
        form=StudentsForm()
    return render(request,"home.html",{'form':form})
def register(request):
    if request.method=="POST":
        print('a')
        form=StudentsForm(request.POST,request.FILES)
        if form.is_valid():
            print("b")
            form.save()
            return redirect('/home')        
    else:
        form=StudentsForm()    
    return render(request,"register.html",{'form':form})
def profile(request):
    form=Students.objects.all()
    return render(request,"profile.html",{'form':form})
def stdprofile(request,id):
    form=Students.objects.get(id=id)
    return render(request,"stdprofile.html",{'form':form})
def delete(request,id):
    form=Students.objects.get(id=id)
    form.delete()
    return redirect("/profile")
def deleteall(request):
    form=Students.objects.all()
    form.delete()
    return HttpResponse("all data are sucessfuly deleted"),redirect('/profile')
def edit(request,id):
    form=Students.objects.get(id=id)
    if request.method=="POST":
        form=StudentsForm(request.POST,request.FILES,instance=form)
        if form.is_valid():
            form.save()
            return redirect('/profile')   
    else:
        form=StudentsForm(instance=form)
    return render(request,'edit.html',{'form':form})

# def edit(request,id):
#     instance=Students.objects.get(id=id)
#     context= {'instance': instance}
#     return render(request, 'edit.html',context)
# def update(request):
#     employee=Students.objects.get(id=id)
#     form=StudentsForm(request.POST,instance=employee)
#     if form.is_valid():
#         form.save()
#         return redirect('/Profile')   
#     return render(request,'edit.html',{'form':employee})



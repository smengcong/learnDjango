from django.shortcuts import render,redirect
from app02.forms import Form as tForm
from app02.models import User
# Create your views here.

def showData(request):
    obj_List = User.objects.all()
    return render(request, 'showData.html', {'obj_List': obj_List})

def form(request):
    if request.method=='GET':
        obj = tForm()
        return render(request, 'form.html', {'obj':obj})
    else:
        obj = tForm(request.POST)
        if obj.is_valid():
            print('验证成功', obj.cleaned_data)
            User.objects.create(**obj.cleaned_data)
            return redirect('/showData.html/')
        else:
            print('验证失败', obj.errors)
            return render(request, 'form.html', {'obj': obj})

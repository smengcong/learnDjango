from django.shortcuts import render,redirect,HttpResponse
from app02.forms import Form as tForm
from app02.models import User
# Create your views here.

def showData(request):
    print("视图")
    raise ValueError("报错了")
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

def mdindex(request):
    return HttpResponse("this is index")

def mdlogin(request):
    if request.method == 'POST':
        user = request.POST.get('name')
        pwd = request.POST.get('pwd')
        print(user,pwd)
        if user=='admin' and pwd =='123456':
            request.session['user'] = user
            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)
            else:
                return redirect('/mdindex/')
    else:
        obj = tForm()
        return render(request,'mdlogin.html',{'obj':obj})
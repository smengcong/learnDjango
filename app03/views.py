from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    if request.method=='GET':
        return render(request,'upload.html')
    else:
        name = request.POST.get('username')
        img = request.FILES.get('img')
        f = open(img.name,'wb')
        for line in img.chunks():
            f.write(line)
        f.close()
        return HttpResponse("上传成功")

def ajaxframe(request):
    if request.method=='GET':
        return render(request,'ajaxframe.html')
    else:
        print(request.GET)
        print(request.POST)
        print(request.FILES)
        return HttpResponse("....")
from django.shortcuts import render,HttpResponse,redirect
from django.db.models import Sum,Min,Count,Avg,Max,F,Q
from django.views import View

# Create your views here.
from app01.models import *

# 使用CBV方式进行返回 class base view
class index(View):
    def dispatch(self, request, *args, **kwargs):
        result = super(index,self).dispatch(request,*args, **kwargs)
        return result
    def get(self,request):
        return render(request,'index.html')

def addbook(req):
    # publish_obj = Publish.objects.get(name='汕头日报')
    # Book.objects.create(name='python',price=20.5,pub_date='2018-05-03',publish=publish_obj)

    # 正向查询
    # book = Book.objects.get(name='java')
    # print(book.name)
    # print(book.publish.name)
    # print(book.publish.city)

    # 逆向查询
    # 第一种方式
    # publish = Publish.objects.get(name='汕头日报')
    # ret = Book.objects.filter(publish=publish).values('name','price')
    # 第二种方式
    # publish = Publish.objects.get(name='汕头日报')
    # book_list = publish.book_set.all().values('name','price')
    # 第三种方式 善用__
    # book_list = Book.objects.filter(publish__name='汕头日报').values('name','price')

    # python这本书的出版社名称
    # publish = Book.objects.filter(name='python').values('publish__name')
    # publish = Publish.objects.filter(book__name='python').values('name')

    # 地方是北京 出版社出过的书
    # book_list = Book.objects.filter(publish__city='北京').values('name')
    # book_list = Publish.objects.filter(city='北京').values('book__name')

    # 多对多查询
    # book_list = Author.objects.get(name='smc').book_set.all().values('name')
    # book_list = Book.objects.filter(authors__age=24).values('name','authors__name')
    # 多对多添加
    # book_obj = Book.objects.get(name='django基础')
    # author_obj = Author.objects.all()
    # book_obj.authors.add(*author_obj)
    # 多对多删除
    # book_obj = Book.objects.get(name='django基础')
    # book_obj.authors.remove(2)  #对应的author主键id
    # 多对多查询 善用__ 找到zhousi写过的书
    # book_list = Book.objects.filter(authors__name='zhousi').values('name','price')

    # 聚合函数
    # result = Book.objects.all().aggregate(Max('price'))
    # 分组查询
    # result = Book.objects.values('authors__name').annotate(Sum(money='price'))
    # 每个出版社出版的最便宜的书价是多少
    # result = Book.objects.values('publish__name').annotate(money=Min('price'))
    # result = Publish.objects.values('name').annotate(Min('book__price'))
    # F查询
    # Book.objects.all().update(price=F('price')+10)
    # Q查询
    # book_list = Book.objects.filter(Q(name='java')|Q(price__gt=100))
    # print(book_list)


    book_list = Book.objects.all().iterator()
    return HttpResponse('添加成功')

def updatebook(req):
    # 第一种写法
    book = Book.objects.get(author='smc')
    book.price=999
    book.save()

    Book.objects.filter(author='smc').update(price=999) #1 第二种写法不能用save save的效率会低些
    return HttpResponse('修改成功')

def deletebook(req):
    Book.objects.get(author='smc').delete()
    return HttpResponse('删除成功')

def showbook(req):
    # book_list = Book.objects.all()
    # book_list = Book.objects.filter(name__contains='attack')
    # book_list = Book.objects.all().values('author','name')  可迭代对象的字典
    book_list = Book.objects.all().values_list('author','name') #可迭代对象的列表
    print(book_list)
    print(type(book_list))
    return render(req,'index.html',locals())

def login(req):
    if req.method=='POST':
        print(req.COOKIES)
        print(req.session)
        username = req.POST.get('username')
        password = req.POST.get('password')
        if username=='smc':
            req.session['username'] = username
            return redirect('/homepage.html/')
    return render(req,'login.html')

def homepage(req):
    username = req.session.get('username',None)
    if username:
        return render(req, 'homepage.html', locals())
    else:
        return redirect('/login.html')

def loout(req):
    del req.session['username']
    return HttpResponse("退出成功")

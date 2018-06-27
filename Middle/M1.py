
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse

class Md1(MiddlewareMixin):
    def process_request(self,request):
        print("this's Md1的process_request")

    def process_response(self,request,response):
        print("this's Md1的process_response")
        return response

    def process_view(self,request,view_func,view_args,view_kwargs):
        print('-'*80)
        print('Md1的process_view')
        print(view_func,view_func.__name__)

    def process_exception(self,request,exception):
        print(exception)
        print("Md1中的process_exception")
        return HttpResponse(str(exception))

class Md2(MiddlewareMixin):
    def process_request(self,request):
        print("this's Md2的process_request")

    def process_response(self,request,response):
        print("this's Md2的process_response")
        return response

    def process_view(self,request,view_func,view_args,view_kwargs):
        print('-'*80)
        print('Md2的process_view')
        print(view_func,view_func.__name__)

    def process_exception(self,request,exception):
        print(exception)
        print("Md2中的process_exception")

class AutoMd(MiddlewareMixin):
    whilte_List = ['/mdlogin',]
    black_List = ['/mdblack',]
    def process_request(self,request):
        from django.shortcuts import HttpResponse,redirect

        next_url = request.path_info
        print(next_url,request.get_full_path())

        if next_url in self.whilte_List or request.session.get('user'):
            return
        elif next_url in self.black_List:
            return HttpResponse("illegal URL")
        else:
            # return redirect('/mdlogin?next={}'.format(next_url))
            return

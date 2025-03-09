

# Create your views here.
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
def index(request):
    return HttpResponse('<h1>欢迎光临开平市第一中学</h1>')
def test(request):
    hi='大家好，欢迎来到开平一中'
    test='世界是美好的，这是一个动态测试页，显示正常，测试成功！！！'
    return render(request,'test.html',{'hi':hi,'test':test})
def login(request):
    if request.method=="GET":
        return render(request,"login.html")
    else:
        username=request.POST.get('username')
        password=request.POST.get('password')
        if (username=='test'and password=='123'):
            return redirect('/test/')
        else:
            return render(request,"login.html",{'error':'用户名或密码错误'})
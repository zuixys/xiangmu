from xiangmu import models
from django.db.models import Q
from django.shortcuts import render
from django.shortcuts import redirect
from xiangmu.models import Users, Gedan, Biaosheng, Rege, Xinge, Xindie,Infos,playlist

def index(request):
    uid = request.session.get('uid',None)
    if uid:
        name = Users.objects.filter(uid=uid)[0].username
    else:
        name = None
    gedan = Gedan.objects.all()
    biaosheng = Biaosheng.objects.all()
    xinge = Xinge.objects.all()
    rege = Rege.objects.all()
    xindie = Xindie.objects.all()
    return render(request,'index.html',locals())
from django.contrib import  messages#实现登录失败弹出警告

def ying(request):
    keywords = request.GET.get("keywords")
    if keywords:
        infos = Infos.objects.filter(Q(mname__contains=keywords)|Q(pname__contains=keywords))
    else:
        infos = Infos.objects.all()
    return render(request,'ying.html',{'infos':infos})
def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    unname = request.POST.get('unname')
    pwd = request.POST.get('pwd')
    result = Users.objects.filter(username=unname,userpwd=pwd)
    if result:
        request.session['uid'] = result[0].uid
        return redirect('/index/?name='+unname)
    elif Users.objects.filter(username=unname):
        messages.error(request,'密码错误')
        return render(request,'login.html')
    else:
        messages.error(request,'账号不存在')
        return render(request,'login.html')

def zhuce(request):
    if request.method == 'POST':
        unname = request.POST.get('unname')
        pwd = request.POST.get('pwd')
        psd = request.POST.get('psd')
        if pwd == psd:
            Users.objects.create(username=unname,userpwd=pwd)
            return redirect('/login/')
        else:
            messages.error(request,'两次密码不一致,请重新输入')
    return render(request,'zhuce.html')

def loginout(request):
    request.session.flush()
    return redirect('/index/')
def goodinfo(request):
    mname = request.GET.get('mname')
    if request.method=='POST':
        uid = request.session.get('uid', None)
        if uid:
            name = Users.objects.filter(uid=uid)[0].username
            gename = request.POST.get("gename")
            singname = request.POST.get('singname')
            zhuanname = request.POST.get('zhuanname')
            models.playlist.objects.create(gename=gename, singname=singname, zhuanname=zhuanname)
        else:
            name = None
    infos =Infos.objects.filter(mname=mname)
    return render(request, 'goodinfo.html', locals())

#数据库列出来
def playlists(request):
        queryset = models.playlist.objects.all()
        return render(request, 'playlist.html', {'queryset': queryset})

def add(request):
    if request.method=='GET':
        return render(request,'add.html')
    gename = request.POST.get("gename")
    singname=request.POST.get('singname')
    zhuanname=request.POST.get('zhuanname')
    models.playlist.objects.create(gename=gename,singname=singname,zhuanname=zhuanname)
    return redirect("http://127.0.0.1:8000/playlist/")

def delete(request):
    nid = request.GET.get("nid")
    # 2、删除
    models.playlist.objects.filter(id=nid).delete()
    # 3、重定向回到部门列表
    return redirect("/playlist")

from django.shortcuts import render,render_to_response,redirect
from django.shortcuts import HttpResponse,HttpResponseRedirect

from django import forms
from django.http import JsonResponse
from django.contrib.sessions.models import Session
import demjson
from random import choice
from BRS.models import BrsPerson,BookRank,Newbook
import NewBook
import myKNN
import word
import worm
import operator
import numpy
import kMeans
import myybayes

# Create your views here.
class RegisterForm(forms.Form):
    username=forms.CharField(max_length=30)
    password=forms.CharField(max_length=30)
    email=forms.EmailField()
    
class LoginForm(forms.Form):
    username=forms.CharField(max_length=30)
    password=forms.CharField(max_length=30)
       
def login(req):
    return render(req,'login.html')
    #print req.method
def loginVerify(request):
    #return JsonResponse({'res':request.POST.get('username')})
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        try:
            user=BrsPerson.objects.get(username=username)
            if(username=="111"):
                return JsonResponse({'res':2})
            if(user.password==password):
                request.session['username']=username
                return JsonResponse({'res':1})
            else:
                return JsonResponse({'res':0})
        except:
            return JsonResponse({'res':-1})
    return JsonResponse({'res':100})
        
def logout(request):
    try:
        del request.session['username']
    except KeyError:
        pass
    return redirect('/')            
    
def index(request):
    username=request.session.get('username')
    return render_to_response('brs001.html',{'username':username})

def inregister(request):
    return render(request,'register.html')

def register(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        email=request.POST.get('email')
        filterResult=BrsPerson.objects.filter(username=username)
        if(len(filterResult)>0):
            return JsonResponse({'res':1})
        else:
            user=BrsPerson.objects.create(username=username,email=email,password=password)
            user.save()
            return JsonResponse({'res':0})
    return JsonResponse({'res':100})
                
def getlist1(request):
    listString=[]
    listpo={}
    animated=["fadeInRight","fadeInDownBig","rotateInDownLeft","bounceIn","bounceInLeft","fadeInRightBig","flipInx","rollIn","fadeInUpBig","flipInY"]
    picture=["../static/image/a0.jpg","../static/image/a1.jpg","../static/image/a2.jpg","../static/image/a3.jpg","../static/image/a4.jpg","../static/image/a5.jpg",
             "../static/image/a6.jpg","../static/image/a7.jpg","../static/image/a8.jpg","../static/image/a9.jpg"]
    booknames=BookRank.objects.all().values_list('name')
    bookhrefs=BookRank.objects.all().values_list('href')
    booktypes=BookRank.objects.all().values_list('type')
    bookwriter=BookRank.objects.all().values_list('writer')
    sums=BookRank.objects.filter().count()
    #print(str(sums)+"总数")
    for i in range(sums):
        listpo = {"src":choice(picture),"name":booknames[i][0],"author":bookwriter[i][0],"type":booktypes[i][0],"animated":animated[i%10],"href":bookhrefs[i][0]}
        listString.append(listpo)        
    json = demjson.encode(listString)
    return HttpResponse(json,content_type="application/json")
   

def mybayes(req):
    return render(req,'bayes.html')
def kmeans(req):
    return render(req,'kmeans.html')
def knn(req):
    return render(req,'knn.html')

def recommend(req):
    return render(req,'recommend.html')

def projects(req):
    return render(req,'projects.html')

def query_KNN(req):#用书名搜索将书存进newbook中
    if req.method=='POST':
        print("post")
        bookname=req.POST.get('bookna')
        print(bookname)
        book=NewBook.search(bookname)
        url="https:"+book["href"]
        print(url)
        NewBook.searchBookInfo(url)
        NewBook.searchKeywords()#将keywords存入newbook表中  
        recommend=[]
        group,labels=word.getArrays()
        newbook=NewBook.getArray()
        rankArray=numpy.array(group)
        for j in range(len(myKNN.classify(newbook, rankArray, labels, 3))):
            BookName=myKNN.classify(newbook,rankArray,labels,3)[j]
            book=BookRank.objects.get(name=BookName)
            dictR = {}
            dictR['name'] = book.name
            dictR['href'] = book.href
            dictR['writer'] = book.writer
            recommend.append(dictR)
        print(recommend)       
        json = demjson.encode(recommend)
        return HttpResponse(json,content_type="application/json")
    
def bayesrecommend(req):
    return render(req,'bayesrecommend.html')

def adminbooks(req):
    return render(req,'adminbooks.html')

def adminshowbook(req):
    listString=[]
    listpo={}
    booknames=BookRank.objects.all().values_list('name')
    bookhrefs=BookRank.objects.all().values_list('href')
    booktypes=BookRank.objects.all().values_list('type')
    bookwriter=BookRank.objects.all().values_list('writer')
    sums=BookRank.objects.filter().count()
    for i in range(sums):
        listpo = {"name":booknames[i][0],"author":bookwriter[i][0],"type":booktypes[i][0],"href":bookhrefs[i][0]}
        listString.append(listpo)
    return render_to_response('adminbooks.html',{"listString":listString})


def kMeansfunction(request):
        kMeans.mainKMeans()
        listString=[]
        listpo={}
        booknames=BookRank.objects.all().values_list('name')
        bookhrefs=BookRank.objects.all().values_list('href')
        booktypes=BookRank.objects.all().values_list('type')
        bookwriter=BookRank.objects.all().values_list('writer')
        sums=BookRank.objects.filter().count()
        print(str(sums)+"总数")
        for i in range(sums):
            listpo = {"name":booknames[i][0],"author":bookwriter[i][0],"type":booktypes[i][0],"href":bookhrefs[i][0]}
            listString.append(listpo)        
        json = demjson.encode(listString)
        return HttpResponse(json,content_type="application/json")
    
def bayesfunction(request):
    if request.method=='POST':
        bookname=request.POST.get('bookna')
        print(bookname)
        book=NewBook.search(bookname)
        url="https:"+book["href"]
        print(url)
        NewBook.searchBookInfo(url)
        NewBook.searchKeywords()#将keywords存入newbook表中
        recommend=[]
        listpo={}
        listString=[]
        recommend=myybayes.mainBayes()
        #print("贝叶斯"+recommend)
        for i in range(len(recommend)):
            bookname=BookRank.objects.get(name=recommend[i])
            print(bookname)
            listpo = {"name":bookname.name,"author":bookname.writer,"type":bookname.type,"href":bookname.href}
            listString.append(listpo)
        json = demjson.encode(listString)
        return HttpResponse(json,content_type="application/json")
    
        
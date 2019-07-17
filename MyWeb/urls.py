"""MyWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from BRS import views

urlpatterns = [
        #登录
    url(r'^$',views.login,name='login'),
    url(r'^login/$',views.loginVerify,name='loginVerify'),
    #注册
    url(r'^register_show/$',views.inregister,name='show_register'),
    url(r'^register/$',views.register,name='register'),
    url(r'^index/$',views.index,name='index'),
    url(r'^bayes/$',views.mybayes,name='bayes'),
    url(r'^kmeans/$',views.kmeans,name='kmeans'),
    url(r'^knn/$',views.knn,name='knn'),
    url(r'^recommend/$',views.recommend,name='recommend'),
    url(r'^logout/$',views.logout,name='logout'),
    url(r'^showinfo/$',views.query_KNN,name='showinfo'),
    url(r'^bayesrecommend/$',views.bayesrecommend,name='bayesrecommend'),
    url(r'^adminbooks/$',views.adminbooks,name='adminbooks'),
    url(r'^kMeansfunction/$',views.kMeansfunction,name='kMeansfunction'),
    url(r'^projects/$',views.projects,name='projects'),
    url(r'^bayesfunction/$',views.bayesfunction,name='bayesfunction'),
    url(r'^admin/', admin.site.urls),
    url(r'^getlist1/$',views.getlist1)
]

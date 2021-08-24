"""ProjectList URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
#from django.urls import path
from django.conf.urls import url
from BMIList import views
from django.conf.urls.static import static


urlpatterns = [
    url(r'^bmi/mhome$', views.mhome, name='mhome'),
    url(r'^$', views.LogIn, name='login'),
    url(r'^bmi/new$', views.new, name='new'),
    url(r'^bmi/signup$', views.SignUpp, name='signup'),
    url(r'^bmi/(\d+)/viewdata/$', views.viewdata, name='viewdata'),
    url(r'^bmi/(\d+)/addData$', views.AddDataBmi, name='adddata'),
    url(r'^bmi/(\d+)/historypage/$', views.HistoryPage, name='historypage'),#OK
    url(r'^bmi/(\d+)/viewdata/updatedon/$', views.UpdateHis, name='updatehis'),
    url(r'^bmi/(\d+)/viewdata/updatedon/datachange/(?P<id>\d+)$', views.DataChange, name='datachange'), 
    url(r'^bmi/(\d+)/historypage/deletedon/(?P<id>\d+)$', views.DeleteDon, name='deletedon'),
    url(r'^bmi/(\d+)/benefitpage/$', views.BenefitPage, name='benefitpage'),
    url(r'^bmi/(\d+)/fitpage/$', views.FitPage, name='fitpage'), 
    url(r'^bmi/(\d+)/aboutpage/$', views.AboutPage, name='aboutpage'),
    url(r'^bmi/(\d+)/addrate$', views.AddRate, name='addrate'),

#    url(r'^section1$', views.section1, name='section1'),#OK
 #   url(r'^section2$', views.section2, name='section2'),#OK
  #  url(r'^section3$', views.section3, name='section3'),#OK
#    url(r'^section4$', views.section4, name='section4'),#OK


#    url(r'^bmi/(\d+)/userpage/updatedon/(?P<id>\d+)$', views.UInfo, name='uinfo'),
#    url(r'^bmi/(\d+)/userpage/updatedon/upinfo/(?P<id>\d+)$', views.UpInfo, name='upinfo'),
#   url(r'^bmi/(\d+)/updateData$', views.UpDateDataBmi, name='updatedata'),
#    path('delete/<int:id>', views.delete),
#    url(r'^ProjectList/index$', views.Indexate, name='index'),
#    url(r'^ProjectList/peach$', views.Peachy, name='peach'),
#    url(r'^ProjectList/bmi$', views.BMI, name='bmi'),
    url('admin/',admin.site.urls),
    
#    url(r'^BMIList/(\d+)/$', views.ViewList, name='mgm'),
#    url(r'^BMIList/mgm2_url$', views.NewList, name='Newlist'),
#    url(r'^BMIList/(\d+)/addItem$', views.AddItem, name='additem'),
    #path('admin/', admin.site.urls),
]

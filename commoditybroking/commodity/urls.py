from django.conf.urls import url,include
from django.contrib import admin
from commodity.views import HomeView,CreationView,PageView,SeaView,MessageView,ImadminView,SpiceView,CashewView,BuyView,BuyorsellView,SellView,UserListView,SellListView,BuyListView
from commodity import views

urlpatterns = [
    url(r'^home/',HomeView.as_view(),name="home"),
    url(r'^create/',CreationView.as_view(),name="create"),
    url(r'^page/',PageView.as_view(),name="page"),
    url(r'^seafood/',SeaView.as_view(),name="seafood"),
    url(r'^imadmin/',ImadminView.as_view(),name="imadmin"),
    url(r'^login/$', views.login, name='login'),
    url(r'^spices/',SpiceView.as_view(),name="spices"),
    url(r'^cashews/',CashewView.as_view(),name="cashews"),
    url(r'^buyorsell/',BuyorsellView.as_view(),name="buyorsell"),
    
    url(r'^buy/',BuyView.as_view(),name="buy"),
  

    url(r'^sell/',SellView.as_view(),name="sell"),
    url(r'^list/',UserListView.as_view(),name="list"),
    url(r'^sellist/',SellListView.as_view(),name="sellist"),
    url(r'^buylist/',BuyListView.as_view(),name="buylist"),
    url(r'^message/',MessageView.as_view(),name="message"),
    url(r'', include('django.contrib.auth.urls')),

#from django.conf.urls import url
#from commodity import views

    url(r'^payment/$', views.payment, name="payment"),
    url(r'^payment/success$', views.payment_success, name="payment_success"),
    url(r'^payment/failure$', views.payment_failure, name="payment_failure"),
]

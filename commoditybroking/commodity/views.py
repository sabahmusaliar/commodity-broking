# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.contrib import messages
import logging, traceback
import commodity.constants as constants
import commodity.config as config
import hashlib
import requests
from random import randint
from django.views.decorators.csrf import csrf_exempt




from django.shortcuts import render,redirect
from django.views.generic import TemplateView,ListView,CreateView,View
from django.views.generic import FormView
from django.contrib.auth.models import User
from commodity.forms import UserForm,CustomerForm,BuyForm,SellForm
from commodity.forms import Customer,Buy,Sell
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from commodity.models import Customer,Buy,Sell
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.contrib.auth.decorators import user_passes_test


import urllib
import urllib2
import json

from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages

from commodity.models import Customer
from .forms import CustomerForm

# Create your views here.

class HomeView(TemplateView):
	template_name="home.html"
class PageView(TemplateView):
	template_name="page1.html"
class SeaView(TemplateView):
	template_name="seafood.html"
class ImadminView(TemplateView):
	template_name="imadmin.html"
class SpiceView(TemplateView):
	template_name="spices.html"
class CashewView(TemplateView):
	template_name="cashews.html"
class BuyorsellView(TemplateView):
	template_name="buyorsell.html"
class MessageView(TemplateView):
	template_name="message.html"

@login_required
def home(request):
    return render(request, 'core/home.html')


class BuyView(CreateView):
	template_name="buy.html"
	form_class=BuyForm
	model=Buy
	success_url='/payment'


class BuyListView(ListView):
	model=Buy
	template_name="buylist.html"
	

class SellView(CreateView):
	template_name="sell.html"
	form_class=SellForm
	model=Sell
	success_url='success'



class SellListView(ListView):
	model=Sell
	template_name="selllist.html"
	


class UserListView(ListView):
	model=Customer
	template_name="userlist.html"
	context_object_name="customer_list"






class CreationView(FormView):
	template_name="create.html"
	form_class=UserForm
	model=Customer

	def get(self, request, *args, **kwargs):
		self.object=None
		form_class=self.get_form_class()
		user_form = self.get_form(form_class)
		cust_form=CustomerForm()
		return self.render_to_response(self.get_context_data
		(form1=user_form,form2=cust_form))


	def post(self, request, *args, **kwargs):
		self.object=None
		form_class=self.get_form_class()
		user_form = self.get_form(form_class)
		cust_form=CustomerForm(self.request.POST,self.request.FILES)
		if(user_form.is_valid() and cust_form.is_valid()):
			return self.form_valid(user_form,cust_form)
		else:
			return self.form_invalid(user_form,cust_form)

	def form_valid(self, user_form, cust_form):
		self.object = user_form.save()
		self.object.is_staff=True
		self.object.save()
		p = cust_form.save(commit=False)
		p.user = self.object
		p.save()

	def form_invalid(self, user_form, cust_form):
		return self.render_to_response(self.get_context_data(form1=user_form,form2=cust_form))


def login(request):
     form =AuthenticationForm()
     if request.user.is_authenticated():
         if request.user.is_superuser:
             return redirect("/imadmin/")# or your url name
         if request.user.is_staff:
             return redirect("/home/")# or your url name


     if request.method == 'POST':
         username = request.POST.get('username')
         password = request.POST.get('password')
         user = auth.authenticate(username=username, password=password)

         if user is not None:
             # correct username and password login the user
             auth.login(request, user)
             if request.user.is_superuser:
                 return redirect("/imadmin/")# or your url name
             if request.user.is_staff:
                 return redirect("/buyorsell/")# or your url name

         else:
             messages.error(request, 'Error wrong username/password')
     context = {}
     context['form']=form

     return render(request, 'login.html', context)

@user_passes_test(lambda u: u.is_staff)
def StaffHome(request):
     context = {}
     return render(request, 'buyorsell.html', context)

@user_passes_test(lambda u: u.is_superuser)
def AdminHome(request):
     context = {}
     return render(request, 'imadmin.html', context)




def payment(request):   
    data = {}
    txnid = get_transaction_id()
    hash_ = generate_hash(request, txnid)
    hash_string = get_hash_string(request, txnid)
    # use constants file to store constant values.
    # use test URL for testing
    data["action"] = constants.PAYMENT_URL_LIVE 
    data["amount"] = float(constants.PAID_FEE_AMOUNT)
    data["productinfo"]  = constants.PAID_FEE_PRODUCT_INFO
    data["key"] = config.KEY
    data["txnid"] = txnid
    data["hash"] = hash_
    data["hash_string"] = hash_string
    
    data["service_provider"] = constants.SERVICE_PROVIDER
    data["furl"] = request.build_absolute_uri(reverse("payment_failure"))
    data["surl"] = request.build_absolute_uri(reverse("payment_success"))
    
    return render(request, "payment.html", data)        
    
# generate the hash
def generate_hash(request, txnid):
    try:
        # get keys and SALT from dashboard once account is created.
        # hashSequence = "key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|udf6|udf7|udf8|udf9|udf10"
        hash_string = get_hash_string(request,txnid)
        generated_hash = hashlib.sha512(hash_string.encode('utf-8')).hexdigest().lower()
        return generated_hash
    except Exception as e:
        # log the error here.
        logging.getLogger("error_logger").error(traceback.format_exc())
        return None

# create hash string using all the fields
def get_hash_string(request, txnid):
    hash_string = config.KEY+"|"+txnid+"|"+str(float(constants.PAID_FEE_AMOUNT))+"|"+constants.PAID_FEE_PRODUCT_INFO+"|"
   
    hash_string += "||||||||||"+config.SALT

    return hash_string

# generate a random transaction Id.
def get_transaction_id():
    hash_object = hashlib.sha256(str(randint(0,9999)).encode("utf-8"))
    # take approprite length
    txnid = hash_object.hexdigest().lower()[0:32]
    return txnid

# no csrf token require to go to Success page. 
# This page displays the success/confirmation message to user indicating the completion of transaction.
@csrf_exempt
def payment_success(request):
    data = {}
    return render(request, "success.html", data)

# no csrf token require to go to Failure page. This page displays the message and reason of failure.
@csrf_exempt
def payment_failure(request):
    data = {}
    return render(request, "failure.html", data)









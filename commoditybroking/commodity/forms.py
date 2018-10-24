from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from commodity.models import Customer,Buy,Sell

class UserForm(UserCreationForm):
	class Meta():
		
		model=User
		fields=['username','email','first_name','last_name']
class CustomerForm(forms.ModelForm):
	class Meta():
		
		model=Customer
		fields=['phone','adress']


class BuyForm(forms.ModelForm):
	class Meta():
		model=Buy
		fields=['user','product_details','quantity']


		
class SellForm(forms.ModelForm):
	class Meta():
		model=Sell
		fields=['user','product_details','quantity','price']




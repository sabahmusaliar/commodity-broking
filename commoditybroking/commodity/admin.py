# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from commodity.models import Customer,Buy,Sell


# Register your models here.
admin.site.register(Customer)
admin.site.register(Buy)
admin.site.register(Sell)

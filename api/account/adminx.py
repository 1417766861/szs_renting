#encoding:utf-8

import xadmin
from .models import AccountModel

class AccountAdmin(object):
    list_display = ['nickname', 'gender', 'status', 'create_time']
    search_fields = ['nickname', 'gender', 'status']
    list_filter = ['nickname', 'gender', 'status', 'create_time']
    model_icon = 'fa fa-info-circle'


xadmin.site.register(AccountModel, AccountAdmin)

import xadmin
from apps.detail.models import SellerModel

# 注册UserProfile 进后台admin
class SellerAdmin(object):
    pass

xadmin.site.register(SellerModel,SellerAdmin)

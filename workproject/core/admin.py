from django.contrib import admin
from core.models import Concert,TargetInfo,QticketsSalesInfo
# Register your models here.

admin.site.register(Concert)
admin.site.register(TargetInfo)
admin.site.register(QticketsSalesInfo)
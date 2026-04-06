from django.contrib import admin
from .models import notificated,notifications,driver_tax_lagacy, persone_salary, category,driver_tax,tabel_group,dayapprove,dayapproved,persone, period, tabel_list, temp_file, objs,ender_list , group, driver_list,driver, automobile,agreement, agreement_step,accepter_list,agreementer_list,agreement_accepter

# Register your models here
admin.site.register(category)
admin.site.register(agreement)
admin.site.register(ender_list)
admin.site.register(temp_file)
admin.site.register(accepter_list)
admin.site.register(agreementer_list)
admin.site.register(agreement_step)
admin.site.register(agreement_accepter)
admin.site.register(period)
admin.site.register(tabel_list)
admin.site.register(driver)
admin.site.register(driver_list)
admin.site.register(objs)
admin.site.register(automobile)
admin.site.register(group)
admin.site.register(persone)
admin.site.register(dayapprove)
admin.site.register(dayapproved)
admin.site.register(tabel_group)
admin.site.register(driver_tax)
admin.site.register(driver_tax_lagacy)
admin.site.register(persone_salary)
admin.site.register(notificated)
admin.site.register(notifications)



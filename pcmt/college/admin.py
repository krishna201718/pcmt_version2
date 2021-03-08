from django.contrib import admin
from .models import Account,Subject,Admission, Student


# Register your models here.
class adminAccount(admin.ModelAdmin):
    fields = (('first_name','last_name'),('email','password'),('phone','image'),
              ('department','recovery_email'),'is_superuser','is_admin','is_staff','is_HOD','is_BOC','is_teacher')

class adminAdmission(admin.ModelAdmin):
    exclude = ['student_data']
admin.site.register(Account,adminAccount)
admin.site.register(Subject)
admin.site.register(Admission, adminAdmission)

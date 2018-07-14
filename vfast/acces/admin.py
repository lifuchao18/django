from django.contrib import admin

# Register your models here.
from acces.models import Students

class StudentAdmin(admin.ModelAdmin):
    list_display = ['name','age','gender','mobile','height','weight']
admin.site.register(Students,StudentAdmin)
#admin.site.register(Parents)

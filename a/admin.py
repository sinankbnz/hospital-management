from django.contrib import admin
from.models import Doctors, Departments, Booking, Message

class DoctorsAdmin(admin.ModelAdmin):
    list_display=('doc_name','doc_spec','doc_department') 
class DepartmentsAdmin(admin.ModelAdmin):
    list_display=('dep_name','dep_description')
class BookingAdmin(admin.ModelAdmin):
    list_display=('p_name','doc_name','booking_date')
class MessageAdmin(admin.ModelAdmin):
    list_display=('name','email','message')

admin.site.register(Departments,DepartmentsAdmin)
admin.site.register(Doctors,DoctorsAdmin)
admin.site.register(Booking,BookingAdmin)
admin.site.register(Message,MessageAdmin)


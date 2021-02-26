from django.contrib import admin
from main.models import PhonebookItem

class PhonebookItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number')


admin.site.register(PhonebookItem, PhonebookItemAdmin)
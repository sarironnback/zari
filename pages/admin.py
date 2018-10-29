from django.contrib import admin
from pages.models import About, Contact, Creation

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('sent_at', 'email', 'message')


admin.site.register(About)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Creation)

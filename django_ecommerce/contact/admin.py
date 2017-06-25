from django.contrib import admin
from .models import ContactForm

class ContactFormAdmin(admin.ModelAdmin):
	class Meta:
		models = ContactForm 


admin.site.register(ContactForm, ContactFormAdmin)
# Register your models here.

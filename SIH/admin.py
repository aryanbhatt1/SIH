from django.contrib import admin
from .models import *
from .forms import *

admin.site.register(Gender)
# Register your models here.
class FormAdmin(admin.ModelAdmin):
    form = AdmissionForm


admin.site.register(Form, FormAdmin)

admin.site.register(info_team)
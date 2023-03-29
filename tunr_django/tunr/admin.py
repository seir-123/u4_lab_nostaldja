from django.contrib import admin

# Register your models here.
from.models import Fad
from.models import Decade

admin.site.register(Decade)
admin.site.register(Fad)
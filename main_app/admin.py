from django.contrib import admin

# Register your models here.
from .models import Work_places, Learning_places, Hobbies, Persons, Sex, Politic


admin.site.register(Work_places)
admin.site.register(Learning_places)
admin.site.register(Hobbies)
admin.site.register(Persons)
admin.site.register(Sex)
admin.site.register(Politic)

from django.contrib import admin

# Register your models here.
from .models import workplaces, learningplaces, hobbies, person


admin.site.register(workplaces)
admin.site.register(learningplaces)
admin.site.register(hobbies)
admin.site.register(person)
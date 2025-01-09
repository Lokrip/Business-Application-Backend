from django.contrib import admin

from .models import (

    Service, 

    Plan, 

    Subsription

)



admin.site.register(Service)

admin.site.register(Plan)

admin.site.register(Subsription)

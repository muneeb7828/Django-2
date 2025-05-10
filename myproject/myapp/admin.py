from django.contrib import admin

# Register your models here.

from .models import *             # isme models me jitni bhi class he jab agai

admin.site.register(Course)       # isse database ko register kar sakte he





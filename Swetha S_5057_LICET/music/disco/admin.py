from django.contrib import admin
from .models import category
from .models import songs
# Register your models here.
class categoryAdmin(admin.ModelAdmin):
    list_display=('name','image','description')
admin.site.register(category,categoryAdmin)
admin.site.register(songs)
from django.contrib import admin
from menu.models import Menu

# Register your models here.
#admin.site.register(Menu)

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name','make_on','category','price','cover_image')
    list_filter=("category",)
    date_hierarchy= ("make_on")
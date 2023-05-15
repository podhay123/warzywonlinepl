from django.contrib import admin
from main.models import *
from .models import Product
from django.contrib.auth.admin import UserAdmin

admin.site.register([Category, Opinion, ProductToSell])


class ProfileInLine(admin.StackedInline):
    model = Profile
    can_delete = False


class AccountsUserAdmin(UserAdmin):
    inlines = [ProfileInLine]


admin.site.unregister(User)
admin.site.register(User, AccountsUserAdmin)



class ProductAdmin(admin.ModelAdmin):
  list_display = ("name",)
  prepopulated_fields = {"slug": ("name", )}
  
admin.site.register(Product, ProductAdmin)
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from.models import *




class AccountAdmin(BaseUserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_seller', 'is_buyer', 'is_active', 'is_staff')
    list_filter = ('is_seller', 'is_buyer', 'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'phone_number', 'address')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superadmin', 'is_seller', 'is_buyer',)}),
        ('Important dates', {'fields': ('last_login','date_joined'), 'classes': ('collapse',)}),
    )
    readonly_fields = ('date_joined', 'last_login')
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)
    filter_horizontal = ()
    
    
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'email', 'phone_number', 'query')
    fieldsets = (
        (None, {'fields': ('first_name', 'email', 'phone_number', 'query')}),
    )    




class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'available', 'created_at']
    list_filter = ['available', 'created_at']
    list_editable = ['price', 'stock', 'available']
    
    prepopulated_fields = {'description': ('name',)}
    search_fields = ['name', 'description']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'author', 'text', 'created_at')
    list_filter = ('created_at', 'author')
    search_fields = ('text', 'product__name')



admin.site.register(Account, AccountAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(ContactUs, ContactUsAdmin)


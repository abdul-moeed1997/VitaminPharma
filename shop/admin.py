from django.contrib import admin
from django.contrib.auth.admin import Group
from  .models import Product, Order, OrderUpdate, Contact

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','city','phone','email','delivered')
    list_editable = ('delivered',)
    search_fields =('city','id')
    list_per_page = 10

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','gender_catagory','price','expire_date')
    list_editable = ('price',)
    search_fields = ('name','gender_catagory','price','expire_date','catagory')
    list_filter = ('gender_catagory','expire_date')

class UpdateAdmin(admin.ModelAdmin):
    list_display = ('order_id','update_desc','timestamp')
    list_editable = ('update_desc',)
    list_filter = ('update_desc','timestamp')
    search_fields = ('order_id','update_desc')

admin.site.unregister(Group)

admin.site.register(Product,ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderUpdate, UpdateAdmin)
admin.site.register(Contact)


from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem

    readonly_fields = ('lineitem_total',)

 #   if OrderLineItem.product_size == 'null':
  #      fields = ('kicks', 'product_size', 'quantity', 'lineitem_total',)
  #  else:
  #      fields = ('accessory', 'quantity', 'lineitem_total',)

  #  def get_fields(self, request, product_size):
   #     if product_size:
    #        fields = ('accessory', 'quantity', 'lineitem_total',)
     #   else:
      #      fields = ('kicks', 'product_size', 'quantity', 'lineitem_total',)    


    #if product_size:
   #     fields = ('kicks', 'product_size', 'quantity', 'lineitem_total',)
 ##   else:
 #       fields = ('accessory', 'quantity', 'lineitem_total',)

    #readonly_fields = ('lineitem_total',)

#class OrderLineItemAdmin(admin.ModelAdmin):

 #   fields = ('order', 'kicks',
 #               'accessory', 'product_size',
 #               'quantity',)
    
 #   readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'grand_total',)

    fields = ('order_number', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'delivery_cost',
              'order_total', 'grand_total',)

    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'delivery_cost',
                    'grand_total',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)

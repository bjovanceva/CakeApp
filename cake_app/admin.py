from django.contrib import admin

from cake_app.models import Cake, Baker

# Register your models here.
class CakeAdmin(admin.ModelAdmin):

    def has_change_permission(self, request, obj=None):
        if obj and request.user==obj.baker.user:
            return True
        return False

    def has_view_permission(self, request, obj=None):
        return True

    def save_model(self, request, obj, form, change):
        if obj:
           if Cake.objects.filter(name=obj.name).exists():
              return False

           baker_cakes=Cake.objects.filter(baker=obj.baker).all()
           if not change and baker_cakes.count()==10:
               return False

           total_price=0
           for cake in baker_cakes:
               total_price+=cake.price

           if change:
               cake_to_edit=baker_cakes.filter(name=obj.name).first()
               total_price-=cake_to_edit.price

               if total_price+obj.price>10000:
                   return False

           else:
               if total_price+obj.price>10000:
                   return False

           super(CakeAdmin, self).save_model(request, obj, form, change)


class BakerAdmin(admin.ModelAdmin):

    def has_delete_permission(self, request, obj=None):
        if obj and request.user.is_superuser:
            return True
        return False

    def has_change_permission(self, request, obj=None):
        if obj and request.user.is_superuser:
            return True
        return False

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        return False

admin.site.register(Cake, CakeAdmin)
admin.site.register(Baker, BakerAdmin)

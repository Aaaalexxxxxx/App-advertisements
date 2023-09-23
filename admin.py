from django.contrib import admin
from .models import Advertisement

# Register your models here.
class AdvertisementAdmin(admin.ModelAdmin):
    #заглущка
    #pass
    list_display = ['id', 'title', 'description', 'price', 'created_at', 'updated_at', 'auction','image']
    list_filter = ['auction', 'created_at']
    actions = ['make_auction_as_false', 'make_auction_as_true']
    fieldsets = (
        ('Общее', {
            'fields': ('title', 'description','image','user')
        }),

        ('Финансы', {
            'fields': ('price', 'auction'), 
            'classes':['collapse']
        })
    )

    @admin.action(description='убрать возможность торга')
    def make_auction_as_false(self, request, queryset):
        queryset.update(auction=False)

    @admin.action(description='добавить возможность торга')
    def make_auction_as_true(self, request, queryset):
        queryset.update(auction=True)

#создаем представление класса внутри админки
admin.site.register(Advertisement, AdvertisementAdmin)
from django.contrib import admin

# Register your models here.
from rango.models import Category, Page
from rango.models import UserProfile

admin.site.register(UserProfile)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')
    exclude = ('user',)

    def save_model(self, request, obj, form, change):
        '''set user == request.user(admin)'''
        if not change:
            obj.user = request.user

        return super(PageAdmin, self).save_model(request, obj, form, change)


admin.site.register(Page, PageAdmin)

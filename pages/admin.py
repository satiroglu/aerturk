from django.contrib import admin
from .models import Page


# Page Admin
class PageAdmin(admin.ModelAdmin):

    # Page Actions
    @admin.action(description="Seçili sayfaları yayınla")
    def make_page_published(modeladmin, request, queryset):
        queryset.update(status='1')

    @admin.action(description="Seçili sayfaları taslak yap")
    def make_page_draft(modeladmin, request, queryset):
        queryset.update(status='0')

    list_display = ('id', 'title', 'slug', 'createdOn', 'updatedOn', 'status')
    list_filter = ('status',)
    list_display_links = ['id', 'title']
    ordering = ['id']
    search_fields = ['title', 'content', 'slug']
    prepopulated_fields = {'slug': ('title',)}
    # list_editable = ['status']
    list_per_page = 20
    # Special Actions
    actions = [make_page_published, make_page_draft]


admin.site.register(Page, PageAdmin)
from django.contrib import admin
from .models import Post, Category, Comment


# Posts Admin
class PostAdmin(admin.ModelAdmin):

    # Posts Actions
    @admin.action(description="Seçili yazıları yayınla")
    def make_post_published(modeladmin, request, queryset):
        queryset.update(status='1')

    @admin.action(description="Seçili yazıları taslak yap")
    def make_post_draft(modeladmin, request, queryset):
        queryset.update(status='0')

    list_display = ('id', 'title', 'category', 'author', 'createdOn', 'updatedOn', 'status')
    list_filter = ('status','author')
    list_display_links = ['id', 'title']
    ordering = ['id']
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    # list_editable = ['status']
    list_per_page = 20
    # special actions
    actions = [make_post_published, make_post_draft]


admin.site.register(Post, PostAdmin)


# Category Admin
class CategoryAdmin(admin.ModelAdmin):

    # Category Actions
    @admin.action(description="Seçili kategorileri yayınla")
    def make_category_published(modeladmin, request, queryset):
        queryset.update(status='1')

    @admin.action(description="Seçili kategorileri taslak yap")
    def make_category_draft(modeladmin, request, queryset):
        queryset.update(status='0')

    list_display = ('id', 'name', 'description', 'createdOn', 'updatedOn', 'status')
    list_display_links = ['id', 'name']
    list_filter = ['status']
    ordering = ['id']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('name',)}
    # list_editable = ['status']
    list_per_page = 20
    # special actions
    actions = [make_category_published, make_category_draft]


admin.site.register(Category, CategoryAdmin)


# Comment Admin
class CommentAdmin(admin.ModelAdmin):

    # Comment Actions
    @admin.action(description="Seçili yorumları onayla")
    def make_comment_published(modeladmin, request, queryset):
        queryset.update(status='1')

    @admin.action(description="Seçili yorumların onayını kaldır")
    def make_comment_draft(modeladmin, request, queryset):
        queryset.update(status='0')

    list_display = ('id', 'post', 'author', 'email', 'createdOn', 'status')
    list_display_links = ['id', 'post', 'author']
    list_filter = ['status']
    ordering = ['id']
    search_fields = ['post', 'email', 'author', 'comment']
    prepopulated_fields = {'author': ('author',)}
    # list_editable = ['status']
    list_per_page = 20
    # special actions
    actions = [make_comment_published, make_comment_draft]


admin.site.register(Comment, CommentAdmin)

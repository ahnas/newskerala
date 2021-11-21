from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .forms import NewsForm
from .models import (About, Announcement, BreakingNews, Category, Comment,
                     Contact, News, Newsletter, Photo, Reporter, Social, WhatsappGroup)


class NewsResource(resources.ModelResource):
    class Meta:
        model = News

class NewsAdmin(ImportExportModelAdmin):
    form = NewsForm
    resource_class = NewsResource
    list_display = ('title','view_link','category','display_time','published','view_count')
    list_filter = ('reporter','display_time','published','popular','hot_post','category')
    ordering = ('-display_time',)
    readonly_fields = ()
    search_fields = ('title', 'location','reporter__name')
    autocomplete_fields = ('reporter','category')

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title','image','published')

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title','news_count',)
    search_fields = ('title',)

class ReporterAdmin(admin.ModelAdmin):
    search_fields = ('name',)

class BreakingNewsAdmin(admin.ModelAdmin):
    ordering = ('-time',)
    autocomplete_fields = ('category',)
    list_display = ('category','title')

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email','phone','subject')
    readonly_fields = ('name','email','phone','subject','message')

class CommentAdmin(admin.ModelAdmin):
    list_filter = ('approved','time')

class SocialAdmin(admin.ModelAdmin):
    list_display = ('media','link')


admin.site.register(Category,CategoryAdmin)
admin.site.register(Reporter,ReporterAdmin)
admin.site.register(News,NewsAdmin)
admin.site.register(Photo,PhotoAdmin)
admin.site.register(BreakingNews,BreakingNewsAdmin)
admin.site.register(Announcement)
admin.site.register(Comment,CommentAdmin)
admin.site.register(About)
admin.site.register(Contact,ContactAdmin)
admin.site.register(Social,SocialAdmin)
admin.site.register(Newsletter)
admin.site.register(WhatsappGroup)


admin.site.site_header = "Newskerala Administration"
admin.site.site_title = "Newskerala Admin Portal"
admin.site.index_title = "Welcome to Newskerala Admin Portal"

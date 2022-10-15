from django.contrib import admin

from .models import *

# admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display =('title','slug','author','publish' ,'status')
    
    # to make a filter sidebar for filtering Posts
    list_filter = ('status', 'created', 'publish', 'author')
    
    # To Add a search field in the admin site
    
    search_fields = ('title', 'body')
    
    #to	prepopulate	the	slug field with the input of the title field
    prepopulated_fields = {'slug': ('title',)}
    
    raw_id_fields = ('author',)
    
    # to navigate through a data hierarchy
    date_hierarchy = 'publish'
    
    # To add a ordering functionality on the admin site
    ordering = ('status', 'publish')


    

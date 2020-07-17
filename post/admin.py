from django.contrib import admin

from .models import Blog, Author

admin.site.site_header = 'Admin Blog'
admin.site.register(Author)
admin.site.register(Blog)

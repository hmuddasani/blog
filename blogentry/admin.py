from django.contrib import admin
from .models import BlogEntry, Likes
# Register your models here.

class BlogEntryAdmin(admin.ModelAdmin):
	class Meta:
		model = BlogEntry
	list_display = ['title','published_date']
	prepopulated_fields = {"slug": ("title",)}
	
admin.site.register(BlogEntry, BlogEntryAdmin)
admin.site.register(Likes)

	
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.template.defaultfilters import slugify

# Create your models here.
class BlogEntry(models.Model):
	title = models.CharField(max_length=250)
	description = models.TextField()
	published_date = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	publish = models.BooleanField(default=False)
	slug = models.SlugField(max_length=50)	
	
	class Meta:
		ordering = ["-published_date"]
		
	def __unicode__(self):
			return self.title
			
	def get_absolute_url(self):
		return reverse('blog_detail', kwargs={"slug": self.slug})
		
	def save(self, *args, **kwargs):
		if not self.slug:
		          self.slug = slugify(self.title)
		super(BlogEntry, self).save(*args, **kwargs)
		
	

class Likes(models.Model):
		title = models.ForeignKey(BlogEntry)
		created = models.DateTimeField(auto_now_add=True)
		
	
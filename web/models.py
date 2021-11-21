from django.core.exceptions import ValidationError
from django.db import models
from django.utils.html import format_html
from taggit.managers import TaggableManager
from tinymce.models import HTMLField
from versatileimagefield.fields import VersatileImageField

SOCIAL_CHOICES = (
	('android', 'android'),('apple', 'apple'),('css3', 'css3'),('dribbble', 'dribbble'),('dropbox', 'dropbox'),('dropbox-alt', 'dropbox-alt'),
	('drupal', 'drupal'),('facebook', 'facebook'),('flickr', 'flickr'),('flickr-alt', 'flickr-alt'),('github', 'github'),('google', 'google'),
	('html5', 'html5'),('instagram', 'instagram'),('joomla', 'joomla'),('jsfiddle', 'jsfiddle'),('linkedin', 'linkedin'),('linux', 'linux'),
	('microsoft', 'microsoft'),('microsoft-alt', 'microsoft-alt'),('pinterest', 'pinterest'),('pinterest-alt', 'pinterest-alt'),
	('reddit', 'reddit'),('sharethis', 'sharethis'),('sharethis-alt', 'sharethis-alt'),('skype', 'skype'),('soundcloud', 'soundcloud'),
	('stack-overflow', 'stack-overflow'),('trello', 'trello'),('tumblr', 'tumblr'),('tumblr-alt', 'tumblr-alt'),('twitter', 'twitter'),
	('twitter-alt', 'twitter-alt'),('vimeo', 'vimeo'),('vimeo-alt', 'vimeo-alt'),('wordpress', 'wordpress'),('whatsapp', 'whatsapp'),('yahoo', 'yahoo'),('youtube', 'youtube'),
)

# News keys
class Category(models.Model):
	title = models.CharField(max_length=128)
	slug = models.SlugField(unique=True)
	popular = models.BooleanField(default=False)
	display_on_header = models.BooleanField(default=False)

	class Meta:
		verbose_name_plural = ('Categories')

	def __str__(self):
		return str(self.title)

	@property
	def news_count(self):
		return News.objects.filter(category=self.pk).count()


class Reporter(models.Model):
	name = models.CharField(max_length=128)
	photo = models.ImageField(upload_to='images/reporters')
	about = models.TextField()

	def __str__(self):
		return str(self.name)


class News(models.Model):
	title = models.CharField('News Title',max_length=128)
	slug = models.SlugField(unique=True)
	reporter = models.ForeignKey(Reporter,on_delete=models.PROTECT)
	category = models.ForeignKey(Category,on_delete=models.PROTECT)
	location = models.CharField(max_length=128,blank=True,null=True)
	display_time = models.DateTimeField()
	featured_image = VersatileImageField('Featured Image',upload_to='default/featured_images',blank=True,null=True,default="images/default-featured-image.jpg")
	summary = models.TextField()
	content = HTMLField('News Content')
	tags = TaggableManager()
	date_added = models.DateTimeField(auto_now_add=True, blank=True)
	published = models.BooleanField('Mark as published',default=True)

	popular = models.BooleanField('Mark as Popular',default=False)
	hot_post = models.BooleanField('Mark as Hotpost',default=False)
	trending = models.BooleanField('Mark as Trending',default=False)
	breaking = models.BooleanField('Show in Breaking News',default=False)
	view_count = models.IntegerField(default=0)

	class Meta:
		verbose_name_plural = ('Newses')
		ordering = ('-display_time',)

	def __str__(self):
		return str(self.title)

	def delete(self, *args, **kwargs):
		storage, path = self.featured_image.storage, self.featured_image.path
		super(News, self).delete(*args, **kwargs)
		storage.delete(path)

	@property
	def comment_count(self):
		return Comment.objects.filter(news=self.pk).count()

	def view_link(self):
		return format_html(
			'<a href="/news/{}" target="_blank">View Post</a>',
			self.slug,
		)


class Photo(models.Model):
	title = models.CharField('Photo Title',max_length=128)
	slug = models.SlugField(unique=True)
	image = VersatileImageField('Image',upload_to='images/gallery')
	summary = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True, blank=True)
	published = models.BooleanField('Mark as published',default=True)

	class Meta:
		verbose_name_plural = ('Photos')
		ordering = ('-date_added',)

	def __str__(self):
		return str(self.title)


class BreakingNews(models.Model):
	category = models.ForeignKey(Category,on_delete=models.PROTECT)
	title = models.TextField()
	time = models.DateTimeField(auto_now_add=True, blank=True)

	class Meta:
		ordering = ('-time',)
		verbose_name_plural = ('Breaking Newses')

	def __str__(self):
		return str(self.title)


class Announcement(models.Model):
	title = models.CharField(max_length=128)
	time = models.DateTimeField(auto_now_add=True, blank=True)
	content = models.TextField(blank=True,null=True)

	class Meta:
		ordering = ('-time',)

	def __str__(self):
		return str(self.title)


class Comment(models.Model):
	news = models.ForeignKey(News,on_delete=models.CASCADE)
	name = models.CharField(max_length=128)
	time = models.DateTimeField(auto_now_add=True, blank=True)
	comment = models.TextField()
	approved = models.BooleanField(default=False)

	class Meta:
		ordering = ('-time',)

	def __str__(self):
		return str(self.name)


# Basic Models.
class About(models.Model):
	title = models.CharField(max_length=128)
	logo = models.ImageField(upload_to='images/logo')
	summary = models.TextField()
	about = HTMLField()
	address = models.TextField()
	email = models.EmailField(max_length=128,default="newskerakadaily@gmail.com")
	phone = models.CharField(max_length=128,default="+91 0000 000 000")
	whatsapp_message = models.TextField(default="-")

	class Meta:
		verbose_name = ('About')
		verbose_name_plural = ('About')

	def clean(self):
		if (About.objects.count() >= 1 and self.pk is None):
			raise ValidationError("You can only create one About. Try editing/removing one of the existing about.")

	def __str__(self):
		return str(self.title)


class Contact(models.Model):
	name = models.CharField(max_length=128)
	email = models.EmailField(blank=True,null=True)
	phone = models.CharField(max_length=128)
	subject = models.CharField(max_length=128)
	message = models.TextField()

	def __str__(self):
		return str(self.name)


class Social(models.Model):
	order = models.IntegerField(unique=True)
	media = models.CharField(max_length=100,choices=SOCIAL_CHOICES)
	link = models.CharField(max_length=150)

	class Meta:
		ordering = ('order',)
		verbose_name = ('Social Media')
		verbose_name_plural = ('Social Medias')

	def __str__(self):
		return str(self.media)


class Newsletter(models.Model):
	name = models.CharField(max_length=15)
	place = models.CharField(max_length=15)
	number = models.CharField(max_length=15)
	district = models.CharField(max_length=15)

	def __str__(self):
		return str(self.number)


class WhatsappGroup(models.Model):
	name = models.CharField(max_length=128)
	link = models.CharField(max_length=1200,blank=True,null=True,default="javascript:void(0)")
	visible = models.BooleanField(default=False)

	def __str__(self):
		return str(self.name)

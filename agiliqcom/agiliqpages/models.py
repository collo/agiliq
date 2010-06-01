from django.db import models

class ContactUs(models.Model):
	name = models.CharField(max_length=75)
	phone = models.CharField(max_length=20, blank=True, null=True)
	email = models.EmailField()
	company = models.CharField(max_length=75, blank=True, null=True)
	message = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	
	class Meta:
		verbose_name_plural = 'Contacts from web'
	def __unicode__(self):
		return '%s - %s - %s' % (self.name, self.email, self.company)

class ClientManager(models.Manager):
    def get_query_set(self, *args, **kwargs):
        return super(ClientManager, self).get_query_set().filter(is_active = True)

class Client(models.Model):
    name = models.CharField(max_length = 100)
    about = models.TextField()
    url = models.URLField()
    email = models.EmailField()
    testimonial = models.TextField(null = True, blank = True)
    contact_name = models.CharField(max_length = 100)
    logo = models.ImageField(upload_to = 'logos/')
    has_testimonial = models.BooleanField(default = False)

    ordering = models.PositiveSmallIntegerField(default = 0)
    created_on = models.DateTimeField(auto_now_add = 1)
    updated_on = models.DateTimeField(auto_now= 1)
    is_active = models.BooleanField(default = True)

    _default_manager = models.Manager()
    objects = ClientManager()

    def save(self):
        if self.testimonial:
            self.has_testimonial = True
        else:
            self.has_testimonial = False
        super(Client, self).save()

    def __unicode__(self):
        return self.name

    class Meta:
        get_latest_by = ('ordering', )
        ordering = ('ordering', )

class BlogEntry(models.Model):
    feed_url = models.URLField()

    #Entry
    entry_title = models.CharField(max_length = 100)
    entry_url = models.URLField(unique = True)
    entry_summary = models.TextField()

    #Who columns
    created_on = models.DateTimeField(auto_now_add = 1)
    updated_on = models.DateTimeField(auto_now= 1)

    class Meta:
        get_latest_by = ('created_on', )

    def __unicode__(self):
        return self.entry_title

class TeamMember(models.Model):
    name = models.CharField(max_length = 100)
    bio = models.TextField()
    photo = models.ImageField(upload_to = 'people/', null = True, blank = True)
    designation = models.CharField(max_length = 100)

    twitter = models.URLField(null = True, blank = True)
    linked_in = models.URLField(null = True, blank = True)

    ordering = models.PositiveSmallIntegerField(default = 0)
    created_on = models.DateTimeField(auto_now_add = 1)
    updated_on = models.DateTimeField(auto_now= 1)

    def __unicode__(self):
        return self.name

    class Meta:
        get_latest_by = ('ordering', )
        ordering = ('ordering', )

class Project(models.Model):
    name = models.CharField(max_length = 100)
    blurb = models.TextField()
    url = models.URLField()
    logo = models.ImageField(upload_to = 'project_logos/')

    ordering = models.PositiveSmallIntegerField(default = 0)
    created_on = models.DateTimeField(auto_now_add = 1)
    updated_on = models.DateTimeField(auto_now= 1)

    class Meta:
        get_latest_by = ('ordering', )
        ordering = ('ordering', )

    def __unicode__(self):
        return self.name

class Whitepaper(models.Model):
    name = models.CharField(max_length = 100)
    details = models.TextField() 
    paper =  models.FileField(upload_to = 'whitepapers/')

    ordering = models.PositiveSmallIntegerField(default = 0)
    created_on = models.DateTimeField(auto_now_add = 1)
    updated_on = models.DateTimeField(auto_now= 1)

    class Meta:
        get_latest_by = ('ordering', )
        ordering = ('ordering', )


    def __unicode__(self):
        return self.name

class ContentBlock(models.Model):
	name = models.CharField(max_length=255)
	slug = models.SlugField()
	content = models.TextField()
	
	def __unicode__(self):
		return self.name

class Tweet(models.Model):
    screen_name = models.CharField(max_length=255)
    text = models.CharField(max_length=150)
    tweet_id = models.CharField(max_length=50)
    
    class Meta:
        get_latest_by = ('id',)
        
    def __unicode__(self):
        return self.screen_name

from django.db import models

class GeneralInfo(models.Model):  
    company_name = models.CharField(max_length=255, default="Company")
    location = models.CharField(max_length=255)  # Ensure the model name is correct
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    open_hours = models.CharField(max_length=100, null=True, blank=True)
    video_url = models.URLField(null=True, blank=True)
    twitter_url = models.URLField(null=True, blank=True)
    facebook_url = models.URLField(null=True, blank=True)
    instagram_url = models.URLField(null=True, blank=True)
    linkedin_url = models.URLField(null=True, blank=True)
    
    def __str__(self):
        return self.company_name
    

class Services(models.Model):
    icon = models.CharField(max_length=50, null=True, blank=True)
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title
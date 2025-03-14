from django.contrib import admin
from app.models import GeneralInfo, Services

# Ensure the model is registered only once
@admin.register(GeneralInfo)
class GeneralInfoAdmin(admin.ModelAdmin):
    list_display = ['company_name', 
                    'location', 
                    'email', 
                    'phone', 
                    'open_hours', 
                    'video_url', 
                    'twitter_url', 
                    'facebook_url', 
                    'instagram_url', 
                    'linkedin_url'
                    ]
    
    search_fields = ['company_name', 'location', 'email', 'phone']
    
    list_filter = ['location']

    # readonly_fields = ['email', 'phone']

    fieldsets = (
        ('Company Info', {
            'fields': ('company_name', 'location', 'email', 'phone')
        }),
        ('Social Media', {
            'fields': ('video_url', 'twitter_url', 'facebook_url', 'instagram_url', 'linkedin_url')
        }),
    )

@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    search_fields = ['title']
    list_filter = ['title']
   


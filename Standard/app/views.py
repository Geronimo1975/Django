from django.shortcuts import render
from app.models import GeneralInfo, Services

# Create your views here.

def index(request):
    general_info = GeneralInfo.objects.first()
    print(f"General Info: {general_info.location}")

    services = Services.objects.all(
        
    )

    context = {
        'location': general_info.location,
        'email': general_info.email,
        'phone': general_info.phone,
        'open_hours': general_info.open_hours,
        'video_url': general_info.video_url,
        'twitter_url': general_info.twitter_url,
        'facebook_url': general_info.facebook_url,
        'instagram_url': general_info.instagram_url,
        'linkedin_url': general_info.linkedin_url,
    }

    print("Context: {context}")

    return render(request, 'index.html', context)





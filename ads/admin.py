from django.contrib import admin

from .models import BottomAd, MiddleAd, PostAd, TopAd

admin.site.register(TopAd)
admin.site.register(PostAd)
admin.site.register(MiddleAd)
admin.site.register(BottomAd)

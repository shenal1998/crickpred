from django.contrib import admin
from .models import  Profile
#UserProfile class
class ProfileAdmin(admin.ModelAdmin):
  list_display = ("user","city", "zipcode",)
  list_display_links = ("user",)
  list_filter = ("zipcode",)
  search_fields = ("user",)

admin.site.register(Profile, ProfileAdmin)
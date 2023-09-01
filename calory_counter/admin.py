from django.contrib import admin

from user.models import Profile, PostFood
from .models import Food
# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    readonly_fields = ('date',)

admin.site.register(Food)
admin.site.register(Profile)
admin.site.register(PostFood)
# admin.site.register(MeatType)
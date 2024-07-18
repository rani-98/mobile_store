from django.contrib import admin
from .models import Mobile, mobileImage, Ram, Rom, Network, Front_cam, back_cam

# Register your models here.


class RamSizeInline(admin.TabularInline):
    model = Ram
    extra = 1
    max_num = 4  # how many rows to show

class RomSizeInline(admin.TabularInline):
    model = Rom
    extra = 1
    max_num = 4  # how many rows to show

class NetworkInline(admin.TabularInline):
    model = Network
    extra = 1
    max_num = 4  # how many rows to show

class back_camInline(admin.TabularInline):
    model = back_cam
    extra = 1
    max_num = 4  # how many rows to show

class front_camInline(admin.TabularInline):
    model = Front_cam
    extra = 1
    max_num = 4  # how many rows to show


class mobileImagesInline(admin.TabularInline):
    model = mobileImage
    extra = 1
    max_num = 4


class MobileAdmin(admin.ModelAdmin):
    inlines = [mobileImagesInline, front_camInline, back_camInline, RamSizeInline, RomSizeInline, NetworkInline]


admin.site.register(Mobile,MobileAdmin),

from django.contrib import admin
from .models import Video , Comment , UserDetails , Catogory_movie , Catogory_anime , Catogory_new_release , Cart 
# Register your models here.
admin.site.register(Video)
admin.site.register(Comment)
admin.site.register(UserDetails)

admin.site.register(Catogory_movie)
admin.site.register(Catogory_anime)
admin.site.register(Catogory_new_release)

admin.site.register(Cart)

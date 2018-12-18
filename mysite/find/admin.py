from django.contrib import admin
from .models import Post_type, Post, Relative, Missing_person, Victim

admin.site.register(Post_type)
admin.site.register(Post)
admin.site.register(Relative)
admin.site.register(Missing_person)
admin.site.register(Victim)


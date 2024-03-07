from django.contrib import admin
from .models import *


class CommentAdmin(admin.ModelAdmin):
    list_display = ('message', 'project', 'user')


admin.site.register(Project)
admin.site.register(Tag)
admin.site.register(Review)
admin.site.register(Comment, CommentAdmin)

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from boards.models import Board, Topic, Post


class BoardAdmin(admin.ModelAdmin):
    pass


class TopicAdmin(admin.ModelAdmin):
    pass


class PostAdmin(admin.ModelAdmin):
    pass


admin.site.register(Board, BoardAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Post, PostAdmin)

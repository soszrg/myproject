# -*- encoding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.conf.urls import url
from boards import views as boards_views

urlpatterns = [
    url(r"^(?P<pk>\d+)/$", view=boards_views.board_topics, name="board_topics"),
    url(r"^(?P<pk>\d+)/new/$", view=boards_views.topic_new, name="topic_new"),
]

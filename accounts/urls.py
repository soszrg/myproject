# -*- encoding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.conf.urls import url
from accounts import views as accounts_views

urlpatterns = [
    url(r"^signup/$", view=accounts_views.signup, name="accounts_signup"),
    url(r"^login/$", view=accounts_views.login, name="accounts_login"),
    url(r"^logout/$", view=accounts_views.logout, name="accounts_logout"),
]

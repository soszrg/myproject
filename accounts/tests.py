# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from accounts import views

# Create your tests here.
from django.urls import reverse, resolve


class SignupViewTest(TestCase):
    def setUp(self):
        pass

    def test_signup_view_status_code(self):
        url = reverse("accounts_signup")
        res = self.client.get(url)
        self.assertEquals(res.status_code, 200)

    def test_signup_url_resolves_signup_view(self):
        view_f = resolve("/accounts/signup/")
        self.assertEquals(view_f.func, views.signup)

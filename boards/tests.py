# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse, resolve

from boards.models import Board, Topic, Post
from boards.views import home
from boards import views as boards_views


class HomeTests(TestCase):
    def setUp(self):
        self.board = Board.objects.create(name="Django", description="Django board")
        url = reverse("home")
        self.response = self.client.get(url)

    def test_home_view_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, home)

    def test_home_view_contain_link_to_topics_page(self):
        board_topics_url = reverse('board_topics', kwargs={'pk': self.board.pk})
        self.assertContains(self.response, 'href="{0}"'.format(board_topics_url))


class BoardTopicsTest(TestCase):
    def setUp(self):
        Board.objects.create(name="Django", description="Django board")

    def test_board_topics_view_success_status_code(self):
        url = reverse("board_topics", kwargs={"pk": 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_board_topics_view_not_found_status_code(self):
        url = reverse("board_topics", kwargs={"pk": 99})
        res = self.client.get(url)
        self.assertEquals(res.status_code, 404)

    def test_board_topics_url_resolves_board_topics_view(self):
        views = resolve("/boards/1/")
        self.assertEquals(views.func, boards_views.board_topics)

    def test_board_topics_contains_link_back_to_home_page(self):
        home_page_url = reverse("home")
        board_topics_url = reverse("board_topics", kwargs={"pk": 1})
        response = self.client.get(board_topics_url)
        self.assertContains(response, 'href="{0}"'.format(home_page_url))


class TopicNewTest(TestCase):
    def setUp(self):
        Board.objects.create(name="Django", description="Django board")
        User.objects.create_user(username='john', email='john@doe.com', password='123')

    def test_topic_new_view_success_status_code(self):
        url = reverse("topic_new", kwargs={"pk": 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_topic_new_view_not_found_status_code(self):
        url = reverse("topic_new", kwargs={"pk": 2})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_topic_new_url_resolves_topic_new_view(self):
        view = resolve("/boards/1/new/")
        self.assertEquals(view.func, boards_views.topic_new)

    def test_topic_new_contains_link_back_to_home_page(self):
        home_page_url = reverse("home")
        url = reverse("topic_new", kwargs={"pk": 1})
        response = self.client.get(url)
        self.assertContains(response, 'href="{0}"'.format(home_page_url))

    def test_topic_new_contains_link_back_to_board_topics(self):
        topic_new_url = reverse("topic_new", kwargs={"pk": 1})
        board_topics_url = reverse("board_topics", kwargs={"pk": 1})
        response = self.client.get(topic_new_url)
        self.assertContains(response, 'href="{0}"'.format(board_topics_url))

    def test_csrf(self):
        url = reverse('topic_new', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertContains(response, 'csrfmiddlewaretoken')

    def test_new_topic_valid_post_data(self):
        url = reverse('topic_new', kwargs={'pk': 1})
        data = {
            'subject': 'Test title',
            'message': 'Lorem ipsum dolor sit amet'
        }
        response = self.client.post(url, data)
        self.assertTrue(Topic.objects.exists())
        self.assertTrue(Post.objects.exists())

    def test_new_topic_invalid_post_data(self):
        '''
        Invalid post data should not redirect
        The expected behavior is to show the form again with validation errors
        '''
        url = reverse('topic_new', kwargs={'pk': 1})
        response = self.client.post(url, {})
        self.assertEquals(response.status_code, 200)

    def test_new_topic_invalid_post_data_empty_fields(self):
        '''
        Invalid post data should not redirect
        The expected behavior is to show the form again with validation errors
        '''
        url = reverse('topic_new', kwargs={'pk': 1})
        data = {
            'subject': '',
            'message': ''
        }
        response = self.client.post(url, data)
        self.assertEquals(response.status_code, 200)
        self.assertFalse(Topic.objects.exists())
        self.assertFalse(Post.objects.exists())

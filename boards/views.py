# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect

from boards.forms import NewTopicForm
from boards.models import Board, Topic, Post


def home(request):
    boards = Board.objects.all()
    return render(request, "boards/home.html", {"boards": boards})


def board_topics(request, pk):
    board = get_object_or_404(Board, pk=pk)
    return render(request, "boards/board_topics.html", {"board": board})


def topic_new(request, pk):
    board = get_object_or_404(Board, pk=pk)
    if request.method == "POST":
        form = NewTopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.starter_id = 1
            new_topic.board = board
            new_topic.save()
            Post.objects.create(topic=new_topic, message=form.cleaned_data.get("message"), created_by_id=1)
            return redirect("board_topics", pk=board.pk)
    else:
        form = NewTopicForm()
    return render(request, "boards/topic_new.html", {'form': form, "board": board})


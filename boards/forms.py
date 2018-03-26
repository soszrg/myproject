# -*- encoding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django import forms

from boards.models import Topic


class NewTopicForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            "rows": 5,
            "placeholder": "Input your mind here!",
            "class": ""
        }),
        max_length=4000,
    )

    class Meta:
        model = Topic
        fields = (
            "subject",
            "message"
        )

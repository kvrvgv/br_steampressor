

from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Feedback, Comment, BlogPost


class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = "__all__"
        exclude = ["ip_address"]


class UserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ("text", )


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('title', 'description', 'content', 'image', )

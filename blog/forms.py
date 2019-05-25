from django import forms
from django.contrib.auth.models import User
from .models import Comment, UserProfile, Post

class UserForm(forms.ModelForm):
	username = forms.CharField(widget=forms.TextInput())
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('portfolio_site', 'profile_pic',)
    

class CommentForm(forms.ModelForm):
	body = forms.CharField(label='', widget=forms.Textarea(
		attrs={"placeholder": "Type your comment here", "class": "input", "cols": 50, "rows": 7, })
	)

	class Meta:
		model = Comment
		fields = ('body', )

class NewPostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'body', 'category', 'featured_image',)
			
    
		
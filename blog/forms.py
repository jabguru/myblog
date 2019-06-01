from django import forms
from django.contrib.auth.models import User
from .models import Comment, UserProfile, Post

class UserForm(forms.ModelForm):
	username = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Username:", "class": "input" }))
	email = forms.CharField(label='', widget=forms.EmailInput(attrs={"placeholder": "Email:", "class": "input" }))
	password = forms.CharField(label='',widget=forms.PasswordInput(attrs={"placeholder": "Password:", "class": "input" }))

	class Meta:
		model = User
		fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
	portfolio_site = forms.CharField(label='', widget=forms.URLInput(attrs={"placeholder": "Portfolio site:", "class": "input" }))
	
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
			
    
		
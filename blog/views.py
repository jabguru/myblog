from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post, Featured_Post
from .forms import CommentForm, UserForm, UserProfileForm, NewPostForm
#Login
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator

# Create your views here.


def index(request):

	posts = Post.objects.all().order_by('-published')
	
	paginator = Paginator(posts, 8)
	
	page = request.GET.get('page')

	posts = paginator.get_page(page)

	featured_post = Featured_Post.objects.all()[0]

	return render(request, 'blog/index.html', {'posts': posts, 'featured_post': featured_post})

@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('index'))

def post(request, post_id):
	post = Post.objects.get(id=post_id)

	form = CommentForm()

	comments = post.comments.all()
	num_of_comments = len(comments)

	if request.method == 'POST':
		form = CommentForm(request.POST)

		if form.is_valid:
			comment = form.save(commit=False)
			comment.name = request.user
			comment.post = post
			comment.save()


	return render(request, 'blog/post.html', {'post': post,'comments': comments, 
		'num_of_comments': num_of_comments, 'form': form, })

@login_required
def create_post(request):

	post_created = False

	if request.method == 'POST':
		post_form = NewPostForm(data=request.POST)

		if post_form.is_valid():
			new_post = post_form.save(commit=False)
			new_post.author = request.user

			if 'featured_image' in request.FILES:
				new_post.featured_image = request.FILES['featured_image']

			new_post.save()

			post_created = True

		else:
			print(post_form.errors)
	else:
		post_form = NewPostForm
	return render(request, 'blog/createpost.html', {'post_form': post_form, 'post_created': post_created,})


def register(request):

	registered = False

	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)

		if user_form.is_valid() and profile_form.is_valid():

			user = user_form.save()
			user.set_password(user.password)
			user.save()

			profile = profile_form.save(commit=False)
			profile.user = user

			if 'profile_pic' in request.FILES:
				profile.profile_pic = request.FILES['profile_pic']

			profile.save()

			registered = True

		else:
			print(user_form.errors, profile_form.errors)

	else:
		user_form = UserForm
		profile_form = UserProfileForm

	return render(request, 'blog/registration.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered,})


def user_login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username=username, password=password)

		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(reverse('index'))
			else:
				return HttpResponse('ACCOUNT NOT ACTIVE')
		else:
			print('Someone tried to login and failed!')
			print('Username: {}, Password: {}'.format(username, password))
			return HttpResponse('Invalid login details supplied')

	else:
		return render(request, 'blog/login.html', {})



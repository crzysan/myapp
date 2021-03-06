from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth import logout as django_logout
from django.conf import settings
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import get_user_model
from django.db.models import Count
from feedapp.forms import PostForm
from feedapp.models import Post, Report

# Create your views here.

def index(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('index')
    else:
        form = PostForm()
        posts = Post.objects.filter(hidden=False).order_by('-date_posted').all()

        context = {'form' : form, 'posts' : posts}
        return render(request, 'feedapp/index.html', context)
    return redirect('index')



def delete_post(request, post_id):
    # check if post belongs to user
    post = Post.objects.get(id=post_id)
    if post.user == request.user:
        post.delete()
    # remove it from the database
    # redirect back to same page
    return redirect('index')

def report_post(request, post_id):
    post = Post.objects.get(id=post_id)

    report, created = Report.objects.get_or_create(reported_by=request.user, post=post)

    if created:
        report.save()

    return redirect('index')


@permission_required('feedapp.change_user')
def block_user(request, user_id):
    users = get_user_model()

    user = users.objects.get(id=user_id)
    for post in user.post_set.all():
        if not post.hidden:
            post.hidden = True
            post.hidden_by = request.user
            post.date_hidden = datetime.now()
            post.save()

    user.is_active = False
    user.save()

    return redirect('reports')

@permission_required('feedapp.view_report', raise_exception=True)
def reports(request):
    reportslist = Post.objects.annotate(
                  times_reported=Count('report')).filter(times_reported__gt=0).all()

    context = {'reports' : reportslist}

    return render(request, 'feedapp/reports.html', context)

@permission_required('feedapp.change_post', raise_exception=True)
def hide_post(request, post_id):
    post = Post.objects.get(id=post_id)
    post.hidden = True
    post.date_hidden = datetime.now()
    post.hidden_by = request.user
    post.save()
    return redirect('reports')


@login_required
def logout(request):
    django_logout(request)
    domain = settings.SOCIAL_AUTH_AUTH0_DOMAIN
    client_id = settings.SOCIAL_AUTH_AUTH0_KEY
    return_to = 'http://94.227.244.125:8000' # this can be current domain
    return redirect(f'https://{domain}/v2/logout?client_id={client_id}&returnTo={return_to}')

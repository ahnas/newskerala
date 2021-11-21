from __future__ import unicode_literals

import json

from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from taggit.models import Tag

from .forms import CommentForm, ContactForm, NewsletterForm
from .models import Announcement, BreakingNews, Category, Comment, News, Photo, WhatsappGroup


def index(request):
    all_news = News.objects.filter(published=True),
    context = {
        "is_home"   : True,
        'announcements' : Announcement.objects.all()[:10],
        'hot_posts' : News.objects.filter(published=True,hot_post=True)[:3],
        'featured_news' : News.objects.filter(published=True)[:10],
        'popular_news' : News.objects.filter(published=True,popular=True)[:10],
        'trending_news' : News.objects.filter(published=True,trending=True)[:10],
        'tech_news' : News.objects.filter(published=True,category__title='Technology')[:10],
        'sports_news' : News.objects.filter(published=True,category__title='Sports')[:10],
        'world_news' : News.objects.filter(published=True,category__title='World')[:10],
        'local_news' : News.objects.filter(published=True,category__title='Local')[:10],
        'gulf_news' : News.objects.filter(published=True,category__title='Gulf')[:10],
        'business_news' : News.objects.filter(published=True,category__title='Business')[:10],
        'health_news' : News.objects.filter(published=True,category__title='Health')[:10],
        'food_news' : News.objects.filter(published=True,category__title='Food')[:10],
        'more_news' : News.objects.filter(published=True)[:10],
    }
    return render(request, 'web/index.html',context)


def about(request):
    context = {
        "is_about"  : True,
    }
    return render(request, 'web/about.html',context)

def advertisement(request):
    context = {
        "is_advertisement"  : True,
    }
    return render(request, 'web/advertisement.html',context)


def policy(request):
    context = {
        "is_policy"  : True,
    }
    return render(request, 'web/policy.html',context)


def join_whatsapp(request):
    whatsapp_groups = WhatsappGroup.objects.filter(visible=True),
    context = {
        "is_join_whatsapp"  : True,
        "whatsapp_groups"  : whatsapp_groups,
    }
    return render(request, 'web/join_whatsapp.html',context)

def terms(request):
    context = {
        "is_terms"  : True,
    }
    return render(request, 'web/terms.html',context)

def disclaimer(request):
    context = {
        "is_disclaimer"  : True,
    }
    return render(request, 'web/disclaimer.html',context)

def contact(request):
    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            response_data = {
                "status" : "true",
                "title" : "Successfully Submitted",
                "message" : "Message successfully Submitted"
            }
        else:
            response_data = {
                "status" : "false",
                "title" : "Form validation error",
            }
        return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    else:
        context = {
            "is_contact"    : True,
            "contact_form"      : ContactForm(),
        }
        return render(request, 'web/contact.html',context)


def category(request,slug):
    instance =  Category.objects.get(slug=slug)
    category_news_list =  News.objects.filter(category__slug=slug)[:200]
    paginator = Paginator(category_news_list,20)
    page_number = request.GET.get('page')
    news_list = paginator.get_page(page_number)

    context = {
        "is_category"  : True,
        'instance' : instance,
        'news_list' : news_list,
    }
    return render(request, 'web/category.html',context)


def tagged_news(request,tag):
    tag_obj = get_object_or_404(Tag, name=tag)
    tagged_news_list =  News.objects.filter(tags=tag_obj)[:200]
    paginator = Paginator(tagged_news_list,20)
    page_number = request.GET.get('page')
    news_list = paginator.get_page(page_number)
    context = {
        'news_list' : news_list,
    }
    return render(request, 'web/tagged_news.html',context)


def post(request,slug):
    instance =  News.objects.get(slug=slug)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.news = instance
            data.save()
            response_data = {
                "status" : "true",
                "title" : "Successfully Submitted",
                "message" : "Your comment will be visible after moderation"
            }
        else:
            print (form.errors)
            response_data = {
                "status" : "false",
                "stable" : "true",
                "title" : "Form validation error",
            }
        return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    else:
        prev_news = News.objects.filter(id__lt=instance.id).order_by('id').last()
        next_news = News.objects.filter(id__gt=instance.id).order_by('id').first()
        comments = Comment.objects.filter(news=instance,approved=True)

        instance.view_count += 1
        instance.save()

        context = {
            "is_news" : True,
            "instance" : instance,
            "prev_news" : prev_news,
            "next_news" : next_news,
            "comments" : comments,
            "comment_form" : CommentForm()
        }
        return render(request, 'web/post.html',context)


def video(request,slug):
    context = {
        "is_video"  : True,
    }
    return render(request, 'web/video.html',context)


def gallery(request):
    gallery =  Photo.objects.filter(published=True)[:100]
    paginator = Paginator(gallery, 20)
    page_number = request.GET.get('page')
    instances = paginator.get_page(page_number)
    context = {
        "is_gallery" : True,
        "instances" : instances,
    }
    return render(request, 'web/gallery.html',context)


def announcements(request):
    announcement_list =  Announcement.objects.all()[:100]
    paginator = Paginator(announcement_list, 20)
    page_number = request.GET.get('page')
    instances = paginator.get_page(page_number)

    context = {
        "is_announcements" : True,
        "instances" : instances,
    }
    return render(request, 'web/announcements.html',context)


def newsletter(request):
    if request.method == "POST":
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            response_data = {
                "status" : "true",
                "title" : "Successfully Subscribed",
                "message" : "Subscription successfully added"
            }
        else:
            response_data = {
                "status" : "false",
                "stable" : "true",
                "title" : "Form validation error",
            }
        return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    else:
        return HttpResponseNotFound("404")

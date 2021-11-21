import datetime

from ads.models import BottomAd, MiddleAd, PostAd, TopAd

from .forms import NewsletterForm
from .models import About, Category, News, Social, BreakingNews


def main_context(request):
    datetime.date.today()

    return {
        'domain' : request.META['HTTP_HOST'],
        'app_name' : 'News kerala Daily',
        'app_description' : 'News kerala Daily',
        'since' : datetime.datetime.now().year - 1982,
        'socials' : Social.objects.all(),
        'about' : About.objects.first(),
        'categories' : Category.objects.filter(popular=True),
        'header_categories' : Category.objects.filter(display_on_header=True),
        'newsletter_form' : NewsletterForm(),

        'top_ads' : TopAd.objects.filter(visible=True),
        'post_ads' : PostAd.objects.filter(visible=True),
        'middle_ads' : MiddleAd.objects.filter(visible=True),
        'bottom_ads' : BottomAd.objects.filter(visible=True),

        'popular_news' : News.objects.filter(published=True,popular=True)[:5],
        'breaking_newses' : BreakingNews.objects.all()[:10],
        'extra_breaking_newses' : News.objects.filter(breaking=True)[:10],

    }

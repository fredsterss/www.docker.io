# Create your views here.

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import request
from mailchimp import utils as mailchimputils
from datetime import datetime
from forms import NewsSubscribeForm
from django.http import HttpResponseRedirect
# from .utils import get_app_auth_twitter
from utils2 import TwitterClient
import json
from django.core.cache import cache

#We are not using the intercom plugin because we use js instead
#from intercom import Intercom

def home(request):
    """
    homepage
    """
    form = NewsSubscribeForm()

    CONSUMER_KEY = 'aEtFq69wvzUAjlzwh9Tw'
    CONSUMER_SECRET = 'o6mcmOLtp35loXfUbRBOVpyfzenFdOSwBV3jd4MMFSM'
    TWITTER_TIMEOUT = 3600

    tweet = cache.get("316683059296624640")

    if tweet:
        pass
    else:
        twitter_client = TwitterClient(CONSUMER_KEY, CONSUMER_SECRET)
        tweet = twitter_client.request('https://api.twitter.com/1.1/statuses/show.json?id=316683059296624640')

        cache.set('316683059296624640', tweet, TWITTER_TIMEOUT)
        data = json.loads(tweet)



    print json.dumps(tweet, sort_keys=True, indent=4, separators=(',', ':'))


    return render_to_response("homepage.md", {
        "form": form,
    }, context_instance=RequestContext(request))


def email_thanks(request):
    """
    Page for thanking the user for signup
    """

    if request.method == "POST":
        form = NewsSubscribeForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]

            list = mailchimputils.get_connection().get_list_by_id('c0995b6e8f')

            results = list.subscribe(
                'thatcher@koffiedik.net',
                {
                    'EMAIL': 'thatcher@peskens.nl',
                    'FNAME': '',
                    'LNAME': '',
                    'MMERGE3': '',
                    'MMERGE4': '',
                    'MMERGE5': 'www.docker.io/',
                    },
                'html',
                'true'
            )

            intercom_extra = {
                'email': "thatcher+intercom@dotcloud.com",
                'news_signup_at': datetime.now().strftime("%Y-%m-%d"),
                #        'created_at': datetime.now().strftime("%s"),
                #        'github_name': 'dhrp2',
            }

            return render_to_response('base/email_thanks.html',
                {
                    'form': form,
                    'intercom_extra': intercom_extra
                },
                context_instance = RequestContext(request))

    else:
        form = NewsSubscribeForm()

    return render_to_response("homepage.md", {
        "form": form,
        }, context_instance=RequestContext(request))



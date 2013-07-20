__author__ = 'thatcher'

from django import template
from base.utils2 import TwitterClient
import json
from django.core.cache import get_cache


cache = get_cache('disk_cache')

# from django.core.urlresolvers import reverse
# import re

register = template.Library()

CONSUMER_KEY = 'aEtFq69wvzUAjlzwh9Tw'
CONSUMER_SECRET = 'o6mcmOLtp35loXfUbRBOVpyfzenFdOSwBV3jd4MMFSM'
TWITTER_TIMEOUT = 3600 * 24



# @register.tag(name="list_tweets")

@register.tag
def list_tweets(parser, token):
    """
    Tag written to fetch the tweets from tweet id's. expects a plain list of tweet id's newline separated.

    ~tp
    """

    nodelist = parser.parse(('end_list_tweets',))
    parser.delete_first_token()
    tweets = TweetNode(nodelist)
    return tweets

class TweetNode(template.Node):
    def __init__(self, nodelist):
        self.nodelist = nodelist
    def render(self, context):
        output = self.nodelist.render(context)

        items = output.split()

        tweet = {}
        tweets = []
        html = ""

        for item in items:
            tweet = cache.get(item)

            if tweet:
                pass
            else:
                twitter_client = TwitterClient(CONSUMER_KEY, CONSUMER_SECRET)
                print item
                tweet = twitter_client.request('https://api.twitter.com/1.1/statuses/show.json?id={0}'.format(item))

                cache.set(item, tweet, TWITTER_TIMEOUT)

            data = json.loads(tweet)
            # print data['user']['screen_name']
                # print data.user.name
                # print data.user.url
                # print data.user.profile_image_url
                #
                # print data['text']
                # print data.created_at

                # tweets.append(tweet)

            # for tweet in tweets:
            html += """
            <div class="tweet">
                <img src="{}">
                <span class="handle">@{}</span>
                <span class="username">({})</span>
                <span class="text">{}</span>
            </div>

            """.format(
                data['user']['profile_image_url'].encode('utf-8').strip(),
                data['user']['screen_name'].encode('utf-8').strip(),
                data['user']['name'].encode('utf-8').strip(),
                data['text'].encode('utf-8').strip()
                # "text"
            )
        return html
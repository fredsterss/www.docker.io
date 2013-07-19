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
TWITTER_TIMEOUT = 3600



# @register.tag(name="list_tweets")

@register.tag
def list_tweets(parser, token):
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
            print data['user']['screen_name']
                # print data.user.name
                # print data.user.url
                # print data.user.profile_image_url
                #
            print data['text']
                # print data.created_at

                # tweets.append(tweet)

            # for tweet in tweets:
            html += """
            <div class="tweet">
                <img src="{}">
                <span class="username">{}</span>
                <span class="text">{}</span>
            </div>

            """.format(


                data['user']['profile_image_url'],
                data['user']['name'],
                data['text']
                # "text"
            )

                        # )

        return html




@register.simple_tag
def sayhi():
    """
    Tag written to be able to add a link "back to search results on any page linked to
    after coming from the search results.

    It looks like a bit much to just match 'search', but I wanted to make sure it does not
     come up when you hit a repository from google or whatever other search engine

    It could also provide other sorts of navigations of we would like to.

    ~tp
    """
    return "hi!"
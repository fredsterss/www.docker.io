__author__ = 'thatcher'

from django import template
from django.core.urlresolvers import reverse
import re

register = template.Library()

@register.simple_tag
def navactive(request, path, reverse_args=None):
    """
    Navactive expects two or three arguments.
    if there are two arguments, the second argument is expected to te the end of the path.
    If there are three arguments, the second argument is the reverse name, and the
    third argument, the argument for the path.

    e.g.
    {% navactive request 'account/' %}
    or
    {% navactive request 'profile_home' %}
    or
    {% navactive request 'profile' 'dhrp' %}
    """

    if not path.endswith('/'):
        if reverse_args is None:
            path = reverse(path)
        else:
            path = reverse(path, args=[reverse_args])


    # if request.path.endswith(path):
    if request.path == path:
        return "active"
    else:
        return ""




@register.simple_tag
def link_back(request):
    """
    Tag written to be able to add a link "back to search results on any page linked to
    after coming from the search results.

    It looks like a bit much to just match 'search', but I wanted to make sure it does not
     come up when you hit a repository from google or whatever other search engine

    It could also provide other sorts of navigations of we would like to.

    ~tp
    """


    backlink = ''

    if 'HTTP_REFERER' in request.META and 'HTTP_HOST' in request.META:

        x = re.compile('.+://([\w:._-]+)/')
        try:
            referrer_host = x.match(request.META['HTTP_REFERER']).group(1)

            # Only accept referrals from our own domain
            if referrer_host == request.META['HTTP_HOST']:

                try:
                    y = re.compile('.+://([\w:._-]+)/([\w/_-]+)')
                    pretty_name = y.match(request.META['HTTP_REFERER']).group(2)

                    if pretty_name == "search":
                        backlink = "<a href=" + request.META['HTTP_REFERER'] + "> &lt; back to search results</a>"
                except:
                    pass
        except:
            pass

    return backlink



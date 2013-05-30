__author__ = 'thatcher'

from django import template


register = template.Library()

@register.simple_tag
def navactive(request, path):

    if request.path.endswith(path):
        return "active"
    else:
        return "nonactive"


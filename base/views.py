# Create your views here.

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import request
from mailchimp import utils as mailchimputils
from datetime import datetime
from forms import NewsSubscribeForm
from django.http import HttpResponseRedirect

#We are not using the intercom plugin because we use js instead
#from intercom import Intercom

def home(request):
    """
    homepage
    """
    form = NewsSubscribeForm()

    return render_to_response("homepage.jmd", {
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

    return render_to_response("homepage.jmd", {
        "form": form,
        }, context_instance=RequestContext(request))



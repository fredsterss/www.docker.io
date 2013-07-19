{% extends 'homepage.html' %}
{% load list_tweets %}

{% block title %}Homepage {% endblock %}
{% block meta-description %}An open source project to pack, ship and run any application as a lightweight container{% endblock %}
{% block meta-keywords %}Docker, linux containers, PaaS, dotCloud, introduction, about, homepage{% endblock %}

{% block copy_headline %}

# an open source project to pack, ship and run any application as a lightweight container #

{% endblock %}


{% block copy_introduction %}

Docker is an open-source project which allows you to easily create lightweight, portable, self-sufficient containers
    from your application. The same container that a developer builds and tests on a laptop can run at scale, in
    production, on VMs, bare metal servers, OpenStack clusters, public instances, or combinations of the above.

{% endblock %}


{% block copy_news %}

### Docker hackday ###
Tuesday July 30, we will have another Docker hackday. This time we feature a couple of special guests.

* **mr from eBay**, talking about what he does there.


<table>
    <tr>
        <td>Foo</td>
    </tr>
    <tr>

        <td>Bar</td>
    </tr>
    <tr>

        <td>Foo</td>
    </tr>
    <tr>

        <td>Bar</td>

    </tr>
</table>


{% endblock %}


{% block copy_1 %}

# The title #

{% endblock %}


{% block tweets %}


{% list_tweets %}

357945285164548096
357983836006645760
357673068086325248

{% end_list_tweets %}

{% endblock %}


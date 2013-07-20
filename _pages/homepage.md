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
    <span class="read-more"><a href="{% url 'about' %}" title="About Docker">Read more -></a></span>
{% endblock %}


{% block copy_news %}
## Latest updates

#### Jul 18 • Docker 0.5 Released
We've released version 0.5. Amongst other things, this release containes External Volumes, Advanced Networking and
    support for an Self Hosted Registry,
    <span class="read-more"><a href="http://blog.docker.io/2013/07/docker-0-5-0-external-volumes-advanced-networking-self-hosted-registry/">read more -></a></span>

#### Jul 11 • Featuring awesome projects:
Everyday the Docker community is building awesome tools and projects with and for Docker. We want to share some of these with you.
    <span class="read-more"><a href="http://blog.docker.io/2013/07/docker-projects-from-the-docker-community/">read more -></a>

#### Jun 6 • Docker in Openstack:
Sam Alba presents an article about the integration of Docker in OpenStack's cloud computing platform: NOVA. This integration
    allows users of OpenStack to seamlessly create Docker containers from the interface they are already using.
    <span class="read-more"><a href="http://blog.docker.io/2013/06/openstack-docker-manage-linux-containers-with-nova/">read more -></a></span>

{% endblock %}



{% block copy_community %}
## From the community

#### Upcoming Meetup • Jul 30:
Come to our July Meetup in San Francisco to hear representatives from **EBay**, **Mailgun (Rackspace)** and **Mozilla**
    discuss how they are using Docker.
    <span class="read-more"><a href="http://www.meetup.com/Docker-meetups/">go to meetup -></a></span>

{% endblock %}


{% block copy_1 %}

# The title #

{% endblock %}


{% block tweets %}


{% list_tweets %}

354224101574983681
355890863261491200
356763917625724928
356280542892802050
357972314660405249
355792575988371456
355705492087119875
354715613337354241
354411184524500992
354829574980378624
355955060607430656
355756267224047616
355404525793841153
355623162551083008
355705492087119875
355761264670162944
355346670520770561
355172662873567233
354954990277758978
355024956763021312
354781876730335233
354970275353329664
354368422328541187
348281405974925313
348249053332647936
347915284977418241
347559367652032513
347003250299531264

{% end_list_tweets %}

{% endblock %}


This is the www.docker.io website repository
============================================

It intends to be small, simple and straightforward.

Builds on 
---------

* Django 1.5
* Twitter Bootstrap
* Includes tracking options such as from Google Analytics and Intercom.io


Installation
------------

* Clone this repository
* pip install -r requirements.txt
* set in your environment the SECRET_KEY


Running locally
----------------

Because this repository is in a public repository, we keep our secrets in environment variables. If you do not
set these keys, running the app might fail.

Most notable:

SECRET_KEY
MAILCHIMP_API_KEY

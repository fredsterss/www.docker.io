This is the www.docker.io website repository
==============================================

It intends to be small, simple and straightforward.

Builds on
----------

* Django 1.5
* Twitter Bootstrap
* Includes tracking options such as from Google Analytics and Intercom.io


Making simple changes
---------------------

This project uses a simplified Django structure, and has the notable feature that all major text contained on this
 website can be maintained by changing the markdown files contained in /_pages/. There is a good chance this will
 be the only part you need to touch.


Simple installation
-------------------

* Clone this repository
* pip install -r requirements.txt
* Done!

To preview the website run: `` ./manage.py runserver``. It will pick the local settings by default, which require no
database.


Structure changes
-----------------

Because this repository is in a public repository, we keep our secrets in environment variables. If you do not
set these keys, running the app might fail.

Most notable:

* SECRET_KEY
* MAILCHIMP_API_KEY

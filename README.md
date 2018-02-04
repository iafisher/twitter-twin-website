# Twitter Twin
A website that analyzes your tweets using NLP and matches them with a similar celebrity Twitter
user.

This repo hosts the front-end and back-end code for the Twitter Twin website, but not the code for
the NLP training.

Developed by [Ian Fisher](https://github.com/elpez), [Conor Stuart Roe](https://github.com/cstuartroe) and [Emily Lin](https://github.com/ellin2) for the 2018 Tri-Co Hackathon.

## Packages and libraries
- [Django](https://djangoproject.com): A Python web framework.
- [Gunicorn](http://gunicorn.org/): A Python WSGI HTTP server.
- [Heroku](https://www.heroku.com/): To host our website live.
- [Pure](https://purecss.io/): A CSS framework.
- [jQuery](https://jquery.com/): A library of JavaScript utilities.
- [WhiteNoise](http://whitenoise.evans.io/en/stable/): A library for serving static files with Django.
- [favicon.ico](https://www.trumbulltimes.com/wp-content/uploads/sites/32/2015/05/TT-icon-600x600.png)

## Helpful resources
These are some resources that we found helpful while developing this project.

- [The Django documentation](https://docs.djangoproject.com/en/2.0/)
- [API reference for jQuery](http://api.jquery.com/)
- [Configuring Django Apps for Heroku](https://devcenter.heroku.com/articles/django-app-configuration#migrating-an-existing-django-project)
- [Deploying Python and Django Apps on Heroku](https://devcenter.heroku.com/articles/deploying-python)

##Screenshots

!(https://i.imgur.com/m7z8Mmx.png)

All five celebrities successfully get flagged as themselves, with varying degrees of certainty.

!(https://i.imgur.com/gP55VQL.png)

Users can also input custom messages.

!(https://i.imgur.com/6eqOgbS.png)

A variety of messages work.

!(https://i.imgur.com/oXRGPeE.png)

The site is fully responsive, with pictures and fonts changing with browser width.

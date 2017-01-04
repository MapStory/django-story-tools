[![Travis CI Status](https://travis-ci.org/MapStory/django-story-tools.svg)](https://travis-ci.org/MapStory/django-story-tools)
# django-story-tools
A Django wrapper for Story-Tools that enables functionality for styling, annotations, timeline configuration and editing of a web mapping client based on OpenLayers 3.

Installation
---------------------

Install the latest stable version from PIP:

```pip install django-story-tools```

Download django-story-tools and install it directly from source:

```python setup.py install```


Project Configuration
---------------------

Once installed you can configure your project to use django-story-tools with the following steps.

Add django-story-tools to INSTALLED_APPS in your project's settings module:

```
INSTALLED_APPS = (
    'django-story-tools',
    # other apps
)
```


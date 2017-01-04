from django.conf.urls import patterns, url


urlpatterns = patterns(
    'story_tools.views',
    url(r'^/frames$', 'frames', name='frames'),
    url(r'^/markers$', 'markers', name='markers'),
)
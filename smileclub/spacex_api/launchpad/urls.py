from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^api/v1/launchpad/(?P<pk>[0-9]+)$',
        views.get_one_launchpad,
        name='get_one_launchpad'
    ),
    url(r'^api/v1/launchpad/$',
        views.get_all_launchpads,
        name='get_all_launchpads'
    )
]
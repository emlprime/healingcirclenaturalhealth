from django.conf.urls.defaults import *
from healingcirclenaturalhealth.settings import MEDIA_ROOT

urlpatterns = patterns('django.views.generic.simple',
    (r'^$', 'direct_to_template', {'template': 'home.html'}),
    (r'^services/$', 'direct_to_template', {'template': 'services.html'}),
    (r'^help/$', 'direct_to_template', {'template': 'help.html'}),
)

urlpatterns += patterns('',
    (r'^product/', include('healingcirclenaturalhealth.product.urls')),
    (r'^accounts/logout/', 'django.contrib.auth.views.logout'),
    (r'^accounts/login/', 'django.contrib.auth.views.login'),
    (r'^media/(.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
#     (r'^admin/', include('django.contrib.admin.urls')),
)

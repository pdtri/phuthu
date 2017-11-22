from django.conf.urls import url
from . import views
from . import views_congtac
from . views_congtac import GeneratePdf
urlpatterns = [
    url(r'^add_congtac/$', views_congtac.add_congtac, name='add_congtac'),
    url(r'^tim_congtac/$', views_congtac.tim_congtac.as_view(), name='tim_congtac'),
    url(r'^thu/$', views_congtac.thu.as_view(), name='thu'),
    #url(r'^pdf/$', views_congtac.GeneratePdf.as_view(), name='GeneratePdf'),
	url(r'^pdf/$', GeneratePdf.as_view()),
]

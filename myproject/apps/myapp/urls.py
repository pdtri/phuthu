from django.conf.urls import url
from . import views
from . import views_congtac
urlpatterns = [
    url(r'^add_congtac/$', views_congtac.add_congtac, name='add_congtac'),
    url(r'^tim_congtac/$', views_congtac.tim_congtac.as_view(), name='tim_congtac'),
]
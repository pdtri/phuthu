from django.conf.urls import url
from . import views
urlpatterns = [
    """
	url(r'^add_chuyenthue/$', views_congtac.add_congtac, name='add_congtac'),
    url(r'^tim_chuyenthue/$', views_congtac.tim_congtac.as_view(), name='tim_congtac'),
    """
]
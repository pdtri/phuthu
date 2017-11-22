from django.conf.urls import url
from . import views
from . import views
from . views import inphieu
urlpatterns = [
    url(r'^chonphieuin/$', views.chonphieuin, name='chonphieuin'),
    url(r'^inphieu/$', inphieu.as_view()),
    #url(r'^admin/tpc/(?P<pcid>\d+)/$', views.admin_tpc_detail,name='admin_tpc_detail'),
    url(r'^admin/tpc/(?P<pcid>\d+)/pdf/$', views.admin_tpc_pdf,name='admin_tpc_pdf'),
	#url(r'^add_chuyenthue/$', views_congtac.add_congtac, name='add_congtac'),
    #url(r'^tim_chuyenthue/$', views_congtac.tim_congtac.as_view(), name='tim_congtac'),
]
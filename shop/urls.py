from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.product_list, name='product_list'),
    url(r'^course/$', views.course_list, name='course_list'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
    url(r'^course/(?P<category_slug>[-\w]+)/$', views.course_list, name='course_list_by_coursecategory'),
    url(r'^course/(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.course_detail, name='course_detail'),
]

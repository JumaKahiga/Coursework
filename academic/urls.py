from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^login/$', views.login, name='login'),
    url(r'^current_orders/$', views.current_orders, name= 'current_orders'),
    url(r'^revisions/$', views.revisions, name='revisions'),
    url(r'^approved_orders/$', views.approved_orders, name= 'approved_orders'),
    url(r'^payment_history/$', views.payment_history, name= 'payment_history'),
    url(r'^new_order/$', views.new_order, name= 'new_order'),
    url(r'^invoice/$', views.invoice, name='invoice'),
    url(r'^order/CA(?P<pk>\d+)/$', views.order, name='order'),

]

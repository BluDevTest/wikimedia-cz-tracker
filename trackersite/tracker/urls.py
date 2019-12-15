# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.views.generic import DetailView, RedirectView

import tracker.views
from tracker.models import Grant
from tracker import feeds

urlpatterns = [
    url(r'tickets/(?:page/(?P<page>\d+)/)?$', tracker.views.ticket_list, name='ticket_list'),
    url(r'ticket/watch/(?P<pk>\d+)/?$', tracker.views.watch_ticket, name='watch_ticket'),
    url(r'tickets/feed/$', feeds.LatestTicketsFeed(), name='ticket_list_feed'),
    url(r'tickets/feed/submitted/$', feeds.SubmittedTicketsFeed(), name='ticket_submitted_feed'),
    url(r'ticket/(?P<pk>\d+)/$', tracker.views.ticket_detail, name='ticket_detail'),
    url(r'ticket/(?P<pk>\d+)/sign/$', tracker.views.sign_ticket, name='sign_ticket'),
    url(r'ticket/(?P<pk>\d+)/edit/$', tracker.views.edit_ticket, name='edit_ticket'),
    url(r'ticket/(?P<pk>\d+)/edit/copypreexpeditures/$', tracker.views.copypreexpeditures, name='copypreexpeditures'),
    url(r'ticket/(?P<pk>\d+)/edit/docs/$', tracker.views.edit_ticket_docs, name='edit_ticket_docs'),
    url(r'ticket/(?P<pk>\d+)/edit/docs/new/$', tracker.views.upload_ticket_doc, name='upload_ticket_doc'),
    url(r'ticket/(?P<pk>\d+)/edit/(?P<ack_type>[a-z_]+)/add/$', tracker.views.ticket_ack_add, name='ticket_ack_add'),
    url(r'ticket/(?P<pk>\d+)/edit/acks/(?P<ack_id>\d+)/delete/$', tracker.views.ticket_ack_delete, name='ticket_ack_delete'),
    url(r'ticket/(?P<ticket_id>\d+)/docs/(?P<filename>[-_\.A-Za-z0-9]+\.[A-Za-z0-9]+)$', tracker.views.download_document, name='download_document'),
    url(r'ticket/new/$', tracker.views.create_ticket, name='create_ticket'),
    url(r'ticket/(?P<ticket_id>\d+)/media/show/$', tracker.views.show_media, name='show_media'),
    url(r'ticket/(?P<ticket_id>\d+)/media/update/$', tracker.views.update_media, name='update_media'),
    url(r'ticket/(?P<ticket_id>\d+)/media/manage/$', tracker.views.manage_media, name='manage_media'),
    url(r'ticket/(?P<ticket_id>\d+)/media/manage/success/$', tracker.views.update_media_success, name='update_media_success'),
    url(r'ticket/(?P<ticket_id>\d+)/media/manage/error/$', tracker.views.update_media_error, name='update_media_error'),
    url(r'topics/$', tracker.views.topic_list, name='topic_list'),
    url(r'topics/finance/$', tracker.views.topic_finance, name='topic_finance'),
    url(r'topics/acks/$', tracker.views.topic_content_acks_per_user, name='topic_content_acks_per_user'),
    url(r'topics/acks/acks\.csv$', tracker.views.topic_content_acks_per_user_csv, name='topic_content_acks_per_user_csv'),
    url(r'topic/(?P<pk>\d+)/$', tracker.views.topic_detail, name='topic_detail'),
    url(r'subtopic/(?P<pk>\d+)/$', tracker.views.subtopic_detail, name='subtopic_detail'),
    url(r'topic/watch/(?P<pk>\d+)/$', tracker.views.watch_topic, name='watch_topic'),
    url(r'topic/(?P<pk>\d+)/feed/$', feeds.TopicTicketsFeed(), name='topic_ticket_feed'),
    url(r'topic/(?P<pk>\d+)/feed/submitted/$', feeds.TopicSubmittedTicketsFeed(), name='topic_submitted_ticket_feed'),
    url(r'grants/$', tracker.views.grant_list, name='grant_list'),
    url(r'grant/watch/(?P<pk>\d+)/?$', tracker.views.watch_grant, name='watch_grant'),
    url(r'grant/(?P<slug>[-\w]+)/$', DetailView.as_view(model=Grant), name='grant_detail'),
    url(r'users/(?P<username>\w+)/$', tracker.views.user_detail, name='user_detail'),
    url('users/', tracker.views.user_list, name='user_list'),
    url('my/details/', tracker.views.user_details_change, name='user_details_change'),
    url('my/preferences/', tracker.views.preferences, name='preferences'),
    url('my/deactivate/', tracker.views.deactivate_account, name='deactivate_account'),
    url('transactions/', tracker.views.transaction_list, name='transaction_list'),
    url('transactions/feed/', feeds.TransactionsFeed(), name='transactions_feed'),
    url('transactions/transactions.csv', tracker.views.transactions_csv, name='transactions_csv'),
    url(r'cluster/(?P<pk>\d+)/$', tracker.views.cluster_detail, name='cluster_detail'),
    url('comments/', include('django_comments.urls')),
    url(r'admin/users/$', tracker.views.admin_user_list, name='admin_user_list'),
    url(r'export/$', tracker.views.export, name='export'),
    url(r'import/$', tracker.views.importcsv, name='importcsv'),
    url(r'tickets/json/(?P<lang>.+).json$', tracker.views.tickets, name='tickets'),
    url('api/mediawiki', tracker.views.mediawiki_api, name='mediawiki_api'),
    url('api/email_all', tracker.views.email_all_users, name='email_all_users'),
    url('api/email_admin', tracker.views.email_all_admins, name='email_all_admins'),
]

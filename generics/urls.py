# -*- coding: utf-8 -*-
from django.conf.urls import url #include,

from generics import views

# import logging
# logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)


urlpatterns = [
    url(r'^task_api$', views.task_api, name="task_api"),
    url(r'^celery_test$', views.celery_test, name="celery_test"),
    url(r'^messages_api$', views.messages_api, name="messages_api"),
]

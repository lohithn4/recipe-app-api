from __future__ import absolute_import, unicode_literals
import os
from django.contrib.auth import get_user_model
from pinax.eventlog.models import log, Log
from pinax.eventlog.signals import event_logged
from django.utils import timezone
from django.contrib.contenttypes.models import ContentType

from app import celery_app


@celery_app.task
def create_log(user_id, action, **extra_args):
    print("Not performing here...")
    # print("user_id=", user_id)
    # user = get_user_model().objects.get(pk=user_id)
    # extra = extra_args.get('extra', {})
    # content_type = extra_args.get('content_type', None)
    # object_id = extra_args.get('object_id', None)
    #
    # if (user is not None and not user.is_authenticated):
    #     user = None
    # dateof = timezone.now()
    #
    # event = Log.objects.create(
    #     user=user,
    #     action=action,
    #     extra=extra,
    #     content_type=ContentType(content_type),
    #     object_id=object_id,
    #     timestamp=dateof
    # )
    # event = event_logged.send(sender=Log, event=event)

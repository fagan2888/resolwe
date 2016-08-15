"""
============
Celery Tasks
============

"""
from __future__ import absolute_import

from celery import shared_task  # pylint: disable=import-error


@shared_task
def celery_run(executor, data_id, script, verbosity):
    """Run process executor."""
    executor.run(data_id, script, verbosity)

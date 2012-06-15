#-*- coding: utf-8 -*-

import os
import logging
import kombu.utils.debug
from kombu import Exchange, Queue
from kombu.mixins import ConsumerMixin


class Worker(ConsumerMixin):

    queues = []

    def __init__(self, connection):
        self.connection = connection

    def get_consumers(self, Consumer, channel):
        consumers = []
        for entry in self.queues:
            q = Queue(entry['queue_name'], exchange=entry['exchange'],
                      routing_key=entry['routing_key'],
                      queue_arguments=entry.get('queue_arguments', None))
            handler = entry['handler']
            consumers.append(Consumer(queues=[q], callbacks=[handler]))
        return consumers


def run(conn, debug=False):
    if debug:
        os.environ.update(KOMBU_LOG_CHANNEL="1", KOMBU_LOG_CONNECTION="1")
        kombu.utils.debug.setup_logging(loglevel="DEBUG")

    Worker(conn).run()

#-*- coding: utf-8 -*-

import os
import logging
import threading
import kombu.utils.debug
from kombu import Exchange, Queue
from kombu.mixins import ConsumerMixin


class Worker(threading.Thread, ConsumerMixin):

    queues = []

    def __init__(self, connection):
        self.connection = connection
        super(Worker, self).__init__()
        self.daemon = True

    def get_consumers(self, Consumer, channel):
        consumers = []
        for entry in self.queues:
            q = Queue(entry['queue_name'], exchange=entry['exchange'],
                      routing_key=entry['routing_key'],
                      queue_arguments=entry.get('queue_arguments', None))
            handler = entry['handler']
            consumers.append(Consumer(queues=[q], callbacks=[handler]))
        return consumers

    def run(self):
        while not self.should_stop:
            try:
                if self.restart_limit.can_consume(1):
                    for _ in self.consume(limit=None):
                        pass
            except self.connection.connection_errors:
                self.error("Connection to broker lost. "
                           "Trying to re-establish the connection...")

    def stop(self):
        self.should_stop = True
        self.join()


def run(conn, debug=False):
    if debug:
        os.environ.update(KOMBU_LOG_CHANNEL="1", KOMBU_LOG_CONNECTION="1")
        kombu.utils.debug.setup_logging(loglevel="DEBUG")

    worker = Worker(conn)
    worker.start()
    return worker

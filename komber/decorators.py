#-*- coding: utf-8 -*-
from komber.worker import Worker


def queue_handler(exchange, **kwargs):
    def wrapper(func):
        kwargs['exchange'] = exchange
        kwargs['handler'] = func
        Worker.queues.append(kwargs)
        return func
    return wrapper

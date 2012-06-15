#-*- coding: utf-8 -*-
import unittest
from kombu import Exchange
from komber.decorators import queue_handler
from komber.worker import Worker



class TestLoading(unittest.TestCase):

    def setUp(self):
        self.exchange = Exchange('amq.topic', type='topic')

        @queue_handler(exchange=self.exchange, queue_name='_test_queue_handler',
                       routing_key='_test_queue_handler')
        def _test_queue_handler(body, message):
            pass

        self._test_queue_handler=  _test_queue_handler

    def test_queue_handler_loading(self):
        self.assertEqual(Worker.queues, [{'exchange': self.exchange,
                                          'handler': self._test_queue_handler,
                                          'queue_name': '_test_queue_handler',
                                          'routing_key': '_test_queue_handler'}])

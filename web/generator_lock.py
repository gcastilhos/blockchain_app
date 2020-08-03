"""
Provides locking mechanism for the data generator.
"""
import threading
import unittest
from web.queue_manager import event_generator


class GeneratorLock:

    def __init__(self, generator):
        self.lock = threading.Lock()
        self.generator = generator

    def next(self):
        self.lock.acquire()
        try:
            return next(self.generator)
        except StopIteration:
            return None
        finally:
            self.lock.release()


class TestGeneratorLock(unittest.TestCase):

    def test_generator_1_to_100(self):
        generator = GeneratorLock((i ** 5 for i in range(100)))
        number_list = []
        for i in range(101):
            number_list.append(generator.next())
        self.assertEqual(len(number_list), 101)
        self.assertIsNone(number_list[-1], None)
        self.assertEqual(number_list[-2], 99 ** 5)

    def test_generator_with_events_queue(self):
        event_queue = event_generator()
        generator = GeneratorLock(event_queue)
        result = generator.next()
        self.assertTrue(isinstance(result, str))

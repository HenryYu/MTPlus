__author__ = 'yuziyuan'

from lib.event.Event import Event, Temp1, Temp2
import unittest


class EventTest(unittest.TestCase):
    def test_on(self):
        e1 = Temp1()
        e2 = Temp2()

        self.assertEqual(e1.and_happen('Temp2'), True)
        pass

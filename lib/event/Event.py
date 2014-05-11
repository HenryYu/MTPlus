__author__ = 'yuziyuan'

from abc import ABCMeta, abstractmethod
from lib.context import Context
from lib.infrastructure.annotation import except_happen

class Event:
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    def is_correct(self):
        if(self.cal_status()):
            self.action() #todo:     异步操作, event driven
            return True

        return False

    @abstractmethod
    def cal_status(self):
        pass

    @abstractmethod
    def action(self):
        pass

    def do(self, action_name, *args):
        pass

    def and_happen(self, event_name, time=0):
        package_path = 'lib.event.Event'
        module_ = __import__(package_path).event.Event
        # todo: package path
        class_ = getattr(module_, event_name)
        event = class_()
        if(event.cal_status()):
            return True

    def check_rule_conflict(self):
        print 'check successful'

    def print_sum(self):
        """
            print whatever rules relative with the event
        """
        pass






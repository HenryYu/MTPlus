__author__ = 'yuziyuan'

from abc import ABCMeta, abstractmethod

class Action:
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def do(self, *args):
        pass


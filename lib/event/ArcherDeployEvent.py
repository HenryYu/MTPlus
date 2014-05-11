__author__ = 'yuziyuan'

from Event import Event
from lib.infrastructure.annotation import except_happen


class ArcherDeployEvent(Event):
    @except_happen('test')
    def cal_status(self):
        return True

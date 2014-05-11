__author__ = 'yuziyuan'

from Event import Event
from annotation import except_happen

class DeployEvent(Event):

    @except_happen('ArcherDeployEvent')
    def cal_status(self):
        return True

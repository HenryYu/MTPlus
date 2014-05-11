__author__ = 'yuziyuan'

import Event

class cpu_beyond_90(Event):

    def get_status(self):
        queryClient = None #todo: fake query client
        cpu = queryClient.queryCpu()
        if(cpu > 90):
            self.action()
            return True

    def action(self):
        super.do

class cpu_beyond_80(Event):
    def get_status(self):
        queryClient = None #todo: fake query client
        cpu = queryClient.queryCpu()
        if(cpu > 90):
            self.action()
            return True

    def action(self):
        pass



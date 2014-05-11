__author__ = 'yuziyuan'

import Event
from lib.infrastructure.annotation import except_happen
from lib.context import Context as c

class Temp1(Event):
    def get_status(self):
        return True

    @except_happen(c.E_Temp2) # demo, fake logic
    def action(self):
        if(self.and_happen(c.E_Temp2)):
            self.do(c.A_Alert, 'henry', 'msg')
            self.do(c.A_Info, 'msg')
            self.do(c.A_Plan, 'plan_id')
        if(self.and_happen('Temp3')):
            self.do('plan', 'plan_id')


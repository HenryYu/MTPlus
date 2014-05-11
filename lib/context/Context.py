__author__ = 'yuziyuan'

E_Deploy= 'DeployEvent'
E_ArcherDeploy= 'ArcherDeployEvent'
E_Temp1 = 'Temp1'
E_Temp2 = 'Temp2'

A_Alert = 'AlertAction'
A_Info = 'InfoAction'
A_Plan = 'PlanAction'

# E_DeployEvent = ('DeployEvent', 'DeployEvent')
# E_ArcherDeployEvent = ('ArcherDeployEvent', 'ArcherDeployEvent')
# E_Temp1 = ('Temp1', 'Event')
# E_Temp2 = ('Temp2', 'Event')
# E_Temp2 = ('Temp2', 'Event', 'lib.event')

D_TestAction = 'TestAction'


class _const:
    class ConstError(TypeError):pass
    def __setattr__(self, name, value):
        if self.__dict__.has_key(name):
            raise self.ConstError, "Can't rebind const (%s)" %name
        self.__dict__[name]=value
import sys
sys.modules[__name__] = _const()


class Context:
    def __init__(self):
        pass



监控+
=======

概述
--------
#目标
补充监控策略层采集组件不全的不足，例如：服务部署、机器挂载、机器故障和流量损失等外界系统的问题
补充监控策略层逻辑扩展方面的不足，提供复杂我
提供策略脚本书写的sdk，方便用户快速书写脚本
提供sdk的开放框架，方便高阶用户做组件扩展
根据脚本中的监控策略生成监控流，配合服务模块，形成业务稳定图谱
引入监控行为的概念，封闭报警、故障处理和预案处理的动作

概念
----------------
监控+存在如下几个概念：事件和行为，其中事件的触发对应触发策略，简称事件策略；行为的触发对应行为触发策略，简称行为策略

#事件
事件对应概念监控中的监控策略，传统的监控项采集数据，通过事件触发策略判断该事件是否正常，如果异常则进入行为判断逻辑，选择是否发送报警、是否执行预案

#事件触发策略
事件触发策略，除了包含现有监控项的判断逻辑外，还包含脚本实现的关于**时间段**，**频率**和**处理趋势**这样复杂的判断条件；也可以包含监控项组合

#行为
事件符合触发条件后，就会进入行为策略判断的逻辑，行为包含：短信报警、逐级通告和故障执行等，并且能够支撑用户扩展自定义的行为

#行为策略
一个策略只对应一个行为，策略内包含与操作的事件，策略和策略之间只能是或操作关系。一个事件如果不对应行为策略，则事件发生异常什么都不执行，或者附带在其他策略中。最终能够通过监控图谱得到事件的实际执行信息。

行为策略包含异常状况的策略，即其他事件发生后，该事件即使发生异常，也可以忽略不计，例如：上线屏蔽操作单；机器未挂载时候，不需要报警等。因为该类策略，对应的行为为空，所以可以通过配置实现。


程序结构
------------------
#包结构
由监控+提供标准lib包，lib包的目录结构如下：
	lib
		action
			BaseAction
			AlertAction
			InfoAction
			PlanAction
		event
			BaseEvent
			CPUEvent
			MemEvent
			NetworkEvent
			VisitFlowEvent
			DeployEvent
		infrastructure
			annotation
			persistence
			log
		context
			Context

	src
		szop
			rp
				action
				event
				infrastructure
				context
			i18n
				action
				event
				infrastructure
				context

监控图谱
----------------

通过一个事件中注册的行为触发策略，能够准确获取事件和事件之间的关系，通过对关系的整理，可以有效避免事件之间相互引用产生策略冲突，避免错误定义策略；并且可以形成监控图谱，配合服务和模块上下游图，可以形成产品线稳定性的全景图

###策略冲突：
	class cpu_beyond_90_Event:
		@except_happen('ssh_conn_time_out_Event')
		action():
			pass

	class ssh_conn_time_out_Event：
		action():
			if(self.and_happen('cpu_beyond_90_Event')):
				alert('ssh timeout alarm!')


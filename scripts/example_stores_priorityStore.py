#!/usr/bin/env python

import simpy


env = simpy.Environment()
issues = simpy.PriorityStore(env)


def inspector(env, issues):
    for issue in [simpy.PriorityItem('P2', '#0000'),
                  simpy.PriorityItem('P0', '#0001'),
                  simpy.PriorityItem('P3', '#0002'),
                  simpy.PriorityItem('P1', '#0003')]:
        yield env.timeout(1)
        print(env.now, 'log', issue)
        yield issues.put(issue)


def maintainer(env, issues):
    while True:
        yield env.timeout(3)
        issue = yield issues.get()
        print(env.now, 'repair', issue)


_ = env.process(inspector(env, issues))
_ = env.process(maintainer(env, issues))

env.run()

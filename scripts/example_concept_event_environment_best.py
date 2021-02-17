#!/usr/bin/env python

import simpy


def example(env):
    value = yield env.timeout(2, value=2)
    print('now=%d, value=%d' % (env.now, value))

#real-time simulation, the code delays 2s after running
env = simpy.RealtimeEnvironment()
p = env.process(example(env))
env.run()

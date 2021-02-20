#!/usr/bin/env python


import simpy


data = []
def test_process(env, data):
    val = 0
    for i in range(5):
        val += env.now
        data.append(val)   # Collect data
        yield env.timeout(1)


env = simpy.Environment()
p = env.process(test_process(env, data))
env.run(p)
print('Collected', data)

#!/usr/bin/env python

# https://simpy.readthedocs.io/en/latest/topical_guides/simpy_basics.html

import simpy

def example(env):
    event = simpy.events.Timeout(env, delay=1, value=100)
    value = yield event
    print('now=%d, value=%d' % (env.now, value))

env = simpy.Environment()
example_gen = example(env)
p = simpy.events.Process(env, example_gen)

env.run()

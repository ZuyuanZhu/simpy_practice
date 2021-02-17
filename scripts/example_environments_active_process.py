#!/usr/bin/env python

import simpy


def subfunc(env):
    print(env.active_process)


def my_proc(env):
    while True:
        print(env.active_process)
        subfunc(env)
        yield env.timeout(1)


env = simpy.Environment()
p1 = env.process(my_proc(env))
env.active_process
env.step()
env.active_process

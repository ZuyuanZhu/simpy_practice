#!/usr/bin/env python


import simpy
from collections import namedtuple


Machine = namedtuple('Machine', 'size, duration')
m1 = Machine(1, 2)
m2 = Machine(2, 1)
env = simpy.Environment()
machine_shop = simpy.FilterStore(env, capacity=2)
machine_shop.items = [m1, m2]


def user(name, env, ms, size):
    machine = yield ms.get(lambda machine: machine.size == size)
    print(name, 'got', machine, 'at', env.now)
    yield env.timeout(machine.duration)
    yield ms.put(machine)
    print(name, 'released', machine, 'at', env.now)


user_names = ['Xu', 'Zhu', 'Li']
users = [env.process(user(user_names[i], env, machine_shop, (i % 2)+1))
         for i in range(3)]
env.run()

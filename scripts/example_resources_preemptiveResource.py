#!/usr/bin/env python


import simpy


def resource_user(name, env, resource, wait, prio):
    yield env.timeout(wait)
    with resource.request(priority=prio) as req:
        print(f'{name} requesting at {env.now} with priority={prio}')
        yield req
        print(f'{name} got resource at {env.now}')
        try:
            yield env.timeout(3)
        except simpy.Interrupt as interrupt:
            by = interrupt.cause.by
            usage = env.now - interrupt.cause.usage_since
            print(f'{name} got preempted by {by} at {env.now}'
                  f' after {usage}')


env = simpy.Environment()
res = simpy.PreemptiveResource(env, capacity=1)
p1 = env.process(resource_user('Xu', env, res, wait=0, prio=0))
p2 = env.process(resource_user('Li', env, res, wait=1, prio=0))
p3 = env.process(resource_user('Zhu', env, res, wait=2, prio=-1))
env.run()

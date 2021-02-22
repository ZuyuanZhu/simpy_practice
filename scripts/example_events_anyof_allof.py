#!/usr/bin/env python

import simpy
from simpy.events import AnyOf, AllOf, Event


def test_condition(env):
    t1, t2 = env.timeout(1, value='spam'), env.timeout(2, value='eggs')
    ret = yield t1 | t2
    print(ret)
    assert ret == {t1: 'spam'}

    t1, t2 = env.timeout(1, value='spam'), env.timeout(2, value='eggs')
    ret = yield t1 & t2
    assert ret == {t1: 'spam', t2: 'eggs'}

    # You can also concatenate & and |
    e1, e2, e3 = [env.timeout(i) for i in range(3)]
    yield (e1 | e2) & e3
    assert all(e.processed for e in [e1, e2, e3])


def fetch_values_of_multiple_events(env):
    t1, t2 = env.timeout(1, value='spam'), env.timeout(2, value='eggs')
    r1, r2 = (yield t2 & t1).values()
    assert r1 == 'eggs' and r2 == 'spam'


env = simpy.Environment()
proc = env.process(fetch_values_of_multiple_events(env))
env.run()


# As a shorthand for AllOf and AnyOf, you can also use the logical operators & (and) and | (or):
# env = simpy.Environment()
# proc = env.process(test_condition(env))
# env.run()


#
# env = simpy.Environment()
# events = [Event(env) for i in range(3)]
# a = AnyOf(env, events)
# print(a)
# b = AllOf(env, events)
# print(b)



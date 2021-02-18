import simpy


def sub(env):
    yield env.timeout(1)
    return 23


def parent(env):
    ret = yield env.process(sub(env))
    return ret


env = simpy.Environment()
event1 = parent(env)
event2 = env.process(event1)
i = env.run()
print(i)

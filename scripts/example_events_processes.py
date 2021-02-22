import simpy


def sub(env):
    yield env.timeout(1)
    print(f'sub return at {env.now}')
    return 23


def parent(env):
    print(f'parent at {env.now}')
    ret = yield env.process(sub(env))
    print(f'return ret={ret} at {env.now}')
    return ret


env = simpy.Environment()
event1 = parent(env)
event2 = env.process(event1)
i = env.run()
print(i)

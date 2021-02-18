import simpy


from simpy.util import start_delayed


def sub(env):
    yield env.timeout(1)
    return 23


def parent(env):
    sub_proc = yield start_delayed(env, sub(env), delay=3)
    ret = yield sub_proc
    return ret


env = simpy.Environment()
env.run(env.process(parent(env)))

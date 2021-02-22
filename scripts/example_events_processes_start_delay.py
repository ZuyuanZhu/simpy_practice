import simpy


from simpy.util import start_delayed


def sub(env):
    print(f'sub start at {env.now}')
    yield env.timeout(1)        # timeout(1) means, the code after this line will be resumed after 1 unit time
    print(f'sub ret at {env.now}')
    return 23


def parent(env):
    print(f'parent start at {env.now}')
    sub_proc = yield start_delayed(env, sub(env), delay=3)      # delay 3 unit time, then call sub(env)
    print(f'sub_proc start at {env.now}')
    ret = yield sub_proc  # this yield is necessary to get the sub(env) return
    print(f'parent ret start at {env.now} ret={ret}')
    return ret


env = simpy.Environment()
env.run(env.process(parent(env)))

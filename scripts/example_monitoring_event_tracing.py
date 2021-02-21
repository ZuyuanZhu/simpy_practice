#!/usr/bin/env python
# TODO

from functools import partial, wraps
import simpy


def trace(env, callback):
    """ Replace the 'step()' method of 'env' with a tracing function that
        calls 'callback' with an events time, priority, ID and its instance
        just before it is processed.
    :param env:
    :param callback:
    :return:
    """
    def get_wrapper(env_step, callback):
        """ Generate the wrapper for env.step().
        :param env_step:
        :param callback:
        :return:
        """
        @wraps(env_step)
        def tracing_step():
            """  Call 'callback' for the next event if one exit before calling
                 'env.step()'
            :return:
            """
            if len(env._queue):
                t, prio, eid, event = env._queue[0]
                callback(t, prio, eid, event)
            return env_step()
        return tracing_step

    env.step = get_wrapper(env.step, callback)


def monitor(data, t, prio, eid, event):
    data.append((t, eid, type(event)))

def test_process(env):
    yield env.timeout(1)

data = []
monitor = partial(monitor, data)
env = simpy.Environment()
trace(env, monitor)
p = env.process(test_process(env))
env.run(until=p)
for d in data:
    print(d)

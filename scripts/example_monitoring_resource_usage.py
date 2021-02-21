#!/usr/bin/env python
# TODO

import simpy
from functools import partial, wraps


def patch_resource(resource, pre=None, post=None):
    """
    :param resource: Patch 'resource' so it calls the callable 'pre' before each put/get/request/release
    :param pre:      operation and the callable 'post' after each operation. The only argument to these
    :param post:     functions is the resource instance
    :return:
    """
    def get_wrapper(func):
        # Generate a wrapper for put/get/request/release
        @wraps(func)
        def wrapper(*args, **kwargs):
            # This is the actual wrapper
            # Call "pre" callback
            if pre:
                pre(resource)

            # Perform actual operation
            ret = func(*args, **kwargs)

            # Call "post" callback
            if post:
                post(resource)

            return ret
        return wrapper

    # Replace the original operations with our wrapper
    for name in ['put', 'get', 'request', 'release']:
        if hasattr(resource, name):
            setattr(resource, name, get_wrapper(getattr(resource, name)))


def monitor(data, resource):
    """  This is our monitor callback
    :param data:
    :param resource:
    :return:
    """
    item = (
        resource._env.now,   # The current simulation time
        resource.count,      # The number of users
        len(resource.queue)  # The number of queued processes
    )
    data.append(item)


def test_process(env, res):
    with res.request() as req:
        yield req
        yield env.timeout(1)


env = simpy.Environment()
res = simpy.Resource(env, capacity=1)
data = []
# Bind 'data' as first argument to monitor()
# see https://docs.python.org/3/library/functools.html#functools.partial
monitor = partial(monitor, data)
patch_resource(res, post=monitor) # Patches (only) this resource instance
p = env.process(test_process(env, res))
env.run(p)
print(data)

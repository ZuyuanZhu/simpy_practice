#!/usr/bin/env python


import simpy


def print_stats(res):
    print(f'{res.count} of {res.capacity} slots are allocated.')
    print(f'  Users: {res.users}')
    print(f'  Queued events: {res.queue}')


def user(_res):
    print_stats(_res)
    with _res.request() as req:
        yield req
        print_stats(_res)
    print_stats(_res)


env = simpy.Environment()
res = simpy.Resource(env, capacity=1)
procs = [env.process(user(res)), env.process(user(res))]
# proc = env.process(user(res))
env.run()

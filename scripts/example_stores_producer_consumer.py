#!/usr/bin/env pyghon


import simpy


def producer(env, store):
    for i in range(100):
        print(f'Before producer {i} yield timeout {env.now}')
        yield env.timeout(2)
        print(f'After producer {i} yield timeout {env.now}')
        yield store.put(f'spam {i}')
        print(f'Produced spam at', env.now)


def consumer(name, env, store):
    while True:
        print(f'Before consumer {name} yield timeout {env.now}')
        yield env.timeout(1)
        print(f'After consumer {name} yield timeout {env.now}')
        print(name, 'requesting spam at', env.now)
        item = yield store.get()
        print(name, 'got', item, 'at', env.now)


env = simpy.Environment()
store = simpy.Store(env, capacity=2)
prod = env.process(producer(env, store))
consumer_names = ['Xu', 'Zhu']
consumers = [env.process(consumer(i, env, store)) for i in consumer_names]
env.run(until=5)

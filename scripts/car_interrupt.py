#!/usr/bin/env python

# https://simpy.readthedocs.io/en/latest/simpy_intro/process_interaction.html#interrupting-another-process

# AttributeError: 'NoneType' object has no attribute 'action' - class Car(object), not def Car(object)

import simpy


class Car(object):
    def __init__(self, env):
        self.env = env
        self.action = env.process(self.run())

    def run(self):
        while True:
            print('Start parking and charging at %d' % self.env.now)
            charge_duration = 5
            # We may get interrupted while charging the battery
            try:
                yield self.env.process(self.charge(charge_duration))
            except simpy.Interrupt:
                # When we received an interrupt, we stop charging and 
                # switch to the "driving" state
                print('Was interrupted. Hope, the battery is full enough ...')

            print ('Start driving at %d' % self.env.now)
            trip_duration = 2
            yield self.env.timeout(trip_duration)

    def charge(self, duration):
        yield self.env.timeout(duration)


def driver(env, car):
    yield env.timeout(3)
    car.action.interrupt()


env = simpy.Environment()
car = Car(env)
env.process(driver(env, car))
env.run(until=15)

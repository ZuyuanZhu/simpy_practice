#!/usr/bin/env python


import simpy


def my_callback(event):
    print('Called back from', event)


env = simpy.Environment()
event = env.event()
event.callbacks.append(my_callback(event))
event.callbacks


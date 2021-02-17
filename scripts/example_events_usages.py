#!/usr/bin/env python
# https://simpy.readthedocs.io/en/latest/topical_guides/events.html
import simpy


class School:
    def __init__(self, env):
        self.env = env
        self.class_ends = env.event()
        self.pupil_procs = [env.process(self.pupil()) for i in range(3)]
        self.bell_proc = env.process(self.bell())

    def bell(self):
        for j in range(2):
            yield self.env.timeout(45)
            self.class_ends.succeed()
            self.class_ends = self.env.event()
            print()

    def pupil(self):
        for k in range(2):
            print(r'\o/', end='')
            yield self.class_ends


env = simpy.Environment()
school = School(env)
env.run()

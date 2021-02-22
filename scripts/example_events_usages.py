#!/usr/bin/env python
# https://simpy.readthedocs.io/en/latest/topical_guides/events.html
import simpy


class School:
    def __init__(self, env):
        self.env = env
        self.class_ends = env.event()
        self.class_begins = env.event()
        self.pupil_procs = [env.process(self.pupil(i)) for i in range(3)]
        self.bell_proc = env.process(self.bell())

    def bell(self):
        for j in range(4):
            yield self.env.timeout(45)
            self.class_ends.succeed()
            self.class_ends = self.env.event()  # last class ends, reassign a new class_end event
            print(f' bell at {env.now}')

    def pupil(self, i):
        for c in range(4):  # k is the number of classes: Math, English, Art...
            print(f'\o/ pupil({i}) c={c} at {env.now}', end=' || ')
            yield self.class_ends
            # yield env.timeout(1)


env = simpy.Environment()
school = School(env)
env.run()

"""
output:
\o/ pupil0 k=0 at 0
\o/ pupil1 k=0 at 0
\o/ pupil2 k=0 at 0
\o/ pupil0 k=1 at 1
\o/ pupil1 k=1 at 1
\o/ pupil2 k=1 at 1

thoughts: 
1.  env.process(self.pupil(0)) env.process(self.pupil(1)) env.process(self.pupil(2)) 
    are three parallel processes, when they have for loop function, they will loop together
    rather than one loop over and another follows. 
2. All processes happen at the same time at 0, so the first output of all the processes are 
    printed out together at time=0
"""

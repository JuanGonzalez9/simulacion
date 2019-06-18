import numpy
import random


class Client(object):

    min_time = {
        '1': 65,
        '2': 45,
        '3': 70
    }

    max_time = {
        '1': 85,
        '2': 75,
        '3': 110
    }

    def __init__(self, env):
        self.env = env
        self.type = numpy.random.choice(['1', '2', '3'], p=[0.6, 0.25, 0.15])

    def pay(self, checkout):
        yield self.env.process(checkout.serve(self))
        print("%.2f Client type %s attended" % (self.env.now, self.type))

    def get_pay_duration(self):
        return random.randint(self.min_time[self.type], self.max_time[self.type])
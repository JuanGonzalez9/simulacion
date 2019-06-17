import random
import simpy
import numpy


instructions_count = 1000
arrival_rate = 250


class Client(object):

    pay_duration = {
        '1': 60,
        '2': 10
    }

    def __init__(self, env):
        self.env = env
        self.type = numpy.random.choice(['1', '2'], p=[0.6, 0.4])

    def pay(self, cashier):
	# Automatic release
        with cashier.request() as req:
            yield req
            yield self.env.timeout(self.get_pay_duration())
            irAMemoria = random.random()
            if irAMemoria < 0.65:
                # Situacion A --> aprox 1320 k
                #yield self.env.timeout(self.get_memory_time())
                # Situacion B --> 650 k aprox
                estaEnCache = random.random()
                if estaEnCache < 0.6:
                    yield self.env.timeout(self.get_cache_time())
                else:
                    yield self.env.timeout(self.get_memory2_time())


	# Manual release
        # request = cashier.request()
        # yield request
        # yield self.env.timeout(self.get_pay_duration())
        # cashier.release(request)

        print("%.2f Client type %s attended" % (self.env.now, self.type))

    def get_pay_duration(self):
        return random.expovariate(1.0/self.pay_duration[self.type])
    
    def get_memory_time(self):
        return random.expovariate(1.0/2000)
    
    def get_cache_time(self):
        return random.expovariate(1.0/500)

    def get_memory2_time(self):
        return random.expovariate(1.0/1500)


def generate_clients(environment, count, interval):
    cashier = simpy.Resource(env, capacity = 1)
    for i in range(count):
        client = Client(env)
        environment.process(client.pay(cashier))
        t = random.expovariate(1.0 / interval)
        yield environment.timeout(t)


env = simpy.Environment()
env.process(generate_clients(env, instructions_count, arrival_rate))
env.run()
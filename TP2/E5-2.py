import random
import simpy

from Checkout import Checkout
from Client import Client


client_count = 10000
arrival_rate = 45
cashier_count = 6


def generate_clients(environment, count, interval, checkout):
    for i in range(count):
        client = Client(env)
        environment.process(client.pay(checkout))
        t = random.expovariate(1.0 / interval)
        yield environment.timeout(t)


env = simpy.Environment()
checkout = Checkout(env, cashier_count)
env.process(generate_clients(env, client_count, arrival_rate, checkout))
env.run()
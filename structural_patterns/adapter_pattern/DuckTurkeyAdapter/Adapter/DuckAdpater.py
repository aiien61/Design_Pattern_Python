from DuckTurkeyAdapter.Adaptee.Duck import Duck
from DuckTurkeyAdapter.Adaptee.Turkey import Turkey
import random

class DuckAdapter(Turkey):
    def __init__(self, duck: Duck):
        self.duck = duck

    def gobble(self):
        self.duck.quack()

    def fly(self):
        if random.randint(0, 5) == 0:
            self.duck.fly()

from DuckTurkeyAdapter.Adaptee.Duck import Duck
from DuckTurkeyAdapter.Adaptee.Turkey import Turkey


class TurkeyAdapter(Duck):
    def __init__(self, turkey: Turkey):
        self.turkey = turkey

    def quack(self):
        self.turkey.gobble()

    def fly(self):
        for i in range(5):
            self.turkey.fly()
    
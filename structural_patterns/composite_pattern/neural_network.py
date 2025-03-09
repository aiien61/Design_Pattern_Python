from abc import ABC
from collections.abc import Iterable
from typing import List

class Connectable(Iterable, ABC):
    def connect_to(self, other):
        if self == other:
            return None
        
        for s in self:
            for o in other:
                s.outputs.append(o)
                o.outputs.append(s)

class Neuron(Connectable):
    def __init__(self, name: str):
        self.name = name
        self.inputs: List["Neuron"] = []
        self.outputs: List["Neuron"] = []

    def __iter__(self):
        yield self

    def __repr__(self):
        return f"{self.name}, {len(self.inputs)} inputs, {len(self.outputs)} outputs."

class NeuronLayer(list, Connectable):
    def __init__(self, name: str, count: int):
        super().__init__()
        self.name = name
        for x in range(0, count):
            self.append(Neuron(f"{name} - {x}"))
    
    def __repr__(self):
        return f"{self.name} with {len(self)} neurons"
    
if __name__ == "__main__":
    neuron1 = Neuron('n1')
    neuron2 = Neuron('n2')
    layer1 = NeuronLayer('L1', 3)
    layer2 = NeuronLayer('L2', 5)

    neuron1.connect_to(neuron2)
    neuron1.connect_to(layer1)
    layer1.connect_to(neuron2)
    layer1.connect_to(layer2)

    print(neuron1)
    print(neuron2)
    print(layer1)
    print(layer2)

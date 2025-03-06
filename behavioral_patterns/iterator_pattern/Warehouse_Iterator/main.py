from abc import ABC, abstractmethod
from typing import List, Any
from rich import print 

# Define iterator interface
class InventoryIterator(ABC):
    @abstractmethod
    def has_next(self) -> bool:
        raise NotImplementedError
    
    @abstractmethod
    def next(self) -> Any:
        raise NotImplementedError
    
# Define aggregate interface
class InventoryAggregate(ABC):
    @abstractmethod
    def create_iterator(self) -> InventoryIterator:
        raise NotImplementedError

# Concrete inventory class
class InventoryItem:
    def __init__(self, name: str, quantity: int, safety_stock: int):
        self.name = name
        self.quantity = quantity
        self.safety_stock = safety_stock
    
    def is_low_stock(self) -> bool:
        return self.quantity < self.safety_stock
    
    def __repr__(self) -> str:
        return f"{self.name}: 數量={self.quantity}, 安全庫存={self.safety_stock}"

# Concrete iterator
class WarehouseIterator(InventoryIterator):
    def __init__(self, items: List[InventoryItem]):
        self.items = items
        self.index: int = 0

    def has_next(self) -> bool:
        return self.index < len(self.items)
    
    def next(self) -> InventoryItem:
        if self.has_next():
            item: InventoryItem = self.items[self.index]
            self.index += 1
            return item
        raise StopIteration("沒有更多庫存項了")
    
# Concrete warehouse aggregator
class Warehouse(InventoryAggregate):
    def __init__(self):
        self.items: List[InventoryItem] = []

    def add_item(self, item: InventoryItem) -> None:
        self.items.append(item)
        return None
    
    def create_iterator(self) -> InventoryIterator:
        return WarehouseIterator(self.items)
    
# Demo
def main():
    # Initialise warehouse
    warehouse = Warehouse()
    warehouse.add_item(InventoryItem("螺絲", 50, 100))
    warehouse.add_item(InventoryItem("螺母", 200, 150))
    warehouse.add_item(InventoryItem("輪胎", 10, 20))

    # Create iterator and traverse all inventory
    iterator = warehouse.create_iterator()
    print("庫存檢查報告:")
    while iterator.has_next():
        item = iterator.next()
        print(f"- {item}", end="")
        if item.is_low_stock():
            print("[bold red] [低於安全庫存！] [/bold red]")
        else:
            print()

if __name__ == "__main__":
    main()

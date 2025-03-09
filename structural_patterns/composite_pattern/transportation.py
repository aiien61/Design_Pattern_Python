"""
假設一個物流公司需要計算其運輸網路的總成本，網路中既有單獨的運輸工具（如卡車），也有由多個工具組成的車隊。

在供應鏈管理中，假設我們需要管理一個物流網路，其中包括單個運輸單位（如卡車）和運輸組合（如車隊或多式聯運系統）。
每個運輸單位有成本，而組合單位（如車隊）由多個子單位組成。
我們希望以統一的方式計算整個物流網路的總成本，並能動態添加或移除單位。
Composite模式非常適合這種“部分-整體”的層次結構。
"""

from abc import ABC, abstractmethod
from typing import List

# Define component interface
class TransportUnit(ABC):
    @abstractmethod
    def get_cost(self) -> float:
        raise NotImplementedError
    
    # 子節點管理方法
    def add(self, unit: 'TransportUnit') -> None:
        raise NotImplementedError
    
    def remove(self, unit: 'TransportUnit') -> None:
        raise NotImplementedError
    
# 葉子類：單個運輸工具
class Truck(TransportUnit):
    def __init__(self, name: str, cost: float):
        self.name = name
        self.cost = cost
    
    def get_cost(self) -> float:
        return self.cost
    
    def __repr__(self) -> str:
        return f"{self.name} (成本: {self.cost})"
    
# 組合類：車隊或運輸網路
class Fleet(TransportUnit):
    def __init__(self, name: str):
        self.name = name
        self.units: List[TransportUnit] = []

    def add(self, unit: TransportUnit) -> None:
        self.units.append(unit)

    def remove(self, unit: TransportUnit) -> None:
        if unit in self.units:
            self.units.remove(unit)

    def get_cost(self) -> float:
        total_cost: float = 0
        for unit in self.units:
            total_cost += unit.get_cost()
        return total_cost
    
    def __repr__(self) -> str:
        return f"{self.name} (包含 {len(self.units)} 個單位)"

# Demo
def main():
    # 創建單個運輸工具（葉子）
    truck1 = Truck("卡車 A", 1_000.0)
    truck2 = Truck("卡車 B", 1_500.0)
    truck3 = Truck("卡車 C", 1_200.0)
    
    # 創建車隊（組合）
    city_fleet = Fleet("城市車隊")
    city_fleet.add(truck1)
    city_fleet.add(truck2)

    # 創建更高層次的運輸網路
    regional_network = Fleet("區域運輸網路")
    regional_network.add(city_fleet)
    regional_network.add(truck3)

    # 客戶端統一處理
    print("物流網路結構：")
    print(f"- {regional_network}")
    print(f"  - {city_fleet}")
    print(f"    - {truck1}")
    print(f"    - {truck2}")
    print(f"  - {truck3}")
    print(f"總成本: {regional_network.get_cost()}")
    
    # 動態移除單位
    city_fleet.remove(truck2)
    print("\n移除卡車 B 後:")
    print(f"總成本: {regional_network.get_cost()}")

if __name__ == "__main__":
    main()

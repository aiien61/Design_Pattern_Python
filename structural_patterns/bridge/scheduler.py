"""
假設有多個 產品類型（如手機、筆電），而每個產品可以在不同的 排程系統（如 ERP、MES） 上執行生產排程。

若直接硬編進每個產品與排程系統的所有組合，會造成類別爆炸：
例如：ERPPhoneScheduler, MESPhoneScheduler, ERPLaptopScheduler, MESLaptopScheduler...

可以用 Bridge 模式 來分離：
- 抽象層：產品排程邏輯（ProductScheduler）
- 實作層：排程系統（SchedulingSystem）


ProductScheduler（抽象）────────┐
   ▲                           │
   ├─ PhoneScheduler           │   → ERPSystem（實作）
   └─ LaptopScheduler          │   → MESSystem（實作）
                               ↓
                    SchedulingSystem（介面）

"""

import abc

# Implementor (Scheduling System)
class SchedulingSystem(abc.ABC):
    @abc.abstractmethod
    def schedule(self):
        pass

# Concrete Implementor
class ERPSystem(SchedulingSystem):
    def schedule(self, product_name: str):
        return f"使用 ERP 系統為 {product_name} 排程"

# Concrete Implementor
class MESSystem(SchedulingSystem):
    def schedule(self, product_name):
        return f"使用 MES 系統為 {product_name} 排程"

# Abstraction (Product Scheduler)
class ProductScheduler:
    def __init__(self, system: SchedulingSystem):
        self.system = system
    
    def run_schedule(self):
        pass

# Refined Abstraction (different scheduler for different products)
class PhoneScheduler(ProductScheduler):
    def run_schedule(self):
        return self.system.schedule("手機")

# Refined Abstraction (different scheduler for different products)
class LaptopScheduler(ProductScheduler):
    def run_schedule(self):
        return self.system.schedule("筆電")
    
if __name__ == "__main__":
    erp = ERPSystem()
    mes = MESSystem()

    phone_scheduler_erp = PhoneScheduler(erp)
    laptop_scheduler_mes = LaptopScheduler(mes)

    print(phone_scheduler_erp.run_schedule())
    print(laptop_scheduler_mes.run_schedule())


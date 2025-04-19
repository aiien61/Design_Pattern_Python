"""
A               | B
產品             | 手機
排程系統         | ERP
排程結果         | 
✅ 輸出欄位在這裡 | ← B5
"""

import xlwings as xw
from abc import ABC, abstractmethod

class SchedulingSystem(ABC):
    @abstractmethod
    def schedule(self): pass


class ERPSystem(SchedulingSystem):
    def schedule(self, product_name: str):
        return f"使用 ERP 系統為 {product_name} 排程完成"


class MESSystem(SchedulingSystem):
    def schedule(self, product_name: str):
        return f"使用 MES 系統為 {product_name} 排程完成"


class ProductScheduler:
    def __init__(self, system: SchedulingSystem):
        self.system = system

    def run_schedule(self):
        pass


class PhoneScheduler(ProductScheduler):
    def run_schedule(self):
        return self.system.schedule("手機")


class LaptopScheduler(ProductScheduler):
    def run_schedule(self):
        return self.system.schedule("筆電")

# Excel 入口函式
def run_schedule():
    wb = xw.Book.caller()
    sht = wb.sheets[0]
    product = sht.range("B2").value  # 產品類型
    system = sht.range("B3").value   # 排程系統

    impl = ERPSystem() if system == "ERP" else MESSystem()
    scheduler = PhoneScheduler(impl) if product == "手機" else LaptopScheduler(impl)

    result = scheduler.run_schedule()
    sht.range("B5").value = result

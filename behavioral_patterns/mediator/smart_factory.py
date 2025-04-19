"""
讓Mediator模式延伸到生產排程系統，實作一個模擬情境，讓各模組（排程器、工作站監控、訂單管理、倉儲管理）透過中介者協調溝通。

情境簡介：
在一間工廠中，當有新的訂單加入時，整個系統需要：

1. 排程器（Scheduler）排定生產時間
2. 工作站監控（WorkstationMonitor）檢查產線是否可用
3. 倉儲管理（InventoryManager）確認原料是否足夠
4. 最後由訂單管理（OrderManager）確認生產排程並回報訂單狀態
"""
# Mediator 介面與實作
class Mediator:
    def notify(self, sender, event, data=None):
        pass

class ProductionMediator(Mediator):
    def __init__(self):
        self.scheduler = None
        self.workstation = None
        self.inventory = None
        self.order_manager = None

    def notify(self, sender, event, data=None):
        if event == "new_order":
            print("📦 收到新訂單！開始排程流程")
            self.scheduler.create_schedule(data)
        elif event == "schedule_created":
            self.workstation.check_availability(data)
        elif event == "workstation_available":
            self.inventory.check_inventory(data)
        elif event == "inventory_checked":
            self.order_manager.confirm_order(data)

# 各模組（Colleague）
class OrderManager:
    def __init__(self, mediator):
        self.mediator = mediator
    
    def create_order(self, order):
        self.mediator.notify(self, "new_order", order)
    
    def confirm_roder(self, order):
        print(f"✅ 訂單 {order['id']} 確認生產，狀態更新為：進行中")

class Scheduler:
    def __init__(self, mediator):
        self.mediator = mediator

    def create_schedule(self, order):
        print(f"📅 為訂單 {order['id']} 建立生產排程")
        self.mediator.notify(self, "schedule_created", order)
    
class WorkstationMonitor:
    def __init__(self, mediator):
        self.mediator = mediator
    
    def check_availability(self, order):
        print(f"🛠️ 檢查工作站可用性：訂單 {order['id']} 可以開始生產")
        self.mediator.notify(self, "workstation_available", order)
    
class InventoryManager:
    def __init__(self, mediator):
        self.mediator = mediator
    
    def check_inventory(self, order):
        print(f"📦 檢查庫存是否足夠：訂單 {order['id']} 所需原料已備齊")
        self.mediator.notify(self, "Inventory_checked", order)

# 啟動系統模擬
def main():
    mediator = ProductionMediator()

    scheduler = Scheduler(mediator)
    workstation = WorkstationMonitor(mediator)
    inventory = InventoryManager(mediator)
    order_manager = OrderManager(mediator)

    # 設定各模組給 mediator 管理
    mediator.scheduler = scheduler
    mediator.workstation = workstation
    mediator.inventory = inventory
    mediator.order_manager = order_manager

    # 模擬一筆訂單
    order = {"id": "ORD001", "product": "WidgetA", "qty": 100}
    order_manager.create_order(order)

if __name__ == "__main__":
    main()

"""
生產排程情境：資源協調員（Mediator）

假設有三個子系統：
1. 訂單管理系統：負責新增或取消生產訂單
2. 產能管理系統：追蹤工作站是否有空閒
3. 排程器：根據訂單與產能排產

它們之間需要大量溝通，但不想彼此耦合太深。
➡️ 我們可以建立一個 排程中介者（Mediator） 來協調它們！
"""

# 定義各系統角色（Colleague）
class OrderSystem:
    def __init__(self, mediator):
        self.mediator = mediator
    
    def create_order(self, order_id):
        print(f"📝 訂單建立：{order_id}")
        self.mediator.notify(self, "new_order", order_id)

class CapacitySystem:
    def __init__(self, mediator):
        self.mediator = mediator
        self.free_stations = ["WS1", "WS2"]
    
    def check_availability(self):
        return len(self.free_stations) > 0
    
    def allocate(self):
        return self.free_stations.pop(0) if self.free_stations else None

class Scheduler:
    def __init__(self, mediator):
        self.mediator = mediator
    
    def schedule_order(self, order_id, station):
        print(f"📅 訂單 {order_id} 已排入工作站 {station}")

# 建立中介者（Mediator）
class SchedulingMediator:
    def __init__(self):
        self.order_system = OrderSystem(self)
        self.capacity_system = CapacitySystem(self)
        self.scheduler = Scheduler(self)

    def notify(self, sender, event, data):
        if event == "new_order":
            if self.capacity_system.check_availability():
                station = self.capacity_system.allocate()
                self.scheduler.schedule_order(data, station)
            else:
                print(f"❌ 沒有可用產能，訂單 {data} 排程失敗")
    
if __name__ == "__main__":
    mediator = SchedulingMediator()
    order_sys = mediator.order_system

    order_sys.create_order("A001")
    order_sys.create_order("A002")
    order_sys.create_order("A003")  # 模擬產能不足

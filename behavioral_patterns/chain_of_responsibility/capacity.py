"""
範例情境：生產排程請求的審核流程
在製造業中，當某個排程需求送出時，可能會經過以下節點審核：

✅ 生產能量審核（有機台嗎？）

✅ 物料庫存審核（有料嗎？）

✅ 人力資源審核（有工人嗎？）

若任一環節失敗，就會中止並回覆對應的錯誤。
"""

# 抽象 Handler
class Handler:
    def __init__(self):
        self.next = None
    
    def set_next(self, handler):
        self.next = handler
        return handler
    
    def handle(self, request):
        if self.next:
            return self.next.handle(request)
        return "✅ 所有條件通過，排程成功"
    
# 各種具體處理器
class CapacityCheck(Handler):
    def handle(self, request):
        if request.get("capacity_ok"):
            return super().handle(request)
        return "❌ 生產能量不足，無法排程"

class MaterialCheck(Handler):
    def handle(self, request):
        if request.get("material_ok"):
            return super().handle(request)
        return "❌ 物料不足，無法排程"
    
class WorkforceCheck(Handler):
    def handle(self, request):
        if request.get("workforce_ok"):
            return super().handle(request)
        return "❌ 工人不足，無法排程"

# 建立責任鏈
capacity = CapacityCheck()
material = MaterialCheck()
workforce = WorkforceCheck()

capacity.set_next(material).set_next(workforce)

if __name__ == "__main__":
    request1 = {
        "capacity_ok": True,
        "material_ok": True,
        "workforce_ok": True
    }

    request2 = {
        "capacity_ok": True,
        "material_ok": False,
        "workforce_ok": True
    }

    print("📝 案例 1 結果", capacity.handle(request1))
    print("📝 案例 2 結果", capacity.handle(request2))

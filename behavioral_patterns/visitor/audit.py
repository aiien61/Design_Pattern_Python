"""
供應鏈情境：貨品倉儲系統的統一稽核

📝 問題背景：
1. 系統中有不同類型的貨品（冷藏品、乾貨、液體原料…）。
2. 每種貨品需要不同的稽核方式（溫度、安全性、有效期等）。
3. 若將這些稽核邏輯都塞進貨品類別，維護困難，Visitor 模式可以解耦這些邏輯。

類別                        | 負責角色
Product                    | 元件基礎類別（Element）
FrozenProduct, DryGoods    | 具體元件
ProductAuditor             | 訪問者基礎類別（Visitor）
SafetyAuditor, TempAuditor | 具體訪問者
Warehouse                  | 負責管理與觸發訪問
"""

# Visitor 基類
class ProductAuditor:
    def visit_frozen(self, product): pass
    def visit_dry(self, product): pass

# 被訪問的元素基類
class Product:
    def accept(self, visitor: ProductAuditor): pass

# 冷藏品
class FrozenProduct(Product):
    def __init__(self, name: str, temperature: int):
        self.name = name
        self.temperature = temperature
    
    def accept(self, visitor: ProductAuditor):
        visitor.visit_frozen(self)

# 乾貨
class DryGoods(Product):
    def __init__(self, name, expiry_date):
        self.name = name
        self.expiry_date = expiry_date
    
    def accept(self, visitor: ProductAuditor):
        visitor.visit_dry(self)

# 稽核訪問者：溫度稽核
class TempAuditor(ProductAuditor):
    def visit_frozen(self, product: FrozenProduct):
        if product.temperature > -18:
            print(f"❌ {product.name} 溫度過高！({product.temperature}°C)")
        else:
            print(f"✅ {product.name} 溫度正常。")

    def visit_dry(self, product: DryGoods):
        print(f"✅ {product.name} 不需溫度稽核。")

# 稽核訪問者：有效期稽核
class ExpiryAudtior(ProductAuditor):
    def visit_frozen(self, product: FrozenProduct):
        print(f"✅ {product.name} 不執行有效期檢查。")

    def visit_dry(self, product: DryGoods):
        print(f"📅 {product.name} 有效期：{product.expiry_date}")

def main():
    inventory = [
        FrozenProduct("冷凍水餃", -15),
        DryGoods("乾燥麵粉", "2025-06-30")
    ]

    print("\n🌡️ 執行溫度稽核：")
    temp_checker = TempAuditor()
    for item in inventory:
        item.accept(temp_checker)
    
    print("\n📆 執行有效期稽核：")
    expiry_checker = ExpiryAudtior()
    for item in inventory:
        item.accept(expiry_checker)

if __name__ == "__main__":
    main()

"""
範例情境：出貨標籤產生器（供應鏈管理）
有成千上萬個要出貨的產品，每個都要生成一張「出貨標籤」，但：

相同型號的產品，共用標籤模板。
唯一差異是：序號 和 目的地地址。

不想為每一件商品都建立完整的標籤物件，這時就能用 Flyweight 模式 🎯
"""
from rich import print

# Flyweight (共享元件)：標籤模板
class LabelTemplate:
    def __init__(self, product_type, size, brand):
        self.product_type = product_type
        self.size = size
        self.brand = brand
    
    def render(self, serial_number, destination):
        return (
            f"[{self.brand}] {self.product_type} - 尺寸: {self.size}\n"
            f"序號: {serial_number} | 寄送地點: {destination}"
        )
    
# Flyweight Factory：用來共用模板物件
class LabelFactory:
    def __init__(self):
        self._templates = {}
    
    def get_template(self, product_type, size, brand):
        key = (product_type, size, brand)
        if key not in self._templates:
            print(f"🔧 建立新模板：{key}")
            self._templates[key] = LabelTemplate(*key)
        return self._templates[key]
    
# Client：產生標籤（含外部狀態）
def generate_shipping_labels(orders):
    factory = LabelFactory()
    labels = []

    for order in orders:
        template = factory.get_template(
            order["product_type"],
            order["size"],
            order["brand"]
        )
        label = template.render(order["serial_number"], order["destination"])
        labels.append(label)
    
    return labels

if __name__ == "__main__":
    orders = [
        {"product_type": "電動工具", "size": "M", "brand": "Bosch", "serial_number": "A001", "destination": "台中"}, 
        {"product_type": "電動工具", "size": "M", "brand": "Bosch", "serial_number": "A002", "destination": "台南"},
        {"product_type": "零件箱", "size": "S", "brand": "Bosch", "serial_number": "B001", "destination": "新竹"},
        {"product_type": "電動工具", "size": "M", "brand": "Bosch", "serial_number": "A003", "destination": "高雄"},
    ]

    for label in generate_shipping_labels(orders):
        print("📦 出貨標籤：\n" + label)
        print("-" * 30)

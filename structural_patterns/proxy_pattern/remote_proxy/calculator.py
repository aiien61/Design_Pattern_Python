from abc import ABC, abstractmethod
import random
import time

# 抽象主題 (Subject)
class Calculator(ABC):
    @abstractmethod
    def add(self, a: int, b: int) -> int:
        raise NotImplementedError

# 真實主題 (RealSubject) - 模擬遠程服務器上的服務
class RemoteCalculator(Calculator):
    def add(self, a: int, b: int) -> int:
        # 模擬網路延遲
        delay: float = random.uniform(0.5, 5.0)
        print(f"模擬遠程服務器處理中，延遲 {delay:.2f} 秒...")
        time.sleep(delay)
        result: int = a + b
        print(f"遠程服務器計算完成: {a} + {b} = {result}")
        return result

# 遠程代理 (Remote Proxy)
class CalculatorProxy(Calculator):
    def __init__(self):
        # 初始化與遠程服務器的連接
        self.remote_calculator = RemoteCalculator()

    def add(self, a: int, b: int) -> int:
        print(f"代理發送請求到遠程服務器: 加法運算 {a} + {b}")
        # 代理負責與遠程服務器通信，直接調用真實對象模擬
        result = self.remote_calculator.add(a, b)
        print("代理收到遠程服務器的結果")
        return result

# 客戶端
if __name__ == "__main__":
    # 客戶端只需要與代理交互，無需關心遠程實現
    calculator = CalculatorProxy()

    # 第一次調用加法
    print("客戶端發起第一次加法請求:")
    result = calculator.add(3, 5)
    print(f"結果: {result}\n")

    # 第二次調用加法
    print("客戶端發起第二次加法請求:")
    result = calculator.add(10, 20)
    print(f"結果: {result}\n")

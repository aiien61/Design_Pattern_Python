from abc import ABC, abstractmethod
import time

# 抽象主題 (Subject)
class FibonacciCalculator(ABC):
    @abstractmethod
    def calculate(self, n: int) -> int:
        raise NotImplementedError

# 真實主題 (RealSubject)
class RealFibonacciCalculator(FibonacciCalculator):
    def calculate(self, n: int) -> int:
        # 模擬耗時計算
        print(f"正在計算斐波那契數列第 {n} 項...")
        time.sleep(1)  # 模擬延遲
        if n <= 1:
            return n
        return self.calculate(n - 1) + self.calculate(n - 2)
    
# 快取代理 (Caching Proxy)
class FibonacciProxy(FibonacciCalculator):
    def __init__(self):
        self.real_calculator = RealFibonacciCalculator()
        self.cache = {}  # 快取字典，儲存計算結果

    def calculate(self, n: int) -> int:
        if n in self.cache:
            print(f"從快取中獲取結果: fibonacci({n}) = {self.cache[n]}")
            return self.cache[n]
        
        # 如果不在快取中，調用真實對象計算並存入快取
        result = self.real_calculator.calculate(n)
        self.cache[n] = result
        print(f"計算完成並快取: fibonacci({n}) = {result}")
        return result
    

# 客戶端
if __name__ == "__main__":
    # 使用代理對象
    calculator = FibonacciProxy()

    # 第一次計算 fibonacci(5)
    print("第一次計算 fibonacci(5):")
    result: int = calculator.calculate(5)
    print(f"結果: {result}\n")

    # 第二次計算 fibonacci(5)，從快取中獲取
    print("第二次計算 fibonacci(5):")
    result: int = calculator.calculate(5)
    print(f"結果: {result}\n")

    # 計算 fibonacci(6)
    print("第一次計算 fibonacci(6):")
    result: int = calculator.calculate(6)
    print(f"結果: {result}\n")

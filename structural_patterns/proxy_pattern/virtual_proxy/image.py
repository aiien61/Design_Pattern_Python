"""以下是一個簡單的虛擬代理範例，模擬圖片加載情境。代理對象在第一次訪問時才加載圖片，後續訪問則直接使用已加載的結果。
"""

from abc import ABC, abstractmethod

# 抽象主題 (Subject)
class Image(ABC):
    @abstractmethod
    def display(self):
        raise NotImplementedError

# 真實主題 (RealSubject)
class RealImage(Image):
    def __init__(self, filename: str):
        self.filename = filename
        self._load_image()

    def _load_image(self):
        print(f"正在從磁盤加載圖片: {self.filename}")

    def display(self):
        print(f"顯示圖片: {self.filename}")

# 代理 (Proxy)
class ImageProxy(Image):
    def __init__(self, filename: str):
        self.filename = filename
        self.real_image = None  # 延遲初始化真實圖片

    def display(self):
        if not self.real_image:  # 第一次訪問時加載
            self.real_image = RealImage(self.filename)
        self.real_image.display()  # 後續直接使用已加載的圖片

if __name__ == "__main__":
    # 使用代理對象
    image = ImageProxy("my_image.jpg")

    # 第一次顯示圖片，會觸發加載
    print("第一次訪問:")
    image.display()

    # 第二次顯示圖片，直接使用已加載的結果
    print("\n第二次訪問:")
    image.display()

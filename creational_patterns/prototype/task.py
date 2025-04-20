"""
適用情境
1. 當物件的建立成本高（如初始化複雜、讀取設定檔、連接外部資源）。
2. 需要產出多個相似的配置實例。

生產排程情境：建立排程任務模板

📝 背景問題：
工廠每天都會排程大量的工作指派，
很多任務其實只有少許差異（如「包裝任務」、「加工任務」、「檢查任務」等）。

如果每次都從頭建立任務，會很浪費資源。
使用 Prototype 模式，可先定義「任務原型」，再根據需求快速複製一份來用 ✅

類別                           | 說明
TaskPrototype                 | 定義任務原型的基礎類別，實作 clone() 方法
PackagingTask, ProcessingTask | 不同任務類型的具體原型
Scheduler                     | 使用者從原型產生任務執行排程
"""
import copy

# 任務原型
class TaskPrototype:
    def __init__(self, name, duration, workstation):
        self.name = name
        self.duration = duration
        self.workstation = workstation
    
    def clone(self):
        return copy.deepcopy(self)
    
    def describe(self):
        print(
            f"📋 任務名稱: {self.name}, 時間: {self.duration} 分鐘, 工作站: {self.workstation}")


# 建立原型任務
packaging_task = TaskPrototype("包裝任務", 30, "包裝站")
processing_task = TaskPrototype("加工任務", 60, "加工站")
inspection_task = TaskPrototype("品質檢查", 20, "品管站")

# 模擬排程器快速產生任務
def main():
    tasks_to_schedule = []

    # 根據生產線需求，複製任務模板並修改部分內容
    for i in range(3):
        t = packaging_task.clone()
        t.name += f" - A{i+1}"
        tasks_to_schedule.append(t)

    for i in range(2):
        t = processing_task.clone()
        t.name += f" - B{i+1}"
        tasks_to_schedule.append(t)
    
    # 顯示所有任務
    print("📆 今日排程任務：")
    for t in tasks_to_schedule:
        t.describe()

if __name__ == "__main__":
    main()

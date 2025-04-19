"""
情境：生產排程系統中的排程版本歷史管理

📝 問題背景：
排程員在調整生產排程時，常常需要回復到前一版排程狀態（例如誤排、突然接到緊急單）。

類別             | 負責角色
Schedule        | 發起人（Originator）👉 排程本體，可儲存或恢復狀態
ScheduleMemento | 備忘錄（Memento）👉 儲存排程狀態
HistoryManager  | 看守者（Caretaker）👉 管理所有備忘紀錄
"""

from copy import deepcopy

# 排程狀態（Memento）
class ScheduleMemento:
    def __init__(self, state):
        self._state = deepcopy(state)
    
    def get_state(self):
        return self._state

# 排程（Originator）
class Schedule:
    def __init__(self):
        self._state = []
    
    def add_job(self, job):
        self._state.append(job)
        print(f"🛠️ 新增工作：{job}")

    def show(self):
        print("📋 當前排程：", self._state)
    
    def save_state(self):
        return ScheduleMemento(self._state)
    
    def restore_state(self, memento):
        self._state = memento.get_state()
        print("🔁 排程狀態已還原")

# 管理歷史（Caretaker）
class HistoryManager:
    def __init__(self):
        self._history = []
    
    def backup(self, memento):
        self._history.append(memento)

    def undo(self):
        if self._history:
            return self._history.pop()
        return None
    
def main():
    schedule = Schedule()
    history = HistoryManager()

    schedule.add_job("JobA")
    history.backup(schedule.save_state())

    schedule.add_job("JobB")
    history.backup(schedule.save_state())

    schedule.add_job("JobC")

    schedule.show()

    print("\n⚠️ 還原到 JobB 前狀態：")
    schedule.restore_state(history.undo())
    schedule.show()

    print("\n⚠️ 再次還原到 JobA 狀態：")
    schedule.restore_state(history.undo())
    schedule.show()

if __name__ == "__main__":
    main()

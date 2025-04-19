"""
情境簡述

當家中的 Alarm 鬧鐘響起 時，它會啟動一系列裝置（如咖啡機、灑水器、行事曆）來準備好你的早晨。
這些裝置不再彼此溝通，而是通知中介者（Mediator）來統一協調各裝置動作。

元件       | 功能說明
Mediator  | 集中處理各家電之間的邏輯與控制流程
Alarm     | 鬧鐘裝置，觸發整個流程的起點
Calendar  | 行事曆系統，判斷是否為週末或垃圾日
Sprinkler | 灑水系統，根據氣象資訊做決策
CoffeePot | 咖啡機，收到通知後啟動
"""
# Mediator 介面與實作
class Mediator:
    def notify(self, sender, event):
        pass

class ConcreteMediator(Mediator):
    def __init__(self):
        self.alarm = None
        self.calendar = None
        self.coffee_pot = None
        self.sprinkler = None
    
    def notify(self, sender, event):
        if event == "alarm_event":
            print("🔔 鬧鐘響了！")
            self.calendar.check_day_of_week()
            self.sprinkler.check_shower()
            self.sprinkler.check_temp()
            self.coffee_pot.brew_coffee()
        elif event == "weekend":
            print("🛌 是週末，不沖咖啡")
        elif event == "rubbish_day":
            print("🚮 今天是倒垃圾日，鬧鐘要提早")
            self.alarm.reset()

# 各家電裝置（Colleagues）
class Alarm:
    def __init__(self, mediator):
        self.mediator = mediator
    
    def on_event(self):
        self.mediator.notify(self, "alarm_event")
    
    def reset(self):
        print("⏰ 鬧鐘重新設定")

class Calendar:
    def __init__(self, mediator):
        self.mediator = mediator

    def check_day_of_week(self):
        print("📅 檢查今天是星期幾")
        self.mediator.notify(self, "weekend")

class CoffeePot:
    def __init__(self, mediator):
        self.mediator = mediator
    
    def brew_coffee(self):
        print("☕️ 開始煮咖啡")

class Sprinkler:
    def __init__(self, mediator):
        self.mediator = mediator
    
    def check_shower(self):
        print("🚿 檢查是否有人洗澡")

    def check_temp(self):
        print("🌡️ 檢查溫度")

    def check_weather(self):
        print("🌧️ 檢查天氣是否適合灑水")

# 啟動整個智慧家庭系統
def main():
    mediator = ConcreteMediator()

    alarm = Alarm(mediator)
    calendar = Calendar(mediator)
    coffee_pot = CoffeePot(mediator)
    sprinkler = Sprinkler(mediator)

    mediator.alarm = alarm
    mediator.calendar = calendar
    mediator.coffee_pot = coffee_pot
    mediator.sprinkler = sprinkler

    # 模擬早上鬧鐘響起
    alarm.on_event()

    # 模擬今天是倒垃圾日
    mediator.notify(calendar, "rubbish_day")

if __name__ == "__main__":
    main()
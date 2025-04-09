from abc import ABC, abstractmethod
from threading import Thread
from typing import List, Optional
from tkinter import ttk
import tkinter as tk
import time
import wave

from rich import print
import pygame

# === Model ===
# observer interfaces
class BeatObserver(ABC):
    @abstractmethod
    def update_beat(self): pass

class BPMObserver(ABC):
    @abstractmethod
    def update_bpm(self, bpm: int): pass

# beat model interface
class BeatModelInterface(ABC):
    @abstractmethod
    def initialize(self): pass

    @abstractmethod
    def on(self): pass

    @abstractmethod
    def off(self): pass

    @abstractmethod
    def set_bpm(self, bpm: int): pass

    @abstractmethod
    def get_bpm(self): pass

    @abstractmethod
    def register_observer(self, observer): pass

    @abstractmethod
    def remove_observer(self, observer): pass

# Beat Model with observer pattern
class BeatModel(BeatModelInterface):
    def __init__(self):
        self.beat_observers: List[BeatObserver] = []
        self.bpm_observers: List[BPMObserver] = []
        self.bpm: int = 90
        self.running: bool = False
        self.thread: Optional[Thread] = None
        self.clip: str = "clap.wav"
        self.audio: Optional[object] = None

    def initialize(self) -> None:
        try:
            pygame.mixer.init()
            self.audio = pygame.mixer.Sound(self.clip)
            print("BeatModel initilised")
        except Exception as e:
            print("Error: can't load clip")
            print(e)
            self.audio = None
    
    def on(self) -> None:
        self.bpm = 90
        self.running = True
        if not self.thread or not self.thread.is_alive():
            self.thread = Thread(target=self.run)
            self.thread.start()

    def off(self) -> None:
        self.running = False

    def run(self) -> None:
        while self.running:
            self.play_beat()
            self.notify_beat_observers()
            time.sleep(60.0 / self.bpm)

    def play_beat(self):
        if self.audio:
            self.audio.play()

    def set_bpm(self, bpm: int):
        self.bpm = bpm
        self.notify_bpm_observers()

    def get_bpm(self) -> int:
        return self.bpm
    
    def register_observer(self, observer: BeatObserver) -> None:
        if isinstance(observer, BeatObserver):
            self.beat_observers.append(observer)

    def remove_observer(self, observer: BeatObserver) -> None:
        if isinstance(observer, BeatObserver):
            self.beat_observers.remove(observer)

    def notify_beat_observers(self):
        for observer in self.beat_observers:
            observer.update_beat()
    
    def register_bpm_observer(self, observer: BPMObserver) -> None:
        if isinstance(observer, BPMObserver):
            self.bpm_observers.append(observer)

    def remove_bpm_observer(self, observer: BPMObserver) -> None:
        if isinstance(observer, BPMObserver):
            self.bpm_observers.remove(observer)

    def notify_bpm_observers(self):
        for observer in self.bpm_observers:
            observer.update_bpm(self.bpm)

# === Controller ===
# controller interface with strategy pattern
class ControllerInterface(ABC):
    @abstractmethod
    def start(self): pass

    @abstractmethod
    def stop(self): pass

    @abstractmethod
    def increase_bpm(self): pass

    @abstractmethod
    def decrease_bpm(self): pass

# a simple controller
class BeatController(ControllerInterface):
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.set_controller(self)
        self.model.initialize()
        self.view.update_controls(start_enabled=True, stop_enabled=False)

    def start(self):
        self.model.on()
        self.view.update_controls(start_enabled=False, stop_enabled=True)

    def stop(self):
        self.model.off()
        self.view.update_controls(start_enabled=True, stop_enabled=False)

    def increase_bpm(self):
        bpm: int = self.model.get_bpm()
        self.model.set_bpm(bpm + 1)
    
    def decrease_bpm(self):
        bpm: int = self.model.get_bpm()
        self.model.set_bpm(bpm - 1)

    def set_bpm(self, bpm: int):
        self.model.set_bpm(bpm)

# === View ===
# view interface
class ViewComponent(ABC):
    @abstractmethod
    def display(self): pass

# composite pattern
class CompositeView(ViewComponent):
    def __init__(self):
        self.children: List[ViewComponent] = []

    def add(self, component: ViewComponent):
        self.children.append(component)

    def remove(self, component: ViewComponent):
        self.children.remove(component)

    def display(self):
        for child in self.children:
            child.display()

# a simple view with observer and strategy pattern
class BeatView(BeatObserver, BPMObserver):
    def __init__(self, model):
        self.model = model
        self.controller = None
        self.root = tk.Tk()
        self.root.title("Beat Player")
        self.root.config(bg="#2e2e2e")
        
        # Progress bar frame (separate for padding)
        progress_frame = tk.Frame(self.root, bg="#2e2e2e")
        progress_frame.pack(pady=(20, 10))
        self.progress = ttk.Progressbar(progress_frame, orient="horizontal", length=250, mode="determinate")
        self.progress.pack()
        
        # Main control panel
        self.main_frame = tk.Frame(self.root, bg="#2e2e2e")
        self.main_frame.pack(padx=30, pady=10)
        
        self.bpm_label = tk.Label(self.main_frame, text="BPM: 90", fg="white", bg="#2e2e2e", font=("Helvetica", 14, "bold"))
        self.bpm_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

    def set_controller(self, controller):
        self.controller = controller
        self.controls()
    
    def controls(self):
        btn_style = {
            "width": 10,
            "height": 2,
            "font": ("Helvetica", 10, "bold"),
            "bg": "#ffffff",
            "fg": "#000000",
            "activebackground": "#dddddd",
            "relief": tk.FLAT
        }

        frame = self.main_frame

        # Start and Stop buttons
        self.start_btn = tk.Button(frame, text="Start", command=self.controller.start, **btn_style)
        self.start_btn.grid(row=1, column=0, padx=15, pady=10)

        self.stop_btn = tk.Button(frame, text="Stop", command=self.controller.stop, **btn_style)
        self.stop_btn.grid(row=1, column=1, padx=15, pady=10)

        # + and - buttons
        self.plus_btn = tk.Button(frame, text="+", command=self.controller.increase_bpm, **btn_style)
        self.plus_btn.grid(row=2, column=0, padx=15, pady=10)
        
        self.minus_btn = tk.Button(frame, text="-", command=self.controller.decrease_bpm, **btn_style)
        self.minus_btn.grid(row=2, column=1, padx=15, pady=10)

    def update_controls(self, start_enabled: bool, stop_enabled: bool):
        self.start_btn.config(state=tk.NORMAL if start_enabled else tk.DISABLED)
        self.stop_btn.config(state=tk.NORMAL if stop_enabled else tk.DISABLED)

    def update_beat(self):
        self.update_progress()

    def update_bpm(self, bpm: int):
        self.bpm_label.config(text=f"BPM: {bpm}")

    def start(self):
        self.root.mainloop()

    def update_progress(self):
        self.progress['value'] = 100
        self.root.after(100, lambda: self.progress.config(value=75))
        self.root.after(200, lambda: self.progress.config(value=50))
        self.root.after(300, lambda: self.progress.config(value=25))
        self.root.after(400, lambda: self.progress.config(value=0))

if __name__ == "__main__":
    model = BeatModel()
    view = BeatView(model)
    controller = BeatController(model, view)

    view.set_controller(controller)
    
    model.register_observer(view)
    model.register_bpm_observer(view)

    # setattr(view, "update_beat", lambda: view.update_progress())
    # setattr(view, "update_bpm", lambda: view.update_bpm(model.get_bpm()))

    view.start()

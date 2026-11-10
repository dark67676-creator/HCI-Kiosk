import pygame
import numpy as np
import tkinter as tk

from home_page import homepage
from map import mapscreen
from keyboard import keyboard, popupkeyboard
from parking import parkingscreen
from exits import exitscreen

class KioskApp:
    def __init__(self, root):
        self.root = root
        self.root.title("trafford centre kiosk")
        self.root.geometry('1368x900')
        self.current_screen = None
        self.font_size = 12

        self.volume= 0.5

        #sound logic
        pygame.mixer.init( frequency=44100)
        sample_rate= 44100
        duration = 0.1
        freq = 1000
        t = np.linspace(0,duration, int(sample_rate* duration),False)
        wave = (np.sin(2*np.pi*freq*t)*32767).astype(np.int16)
        wave = np.column_stack([wave,wave])
        self.beep_sound = pygame.sndarray.make_sound(wave)
        self.show_home()

    def show_home (self):
        self.switch_to(homepage)
    def show_keyboard (self):
        self.switch_to(keyboard)
    def show_pop_up_keyboard(self):
        self.switch_to(popupkeyboard)
    def show_map (self):
        self.switch_to(mapscreen)
    def show_parking (self):
        self.switch_to(parkingscreen)
    def show_exits (self):
        self.switch_to(exitscreen)
    def switch_to(self, ScreenClass):
        if self.current_screen is not None:
            self.current_screen.frame.destroy()
        self.current_screen = ScreenClass(self.root, self)
        self.apply_font()

    def update_font(self):
        self.update_size(10 if self.font_size == 12 else -10)

    def update_size(self,delta):
        self.font_size = max(12,min(60,self.font_size + delta))
        self.apply_font()
    def apply_font(self):

        def update_widgets(parent):
            for widget in parent.winfo_children():
                if isinstance(widget,tk.Button):
                    widget.config(font=("Arial",self.font_size))
                update_widgets(widget)
        update_widgets(self.root)
    
    def on_click(self):
        if self.volume > 0:
           self.beep_sound.set_volume(self.volume)
           self.beep_sound.play()
    def with_sound(self, command):
        def wrapper():
            self.on_click()
            command()
        return wrapper

    def set_volume(self, volume):
        self.volume = volume
if __name__ == "__main__":
    root = tk.Tk()
    app = KioskApp(root)
    root.mainloop()


import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import base64
from io import BytesIO


class homepage:
    def __init__(self, root, app):
        self.root = root
        self.app = app
        self.root.title("Untitled Project")
        self.root.geometry("1368x900")
        self.root.resizable(True, True)
        self.font_size =35
        
        # Initialize variables
        
        # Create widgets
        self._create_widgets()
    
    def _create_widgets(self):
        """Create and place all widgets"""
        
        self.frame = tk.Frame(self.root, width=1368, height=900)
        self.frame.place(x=0, y=0)
        self.volume_label = tk.Label(
            self.root,
            text="volume",
            font=("Arial",10),
        )
        self.volume_label.place(x=140, y=230, width=140 ,height=20)
        
        self.volume_slider = tk.Scale(        
        self.root,
        from_=0,
        to=100,
        orient=tk.HORIZONTAL,
        command=self.on_volume_change,
        font=("Arial", 9),
        )
        self.volume_slider.place(x=140,y=250,width=140,height=40)
        # button_111
        self.button_111 = tk.Button(
            self.root,
            text="french",
            font=("Arial", 12),
            command=self.on_button_111_click
        )
        self.button_1.place(x=500, y=270, width=140, height=46)
        # button_1
        self.button_1 = tk.Button(
            self.root,
            text="Food",
            font=("Arial", 12),
            command=self.on_button_1_click
        )
        self.button_1.place(x=500, y=270, width=140, height=46)                                                                                                                                                                                                                                                                                                                              
        # button_2
        self.button_2 = tk.Button(
            self.root,
            text="Shopping",
            font=("Arial", 12),
            command=self.app.with_sound(self.on_button_2_click)
        )
        self.button_2.place(x=730, y=220, width=140, height=46)
        
        # button_3
        self.button_3 = tk.Button(
            self.root,
            text="Cashpoints",
            font=("Arial", 12),
            command=self.app.with_sound(self.on_button_3_click)
        )
        self.button_3.place(x=730, y=270, width=140, height=46)
        
        # button_4
        self.button_4 = tk.Button(
            self.root,
            text="Parking",
            font=("Arial", 12),
            command=self.app.with_sound(self.on_button_4_click)
        )
        self.button_4.place(x=500, y=220, width=140, height=46)
        
        # button_5
        self.button_5 = tk.Button(
            self.root,
            text="Map",
            font=("Arial", 12),
            command=self.app.with_sound(self.on_button_5_click)
        )
        self.button_5.place(x=500, y=320, width=140, height=46)
        
        # button_6
        self.button_6 = tk.Button(
            self.root,
            text="emergency exits",
            bg="#f73b3b",
            font=("Arial", 12),
            command=self.app.with_sound(self.on_button_6_click)
        )
        self.button_6.place(x=730, y=320, width=140, height=46)
        
        # button_7
        self.button_7 = tk.Button(
            self.root,
            text="Help",
            font=("Arial", 12),
            command=self.app.with_sound(self.on_button_7_click)
        )
        self.button_7.place(x=610, y=370, width=140, height=46)
        
        self.button_8 = tk.Button(
            self.root,
            text="search🔎",
            font=("Arial", 12),
            command=self.app.with_sound(self.on_button_8_click)
        )
        self.button_8.place(x=300, y=160, width=120, height=60)
        
        self.zoom = tk.Button(
            self.root,
            text="zoom in",
            bg="#3b57f7",
            font=("Arial", 12),
            command=self.app.with_sound(self.on_button_zoom_click)
        )
        self.zoom.place(x=140, y=160, width=140, height=60)
        # image_1
        # Load image for image_1
        self.image_1_photo = tk.PhotoImage(file="assets/logo.png")
        self.image_1 = tk.Label(
            self.root,
            image=self.image_1_photo,
        )
        self.image_1.image = self.image_1_photo  # Keep reference
        self.image_1.place(x=510, y=20, width=320, height=150)
        
        # image_2
        # Load image for image_2
        self.image_2_photo = tk.PhotoImage(file="assets/map.png")
        self.image_2 = tk.Label(
            self.root,
            image=self.image_2_photo,
        )
        self.image_2.image = self.image_2_photo  # Keep reference
        self.image_2.place(x=460, y=450, width=450, height=150)
        
        """ self.image_3_photo = tk.PhotoImage(file="assets/search.png")
        self.image_3 = tk.Label(
            self.root,
            image=self.image_3_photo,
        )
        self.image_3.image = self.image_3_photo  # Keep reference
        self.image_3.place(x=320, y=140, width=80, height=60)"""
    
    
    # ==========================================
    # Event Handlers - Implement your logic here
    # ==========================================
    

        
    def on_button_1_click(self):
        print("Button 2 clicked")
        messagebox.showinfo("Food", "Food options include: McDonald's, KFC, Subway, and more!")
        
        pass
    
    def on_button_2_click(self):
        print("Button 2 clicked")
        messagebox.showinfo("Shopping", "Shopping options include: Zara, H&M, Apple Store, and more!")
        
        pass
    
    def on_button_3_click(self):
        print("Button 2 clicked")
        messagebox.showinfo("Cashpoints", "HSBC Halifax")
        
        pass
    
    def on_button_4_click(self):
        
        self.app.show_parking()
        
        pass
    
    def on_button_5_click(self):
     
        self.app.show_map()
        pass
    
    def on_button_6_click(self):
        
        self.app.show_exits()
        pass
    
    def on_button_7_click(self):
    
        messagebox.showinfo("Help", "For assistance, please contact our customer service at 0737661478 or visit the information desk located in the food court.")
    
        pass
    def on_button_8_click(self):
        self.app.show_keyboard() 
        pass
    def on_button_zoom_click(self):
        self.app.update_font() 
        pass
    def on_volume_change(self, value):
        volume = int(value) / 100  # Convert 0–100 to 0.0–1.0
        self.app.set_volume(volume)
        pass


import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import base64
from io import BytesIO
from PIL import Image, ImageTk


class mapscreen:
    def __init__(self, root, app):
        self.root = root
        self.app = app
        self.root.title("Untitled Project")
        self.root.geometry("1138x828")
        self.root.resizable(True, True)
        
        # Initialize variables
        
        
        # Create widgets
        self._create_widgets()
    
    def _create_widgets(self):
        """Create and place all widgets"""
        self.frame = tk.Frame(self.root, width=1138, height=828)
        self.frame.place(x=0,y=0)
        
        # button_1
        self.button_1 = tk.Button(
            self.root,
            text="Return to main menu",
            bg="#3b57f7",
            font=("Arial", 12),
            command=self.app.with_sound(self.on_button_1_click)
        )
        self.button_1.place(x=200, y=220, width=140, height=36)
        
        # progressbar_1
        # TODO: Implement progressbar widget
        
        # label_1
        self.label_1 = tk.Label(
            self.root,
            text="Zoom ",
            fg="#000000",
            font=("Arial", 12),
            anchor="center"
        )
        self.label_1.place(x=540, y=580, width=80, height=20)
        
        # label_2
        self.label_2 = tk.Label(
            self.root,
            text="+",
            fg="#000000",
            font=("Arial", 12),
            anchor="center"
        )
        self.label_2.place(x=690, y=580, width=40, height=20)
        
        # label_3
        self.label_3 = tk.Label(
            self.root,
            text="-",
            fg="#000000",
            font=("Arial", 12),
            anchor="center"
        )
        self.label_3.place(x=450, y=580, width=20, height=20)
        
        # logo
        # Load image for logo
        self.logo_photo = tk.PhotoImage(file="assets/logo.png")
        self.logo = tk.Label(
            self.root,
            image=self.logo_photo,
        )
        self.logo.image = self.logo_photo  # Keep reference
        self.logo.place(x=390, y=40, width=370, height=130)
        
        # search
        # Load image for search
        self.search_photo = tk.PhotoImage(file="assets/search.png")
        self.search = tk.Label(
            self.root,
            image=self.search_photo,
        )
        self.search.image = self.search_photo  # Keep reference
        self.search.place(x=350, y=230, width=0, height=0)
        
        # Map
        # Load image for Map
        self.Map_photo = tk.PhotoImage(file="assets/map.png")
        self.Map = tk.Label(
            self.root,
            image=self.Map_photo,
        )
        self.Map.image = self.Map_photo  # Keep reference
        self.Map.place(x=300, y=270, width=510, height=270)
    
    # ==========================================
    # Event Handlers - Implement your logic here
    # ==========================================
    
    def on_button_1_click(self):
        
        self.app.show_home()
        
        
        pass
    

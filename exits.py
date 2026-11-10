

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import base64
from io import BytesIO
from PIL import Image, ImageTk


class exitscreen:
    def __init__(self, root, app):
        self.root = root
        self.app = app
        self.root.title("Untitled Project")
        self.root.geometry("1368x900")
        self.root.resizable(True, True)
        
        # Initialize variables
        
        # Create widgets
        self._create_widgets()
    
    def _create_widgets(self):
        """Create and place all widgets"""



        self.frame = tk.Frame(self.root, width=1368, height=900)
        self.frame.place(x=0,y=0)
        # logo
        # Load image for logo
        self.logo_photo = tk.PhotoImage(file="assets/logo.png")
        self.logo = tk.Label(
            self.root,
            image=self.logo_photo,
        )
        self.logo.image = self.logo_photo  # Keep reference
        self.logo.place(x=513, y=20, width=300, height=150)
        
        # map
        # Load image for map
        self.map_photo = tk.PhotoImage(file="assets/emergency.png")
        self.map = tk.Label(
            self.root,
            image=self.map_photo,
        )
        self.map.image = self.map_photo  # Keep reference
        self.map.place(x=234, y=200, width=900, height=580)
        
        # exit
        self.exit = tk.Label(
            self.root,
            text="EMERGENCY EXITS",
            fg="#000000",
            font=("Arial", 12),
            anchor="center"
        )
        self.exit.place(x=515, y=175, width=240, height=30)
         # return
        self.returnc = tk.Button(
            self.root,
            text="Return to main menu",
            bg="#3b57f7",
            font=("Arial", 12),
            command=self.on_button_returnc_click
        )
        self.returnc.place(x=340, y=175, width=140, height=60)
    
    # ==========================================
    # Event Handlers - Implement your logic here
    # ==========================================
    def on_button_returnc_click(self):
        self.app.show_home()


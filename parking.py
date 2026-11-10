import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import base64
from io import BytesIO
from PIL import Image, ImageTk
from keyboard import popupkeyboard
import keyboard as kb

class parkingscreen:
    def __init__(self, root, app):
        
        self.root = root
        self.app = app
        self.root.title("Untitled Project")
        self.root.geometry("1368x900")
        self.root.resizable(True, True)
        
        # Initialize variables
        self.bay_status = {
            1:'available',
            2:'available',
            3:'available',
            4:'unavailable',
            5:'available',
            6:'available',
            7:'unavailable',
            8:'available',
            9:'available',
            10:'available',
            11:'available',
            12:'available',
            13:'available',
            14:'unavailable',
            15:'available',
            16:'available',
            }
        self.selected_bay = None
        # Create widgets
        self._create_widgets()
    
    def _create_widgets(self):
        """Create and place all widgets"""

    
        self.frame = tk.Frame(self.root, width=1368, height=900)
        self.frame.place(x=0, y=0)
        self.confirm = tk.Button(
            self.root,
            text="confrim",
            bg="#1ec821",
            font=("Arial", 12),
            command=self.app.with_sound(self.on_confirm_click)
        )
        self.confirm.place(x=120, y=120, width=165, height=45)
        # bay_1
        self.bay_1 = tk.Button(
            self.root,
            text="bay 1",
            font=("Arial", 12),
            command=self.app.with_sound(self.on_bay_1_click)
        )
        self.bay_1.place(x=430, y=610, width=120, height=190)
        
        # bay_2
        self.bay_2 = tk.Button(
            self.root,
            text="bay 2",
            font=("Arial", 12),
            command=self.app.with_sound(self.on_bay_2_click)
        )
        self.bay_2.place(x=270, y=610, width=120, height=190)
        
        # bay_3
        self.bay_3 = tk.Button(
            self.root,
            text="bay 3",
            font=("Arial", 12),
            command=self.app.with_sound(self.on_bay_3_click)
        )
        self.bay_3.place(x=120, y=610, width=120, height=190)
        
        # bay_4
        self.bay_4 = tk.Button(
            self.root,
            text="bay 4",
            font=("Arial", 12),
            command=self.app.with_sound(self.on_bay_4_click)
        )
        self.bay_4.place(x=1140, y=340, width=120, height=190)
        
        # bay_5
        self.bay_5 = tk.Button(
            self.root,
            text="bay 5",
            font=("Arial", 12),
            command=self.app.with_sound(self.on_bay_5_click)
        )
        self.bay_5.place(x=990, y=340, width=120, height=190)
        
        # bay_6
        self.bay_6 = tk.Button(
            self.root,
            text="bay 6",
            font=("Arial", 12),
            command=self.app.with_sound(self.on_bay_6_click)
        )
        self.bay_6.place(x=840, y=340, width=120, height=190)
        
        # bay_7
        self.bay_7 = tk.Button(
            self.root,
            text="bay 7",
            font=("Arial", 12),
            command=self.app.with_sound(self.on_bay_7_click)
        )
        self.bay_7.place(x=700, y=340, width=120, height=190)
        
        # bay_8
        self.bay_8 = tk.Button(
            self.root,
            text="bay 8",
            font=("Arial", 12),
            command=self.app.with_sound(self.on_bay_8_click)
        )
        self.bay_8.place(x=560, y=340, width=120, height=190)
        
        # bay_9
        self.bay_9 = tk.Button(
            self.root,
            text="bay 9",
            font=("Arial", 12),
            command=self.app.with_sound(self.on_bay_9_click)
        )
        self.bay_9.place(x=420, y=340, width=120, height=190)
        
        # bay_10
        self.bay_10 = tk.Button(
            self.root,
            text="bay 10",
            font=("Arial", 12),
            command=self.app.with_sound(self.on_bay_10_click)
        )
        self.bay_10.place(x=270, y=340, width=120, height=190)
        
        # bay_11
        self.bay_11 = tk.Button(
            self.root,
            text="bay 11",
            font=("Arial", 12),
            command=self.app.with_sound(self.on_bay_11_click)
        )
        self.bay_11.place(x=120, y=340, width=120, height=190)
        
        # bay_12
        self.bay_12 = tk.Button(
            self.root,
            text="bay 12",
            font=("Arial", 12),
            command=self.app.with_sound(self.on_bay_12_click)
        )
        self.bay_12.place(x=570, y=610, width=120, height=190)
        
        # bay_13
        self.bay_13 = tk.Button(
            self.root,
            text="bay 13",
            font=("Arial", 12),
            command=self.app.with_sound(self.on_bay_13_click)
        )
        self.bay_13.place(x=710, y=610, width=120, height=190)
        
        # bay _14
        self.bay_14 = tk.Button(
            self.root,
            text="bay 14",
            font=("Arial", 12),
            command=self.app.with_sound(self.on_bay_14_click)
        )
        self.bay_14.place(x=1150, y=610, width=120, height=190)
        
        # bay_15
        self.bay_15 = tk.Button(
            self.root,
            text="bay 15",
            font=("Arial", 12),
            command=self.app.with_sound(self.on_bay_15_click)
        )
        self.bay_15.place(x=1000, y=610, width=120, height=190)
        
        # bay_16
        self.bay_16 = tk.Button(
            self.root,
            text="bay 16",
            font=("Arial", 12),
            command=self.app.with_sound(self.on_bay_16_click)
        )
        self.bay_16.place(x=850, y=610, width=120, height=190)
          # button_32
        self.returna = tk.Button(
            self.root,
            text="Return to main menu",
            bg="#3b57f7",
            font=("Arial", 12),
            command=self.app.with_sound(self.on_button_returna_click)
        )
        self.returna.place(x=120, y=180, width=165, height=45)

        
        # parking
        self.parking = tk.Label(
            self.root,
            text="PARKING",
            fg="#000000",
            font=("Arial", 20),
            anchor="center"
        )
        self.parking.place(x=520, y=260, width=320, height=20)
        
        # logo
        # Load image for logo
        self.logo_photo = tk.PhotoImage(file="assets/logo.png")
        self.logo = tk.Label(
            self.root,
            image=self.logo_photo,
        )
        self.logo.image = self.logo_photo  # Keep reference
        self.logo.place(x=410, y=10, width=540, height=150)
        
        # keyboard
        self.keyboard = tk.Button(
            self.root,
            text="enter reg",
            font=("Arial", 12),
            command=self.app.with_sound(self.on_keyboard_click)
        )
        self.keyboard.place(x=120, y=260, width=165, height=45)
        
        # entry_1
        self.entry_1 = tk.Entry(
            self.root,
            font=("Arial", 12),
            bg="#ffffff",
            fg="#000000"
        )
        self.entry_1.place(x=580, y=170, width=200, height=32)#this decides the appriopoate color for the pay depending on it its taken or not
        self.entry_1.insert(0, "Enter reg")  # Placeholder text

        
        bay_colours = {'available': '#1ec821', 'taken': '#f73b3b', 'unavailable': '#aaaaaa'}
        for bay_num, status in self.bay_status.items():
            frame_name = f'bay_{bay_num}'

            bay_frame = getattr(self, frame_name)
            bay_frame.config(bg=bay_colours[status])
            
        #this allows the click to actually make something occur
        for bay_num in self.bay_status:
             frame_name = f'bay_{bay_num}'
             bay_frame = getattr(self, frame_name)
             bay_frame.bind('<Button-1>', lambda event, n=bay_num: self.on_bay_click(n))
    # ==========================================
    # Event Handlers - Implement your logic here
    # ==========================================
    def on_bay_click(self,bay_number):#sees if the bay is empty
        if self.bay_status[bay_number] in ("taken", "unavailable"):
            messagebox.showwarning("bay is taken choose another!",
                                    f'Sorry,Bay{bay_number}is already resereved')
            
            return
        if self.selected_bay is not None:#puts bays back to green
            prev_frame = getattr(self,f'bay_{self.selected_bay}')
            prev_frame.config(bg ='#1ec821')
            
        self.selected_bay = bay_number
        getattr(self,f'bay_{bay_number}').config(bg= '#f5a623')

    def on_confirm_click(self):
        plate = kb.typed_reg.strip()
        if self.selected_bay is None:
            messagebox.showerror("No bay selected!",
                                    f'Please select an avabilable bay')
            return
        if plate == "" :
            messagebox.showerror('no plate entered',
                                 'Please enter your reg')
            return
        self.bay_status[self.selected_bay] = 'taken'
        getattr(self, f'bay_{self.selected_bay}').config(bg= '#f73b3b')
        messagebox.showinfo('reserved',
                            f'Bay {self.selected_bay}is reserved for {plate}')
        self.selected_bay = None
        self.entry_1.delete(0,tk.END)

    def on_bay_1_click(self,):
        """
        Handle on_bay_1_click event
        TODO: Implement your logic here
        """
        pass
    
    def on_bay_2_click(self):
        """
        Handle on_bay_2_click event
        TODO: Implement your logic here
        """
        pass
    
    def on_bay_3_click(self):
        """
        Handle on_bay_3_click event
        TODO: Implement your logic here
        """
        pass
    
    def on_bay_4_click(self):
        """
        Handle on_bay_4_click event
        TODO: Implement your logic here
        """
        pass
    
    def on_bay_5_click(self):
        """
        Handle on_bay_5_click event
        TODO: Implement your logic here
        """
        pass
    
    def on_bay_6_click(self):
        """
        Handle on_bay_6_click event
        TODO: Implement your logic here
        """
        pass
    
    def on_bay_7_click(self):
        """
        Handle on_bay_7_click event
        TODO: Implement your logic here
        """
        pass
    
    def on_bay_8_click(self):
        """
        Handle on_bay_8_click event
        TODO: Implement your logic here
        """
        pass
    
    def on_bay_9_click(self):
        """
        Handle on_bay_9_click event
        TODO: Implement your logic here
        """
        pass
    
    def on_bay_10_click(self):
        """
        Handle on_bay_10_click event
        TODO: Implement your logic here
        """
        pass
    
    def on_bay_11_click(self):
        """
        Handle on_bay _11_click event
        TODO: Implement your logic here
        """
        pass
    
    def on_bay_12_click(self):
        """
        Handle on_bay_12_click event
        TODO: Implement your logic here
        """
        pass
    
    def on_bay_13_click(self):
        """
        Handle on_bay_13_click event
        TODO: Implement your logic here
        """
        pass
    
    def on_bay_14_click(self):
        """
        Handle on_bay _14_click event
        TODO: Implement your logic here
        """
        pass
    
    def on_bay_15_click(self):
        """
        Handle on_bay_15_click event
        TODO: Implement your logic here
        """
        pass
    
    def on_bay_16_click(self):
        """
        Handle on_bay_16_click event
        TODO: Implement your logic here
        """
        pass
    
    def on_keyboard_click(self):
        """
        Handle on_keyboard_click event
        TODO: Implement your logic here
        """
        self.app.show_pop_up_keyboard() 

    def on_button_returna_click(self):
        self.app.show_home()

        
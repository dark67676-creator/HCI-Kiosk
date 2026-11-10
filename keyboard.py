
typed_reg = ""


import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import base64
from io import BytesIO
from PIL import Image, ImageTk


class keyboard:


    def __init__(self, root, app, _entry=None):

        self.root = root
        self.app = app
        self.root.title("Untitled Project")
        self.root.geometry("1368x900")
        self.root.resizable(True, True)
        self.caps_on= False
        self._create_widgets()
       
        # Initialize variables
        
    def _create_widgets(self):
        """Create and place all widgets"""
        self.frame = tk.Frame(self.root, width=1368, height=900)
        self.frame.place(x=0, y=0)
        self.frame.lift()
    
    
        
        # entry_1
        self.entry_1 = tk.Entry(
            self.root,
            font=("Arial", 12),
            bg="#ffffff",
            fg="#000000"
        )
        self.entry_1.place(x=334, y=110, width=700, height=50)
        self.entry_1.insert(0, "")  # Placeholder text
        
        # frame_1
        self.frame_1 = tk.Frame(
            self.root,
            bg="#f3f4f6",
            relief="groove",
            bd=1
        )
        self.frame_1.place(x=390, y=200, width=470, height=160)
#nums
        self.button_1 = tk.Button(
            self.root,
            text="1",
            font=("Arial", 12),
            command=lambda: self.keys("1")
        )
        self.button_1.place(x=400, y=230, width=30, height=20)
        self.button_2 = tk.Button(
            self.root,
            text="2",
            font=("Arial", 12),
            command=lambda: self.keys("2")
        )
        self.button_2.place(x=440, y=230, width=30, height=20)
        self.button_3 = tk.Button(
            self.root,
            text="3",
            font=("Arial", 12),
            command=lambda: self.keys("3")
        )
        self.button_3.place(x=480, y=230, width=30, height=20)
        
        self.button_4 = tk.Button(
            self.root,
            text="4",
            font=("Arial", 12),
            command=lambda: self.keys("4")
        )
        self.button_4.place(x=520, y=230, width=30, height=20)
        self.button_5 = tk.Button(
            self.root,
            text="5",
            font=("Arial", 12),
            command=lambda: self.keys("5")
        )
        self.button_5.place(x=560, y=230, width=30, height=20)
        self.button_6 = tk.Button(
            self.root,
            text="6",
            font=("Arial", 12),
            command=lambda: self.keys("6")
        )
        self.button_6.place(x=600, y=230, width=30, height=20)
        
        self.button_7 = tk.Button(
            self.root,
            text="7",
            font=("Arial", 12),
            command=lambda: self.keys("7")
        )
        self.button_7.place(x=640, y=230, width=30, height=20)
        self.button_8 = tk.Button(
            self.root,
            text="8",
            font=("Arial", 12),
            command=lambda: self.keys("8")
        )
        self.button_8.place(x=680, y=230, width=30, height=20)
        
        self.button_9 = tk.Button(
            self.root,
            text="9",
            font=("Arial", 12),
            command=lambda: self.keys("9")
        )
        self.button_9.place(x=720, y=230, width=30, height=20)
       
        self.button_0 = tk.Button(
            self.root,
            text="0",
            font=("Arial", 12),
            command=lambda: self.keys("0")
        )
        self.button_0.place(x=760, y=230, width=30, height=20)

        # button_1
        self.button_Q = tk.Button(
            self.root,
            text="Q",
            font=("Arial", 12),
            command=self.on_button_Q_click
        )
        self.button_Q.place(x=400, y=260, width=30, height=20)
        
        # button_2
        self.button_W = tk.Button(
            self.root,
            text="W",
            font=("Arial", 12),
            command=self.on_button_W_click
        )
        self.button_W.place(x=440, y=260, width=30, height=20)
        
        # button_3
        self.button_E = tk.Button(
            self.root,
            text="E",
            font=("Arial", 12),
            command=self.on_button_E_click
        )
        self.button_E.place(x=480, y=260, width=30, height=20)
        
        # button_4
        self.button_R = tk.Button(
            self.root,
            text="R",
            font=("Arial", 12),
            command=self.on_button_R_click
        )
        self.button_R.place(x=520, y=260, width=30, height=20)
        
        # button_5
        self.button_T = tk.Button(
            self.root,
            text="T",
            font=("Arial", 12),
            command=self.on_button_T_click
        )
        self.button_T.place(x=560, y=260, width=30, height=20)
        
        # button_6
        self.button_Y = tk.Button(
            self.root,
            text="Y",
            font=("Arial", 12),
            command=self.on_button_Y_click
        )
        self.button_Y.place(x=600, y=260, width=30, height=20)
        
        # button_7
        self.button_U = tk.Button(
            self.root,
            text="U",
            font=("Arial", 12),
            command=self.on_button_U_click
        )
        self.button_U.place(x=640, y=260, width=30, height=20)
        
        # button_8
        self.button_I = tk.Button(
            self.root,
            text="I",
            font=("Arial", 12),
            command=self.on_button_I_click
        )
        self.button_I.place(x=680, y=260, width=30, height=20)
        
        # button_9
        self.button_O = tk.Button(
            self.root,
            text="O",
            font=("Arial", 12),
            command=self.on_button_O_click
        )
        self.button_O.place(x=720, y=260, width=30, height=20)
        
        # button_10
        #self.button_del = tk.Button(
        #   self.root,
        #    text="Delete",
         #   font=("Arial", 12),
         #   command=self.on_button_del_click #ter
        #)
        #self.button_P.place(x=60, y=260, width=46, height=20)
        
        # button_11
        self.button_P = tk.Button(
            self.root,
            text="P",
            font=("Arial", 12),
            command=self.on_button_P_click
        )
        self.button_P.place(x=760, y=260, width=30, height=20)
        
        # button_18
        #self.button_Q = tk.Button(
            #self.root,
            #text="Q",
            #font=("Arial", 12),
            #command=self.on_button_Q_click
        #)
        #self.button_Q.place(x=100, y=290, width=30, height=20)
        
        # button_19
        #self.button_Q = tk.Button(
        #    self.root,
        #    text="Q",
        #    font=("Arial", 12),
        #    command=self.on_button_Q_click
        #)
        #self.button_Q.place(x=100, y=290, width=30, height=20)
        
        # button_14
        self.button_S = tk.Button(
            self.root,
            text="S",
            font=("Arial", 12),
            command=self.on_button_S_click
        )
        self.button_S.place(x=440, y=290, width=30, height=20)
        
        # button_15
        self.button_A = tk.Button(
            self.root,
            text="A",
            font=("Arial", 12),
            command=self.on_button_A_click
        )
        self.button_A.place(x=400, y=290, width=30, height=20)
        
        # button_16
        self.button_L = tk.Button(
            self.root,
            text="L",
            font=("Arial", 12),
            command=self.on_button_L_click
        )
        self.button_L.place(x=480, y=290, width=30, height=20)
        
        # button_17
        self.button_G = tk.Button(
            self.root,
            text="G",
            font=("Arial", 12),
            command=self.on_button_G_click
        )
        self.button_G.place(x=560, y=290, width=30, height=20)
        
        # button_18
        self.button_F = tk.Button(
            self.root,
            text="F",
            font=("Arial", 12),
            command=self.on_button_F_click
        )
        self.button_F.place(x=520, y=290, width=30, height=20)
        
        # button_19
        self.button_D = tk.Button(
            self.root,
            text="D",
            font=("Arial", 12),
            command=self.on_button_D_click
        )
        self.button_D.place(x=680, y=290, width=30, height=20)
        
        # button_20
        self.button_K = tk.Button(
            self.root,
            text="K",
            font=("Arial", 12),
            command=self.on_button_K_click
        )
        self.button_K.place(x=720, y=290, width=30, height=20)
        
        # button_21
        self.button_J = tk.Button(
            self.root,
            text="J",
            font=("Arial", 12),
            command=self.on_button_J_click
        )
        self.button_J.place(x=640, y=290, width=30, height=20)
        
        # button_22
        self.button_H = tk.Button(
            self.root,
            text="H",
            font=("Arial", 12),
            command=self.on_button_H_click
        )
        self.button_H.place(x=600, y=290, width=30, height=20)
        
        # button_23
        self.button_L = tk.Button(
            self.root,
            text="DELETE",
            font=("Arial", 12),
            command=self.on_button_DELETE_click
        )
        self.button_L.place(x=760, y=290, width=70, height=20)
        
        # button_24
        self.button_M = tk.Button(
            self.root,
            text="M",
            font=("Arial", 12),
            command=self.on_button_M_click
        )
        self.button_M.place(x=640, y=320, width=30, height=20)
        
        # button_25
        self.button_N = tk.Button(
            self.root,
            text="N",
            font=("Arial", 12),
            command=self.on_button_N_click
        )
        self.button_N.place(x=600, y=320, width=30, height=20)
        
        # button_26
        self.button_B = tk.Button(
            self.root,
            text="B",
            font=("Arial", 12),
            command=self.on_button_B_click
        )
        self.button_B.place(x=560, y=320, width=30, height=20)
        
        # button_27
        self.button_V = tk.Button(
            self.root,
            text="V",
            font=("Arial", 12),
            command=self.on_button_V_click
        )
        self.button_V.place(x=520, y=320, width=30, height=20)
        
        # button_28
        self.button_C = tk.Button(
            self.root,
            text="C",
            font=("Arial", 12),
            command=self.on_button_C_click
        )
        self.button_C.place(x=480, y=320, width=30, height=20)
        
        # button_29
        self.X = tk.Button(
            self.root,
            text="X",
            font=("Arial", 12),
            command=self.on_button_X_click
        )
        self.X.place(x=440, y=320, width=30, height=20)
        
        # button_30
        self.Z = tk.Button(
            self.root,
            text="Z",
            font=("Arial", 12),
            command=self.on_button_Z_click
        )
        self.Z.place(x=400, y=320, width=30, height=20)
        
        # button_31
        self.Enter = tk.Button(
            self.root,
            text="Enter",
            font=("Arial", 12),
            command=self.on_button_enter_click
        )
        self.Enter.place(x=800, y=310, width=50, height=20)
        self.enter = tk.Button(
            self.root,
            text="Enter",
            font=("Arial", 12),
            command=self.on_button_enter_click
        )
   
          # button_32
        self.returnb = tk.Button(
            self.root,
            text="Return to main menu",
            bg="#3b57f7",
            font=("Arial", 12),
            command=self.on_button_returnb_click
        )
        self.returnb.place(x=540, y=440, width=140, height=60)
        # image_2
        # Load image for image_2
        import base64
        from io import BytesIO
        from PIL import Image, ImageTk
        self.image_2_data = base64.b64decode("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")
        self.image_2_img = Image.open(BytesIO(self.image_2_data))
        self.image_2_img = self.image_2_img.resize((50, 20), Image.Resampling.LANCZOS)
        self.image_2_photo = ImageTk.PhotoImage(file ="path/to/image_2.png")
        self.image_2 = tk.Label(
            self.root,
            image=self.image_2_photo,
        )
        self.image_2.image = self.image_2_photo  # Keep reference
        self.image_2.place(x=170, y=170, width=50, height=20)
        
        # frame_2
        self.frame_2 = tk.Frame(
            self.root,
            bg="#f3f4f6",
            relief="groove",
            bd=1
        )
        self.frame_2.place(x=40, y=370, width=180, height=100)
        
        # label_4
        self.label_4 = tk.Label(
            self.root,
            text="Results",
            fg="#000000",
            font=("Arial", 12),
            anchor="center"
        )
        self.label_4.place(x=50, y=370, width=100, height=24)
        
        # label_5
        self.label_5 = tk.Label(
            self.root,
            text="Car park",
            fg="#000000",
            font=("Arial", 12),
            anchor="center"
        )
        self.label_5.place(x=50, y=400, width=120, height=20)
        
        # label_10
        self.label_10 = tk.Label(
            self.root,
            text="Cinema",
            fg="#000000",
            font=("Arial", 12),
            anchor="center"
        )
        self.label_10.place(x=60, y=420, width=100, height=24)
        
        # image_2
        # Load image for image_2
        self.image_2_photo = tk.PhotoImage(file="path/to/image.png")
        self.image_2 = tk.Label(
            self.root,
            image=self.image_2_photo,
        )
        self.image_2.image = self.image_2_photo  # Keep reference
        self.image_2.place(x=50, y=400, width=20, height=20)
    
    # ==========================================
    # Event Handlers - Implement your logic here
    # ==========================================
    def keys(self, charcater):
        if charcater == "DELETE":
            current_text = self.entry_1.get()
            self.entry_1.delete(0, tk.END)
            self.entry_1.insert(0, current_text[:-1])
        elif charcater.isdigit():
            self.entry_1.insert(tk.END, charcater)
        elif charcater.isalpha():
            if not self.caps_on:
                charcater = charcater.lower()
            self.entry_1.insert(tk.END, charcater)
    def on_button_Q_click(self):
        self.keys("Q")
        pass
    
    def on_button_W_click(self):
        self.keys("W")
        pass
    
    def on_button_E_click(self):
        self.keys("E")
        pass
    
    def on_button_R_click(self):
        self.keys("R")
        pass
    
    def on_button_T_click(self):
        self.keys("T")
        pass
    
    def on_button_Y_click(self):
        self.keys("Y")
        pass
    
    def on_button_U_click(self):
        self.keys("U")
        pass
    
    def on_button_I_click(self):
        self.keys("I")
        pass
    
    def on_button_O_click(self):
        self.keys("O")
        pass
    
    def on_button_10_click(self):
        self.keys("")
        pass
    
    def on_button_P_click(self):
        self.keys("P")
        pass
    
    def on_button_F_click(self):
        self.keys("F")
        pass
    
    def on_button_D_click(self):
        self.keys("D")
        pass
    
    def on_button_S_click(self):
        self.keys("S")
        pass
    
    def on_button_A_click(self):
        
        self.keys("A")
        pass
    
    def on_button_L_click(self):
        self.keys("L")
        pass
    
    def on_button_G_click(self):
        self.keys("G")
        pass
    
    def on_button_K_click(self):
        self.keys("K")
        pass
    
    def on_button_J_click(self):
        self.keys("J")
        pass
    
    def on_button_H_click(self):
        self.keys("H")
        pass
    
    def on_button_DELETE_click(self):
        self.keys("DELETE")
        pass
    
    def on_button_M_click(self):
        self.keys("M")
        pass
    
    def on_button_N_click(self):
        self.keys("N")
        pass
    
    def on_button_B_click(self):
        self.keys("B")
        pass
    
    def on_button_V_click(self):
        self.keys("V")
        pass
    
    def on_button_C_click(self):
        self.keys("C")
        pass
    
    def on_button_X_click(self):
        self.keys("X")
        pass
    
    def on_button_Z_click(self):
        self.keys("Z")
        pass
    def on_button_0_click(self):
        self.keys("0")
        pass
    def on_button_1_click(self):
        self.keys("1")
        pass
    def on_button_2_click(self):
        self.keys("2")
        pass
    def on_button_3_click(self):
        self.keys("3")
        pass
    def on_button_4_click(self):
        self.keys("4")
        pass
    def on_button_5_click(self):
        self.keys("5")
        pass
    def on_button_6_click(self):
        self.keys("6")
        pass
    def on_button_7_click(self):
        self.keys("7")
        pass
    def on_button_8_click(self):
        self.keys("8")
        pass
    def on_button_9_click(self):
        self.keys("9")
        pass
    def on_button_enter_click(self):
        global typed_reg
        
        typed_reg = self.entry_2.get()
        self.target_entry.delete(0, tk.END)
        self.target_entry.insert(0, typed_reg)
        self.root.destroy()
        pass
       
    def on_button_returnb_click(self):
        self.app.show_home() 
        pass

    



class popupkeyboard:
    def __init__(self, root, app, _entry=None):

        self.root = root
        self.app = app
        self.root.title("Untitled Project")
        self.root.geometry("1368x900")
        self.root.resizable(True, True)
        self.caps_on= False
        self._create_widgets()
       
        # Initialize variables
        
    def _create_widgets(self):
        """Create and place all widgets"""
        self.frame = tk.Frame(self.root, width=1368, height=900)
        self.frame.place(x=0, y=0)
        self.frame.lift()
    
    
        
        # entry_2
        self.entry_2 = tk.Entry(
            self.root,
            font=("Arial", 12),
            bg="#ffffff",
            fg="#000000"
        )
        self.entry_2.place(x=334, y=110, width=700, height=50)
        self.entry_2.insert(0, "")  # Placeholder text
        
        # frame_1
        self.frame_1 = tk.Frame(
            self.root,
            bg="#f3f4f6",
            relief="groove",
            bd=1
        )
        self.frame_1.place(x=390, y=200, width=470, height=160)
        self.button_1 = tk.Button(
            self.root,
            text="1",
            font=("Arial", 12),
            command=lambda: self.keys("1")
        )
        self.button_1.place(x=400, y=230, width=30, height=20)
        self.button_2 = tk.Button(
            self.root,
            text="2",
            font=("Arial", 12),
            command=lambda: self.keys("2")
        )
        self.button_2.place(x=440, y=230, width=30, height=20)
        self.button_3 = tk.Button(
            self.root,
            text="3",
            font=("Arial", 12),
            command=lambda: self.keys("3")
        )
        self.button_3.place(x=480, y=230, width=30, height=20)
        
        self.button_4 = tk.Button(
            self.root,
            text="4",
            font=("Arial", 12),
            command=lambda: self.keys("4")
        )
        self.button_4.place(x=520, y=230, width=30, height=20)
        self.button_5 = tk.Button(
            self.root,
            text="5",
            font=("Arial", 12),
            command=lambda: self.keys("5")
        )
        self.button_5.place(x=560, y=230, width=30, height=20)
        self.button_6 = tk.Button(
            self.root,
            text="6",
            font=("Arial", 12),
            command=lambda: self.keys("6")
        )
        self.button_6.place(x=600, y=230, width=30, height=20)
        
        self.button_7 = tk.Button(
            self.root,
            text="7",
            font=("Arial", 12),
            command=lambda: self.keys("7")
        )
        self.button_7.place(x=640, y=230, width=30, height=20)
        self.button_8 = tk.Button(
            self.root,
            text="8",
            font=("Arial", 12),
            command=lambda: self.keys("8")
        )
        self.button_8.place(x=680, y=230, width=30, height=20)
        
        self.button_9 = tk.Button(
            self.root,
            text="9",
            font=("Arial", 12),
            command=lambda: self.keys("9")
        )
        self.button_9.place(x=720, y=230, width=30, height=20)
       
        self.button_0 = tk.Button(
            self.root,
            text="0",
            font=("Arial", 12),
            command=lambda: self.keys("0")
        )
        self.button_0.place(x=760, y=230, width=30, height=20)

        # button_1
        self.button_Q = tk.Button(
            self.root,
            text="Q",
            font=("Arial", 12),
            command=self.on_button_Q_click
        )
        self.button_Q.place(x=400, y=260, width=30, height=20)
        
        # button_2
        self.button_W = tk.Button(
            self.root,
            text="W",
            font=("Arial", 12),
            command=self.on_button_W_click
        )
        self.button_W.place(x=440, y=260, width=30, height=20)
        
        # button_3
        self.button_E = tk.Button(
            self.root,
            text="E",
            font=("Arial", 12),
            command=self.on_button_E_click
        )
        self.button_E.place(x=480, y=260, width=30, height=20)
        
        # button_4
        self.button_R = tk.Button(
            self.root,
            text="R",
            font=("Arial", 12),
            command=self.on_button_R_click
        )
        self.button_R.place(x=520, y=260, width=30, height=20)
        
        # button_5
        self.button_T = tk.Button(
            self.root,
            text="T",
            font=("Arial", 12),
            command=self.on_button_T_click
        )
        self.button_T.place(x=560, y=260, width=30, height=20)
        
        # button_6
        self.button_Y = tk.Button(
            self.root,
            text="Y",
            font=("Arial", 12),
            command=self.on_button_Y_click
        )
        self.button_Y.place(x=600, y=260, width=30, height=20)
        
        # button_7
        self.button_U = tk.Button(
            self.root,
            text="U",
            font=("Arial", 12),
            command=self.on_button_U_click
        )
        self.button_U.place(x=640, y=260, width=30, height=20)
        
        # button_8
        self.button_I = tk.Button(
            self.root,
            text="I",
            font=("Arial", 12),
            command=self.on_button_I_click
        )
        self.button_I.place(x=680, y=260, width=30, height=20)
        
        # button_9
        self.button_O = tk.Button(
            self.root,
            text="O",
            font=("Arial", 12),
            command=self.on_button_O_click
        )
        self.button_O.place(x=720, y=260, width=30, height=20)
        
        # button_10
        #self.button_del = tk.Button(
        #   self.root,
        #    text="Delete",
         #   font=("Arial", 12),
         #   command=self.on_button_del_click #ter
        #)
        #self.button_P.place(x=60, y=260, width=46, height=20)
        
        # button_11
        self.button_P = tk.Button(
            self.root,
            text="P",
            font=("Arial", 12),
            command=self.on_button_P_click
        )
        self.button_P.place(x=760, y=260, width=30, height=20)
        
        # button_18
        #self.button_Q = tk.Button(
            #self.root,
            #text="Q",
            #font=("Arial", 12),
            #command=self.on_button_Q_click
        #)
        #self.button_Q.place(x=100, y=290, width=30, height=20)
        
        # button_19
        #self.button_Q = tk.Button(
        #    self.root,
        #    text="Q",
        #    font=("Arial", 12),
        #    command=self.on_button_Q_click
        #)
        #self.button_Q.place(x=100, y=290, width=30, height=20)
        
        # button_14
        self.button_S = tk.Button(
            self.root,
            text="S",
            font=("Arial", 12),
            command=self.on_button_S_click
        )
        self.button_S.place(x=440, y=290, width=30, height=20)
        
        # button_15
        self.button_A = tk.Button(
            self.root,
            text="A",
            font=("Arial", 12),
            command=self.on_button_A_click
        )
        self.button_A.place(x=400, y=290, width=30, height=20)
        
        # button_16
        self.button_L = tk.Button(
            self.root,
            text="L",
            font=("Arial", 12),
            command=self.on_button_L_click
        )
        self.button_L.place(x=480, y=290, width=30, height=20)
        
        # button_17
        self.button_G = tk.Button(
            self.root,
            text="G",
            font=("Arial", 12),
            command=self.on_button_G_click
        )
        self.button_G.place(x=560, y=290, width=30, height=20)
        
        # button_18
        self.button_F = tk.Button(
            self.root,
            text="F",
            font=("Arial", 12),
            command=self.on_button_F_click
        )
        self.button_F.place(x=520, y=290, width=30, height=20)
        
        # button_19
        self.button_D = tk.Button(
            self.root,
            text="D",
            font=("Arial", 12),
            command=self.on_button_D_click
        )
        self.button_D.place(x=680, y=290, width=30, height=20)
        
        # button_20
        self.button_K = tk.Button(
            self.root,
            text="K",
            font=("Arial", 12),
            command=self.on_button_K_click
        )
        self.button_K.place(x=720, y=290, width=30, height=20)
        
        # button_21
        self.button_J = tk.Button(
            self.root,
            text="J",
            font=("Arial", 12),
            command=self.on_button_J_click
        )
        self.button_J.place(x=640, y=290, width=30, height=20)
        
        # button_22
        self.button_H = tk.Button(
            self.root,
            text="H",
            font=("Arial", 12),
            command=self.on_button_H_click
        )
        self.button_H.place(x=600, y=290, width=30, height=20)
        
        # button_23
        self.button_L = tk.Button(
            self.root,
            text="DELETE",
            font=("Arial", 12),
            command=self.on_button_DELETE_click
        )
        self.button_L.place(x=760, y=290, width=70, height=20)
        
        # button_24
        self.button_M = tk.Button(
            self.root,
            text="M",
            font=("Arial", 12),
            command=self.on_button_M_click
        )
        self.button_M.place(x=640, y=320, width=30, height=20)
        
        # button_25
        self.button_N = tk.Button(
            self.root,
            text="N",
            font=("Arial", 12),
            command=self.on_button_N_click
        )
        self.button_N.place(x=600, y=320, width=30, height=20)
        
        # button_26
        self.button_B = tk.Button(
            self.root,
            text="B",
            font=("Arial", 12),
            command=self.on_button_B_click
        )
        self.button_B.place(x=560, y=320, width=30, height=20)
        
        # button_27
        self.button_V = tk.Button(
            self.root,
            text="V",
            font=("Arial", 12),
            command=self.on_button_V_click
        )
        self.button_V.place(x=520, y=320, width=30, height=20)
        
        # button_28
        self.button_C = tk.Button(
            self.root,
            text="C",
            font=("Arial", 12),
            command=self.on_button_C_click
        )
        self.button_C.place(x=480, y=320, width=30, height=20)
        
        # button_29
        self.X = tk.Button(
            self.root,
            text="X",
            font=("Arial", 12),
            command=self.on_button_X_click
        )
        self.X.place(x=440, y=320, width=30, height=20)
        
        # button_30
        self.Z = tk.Button(
            self.root,
            text="Z",
            font=("Arial", 12),
            command=self.on_button_Z_click
        )
        self.Z.place(x=400, y=320, width=30, height=20)
        
        # button_31
        self.enter = tk.Button(
            self.root,
            text="Enter",
            font=("Arial", 12),
            command=self.on_button_enter_click
        )
        self.enter.place(x=800, y=310, width=50, height=20)
        self.enter = tk.Button(
            self.root,
            text="Enter",
            font=("Arial", 12),
            command=self.on_button_enter_click
        )
   
          # button_32
        self.returnb = tk.Button(
            self.root,
            text="Return to main menu",
            bg="#3b57f7",
            font=("Arial", 12),
            command=self.on_button_returnb_click
        )
        self.returnb.place(x=540, y=440, width=140, height=60)
        # image_2
        # Load image for image_2
        import base64
        from io import BytesIO
        from PIL import Image, ImageTk
        self.image_2_data = base64.b64decode("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")
        self.image_2_img = Image.open(BytesIO(self.image_2_data))
        self.image_2_img = self.image_2_img.resize((50, 20), Image.Resampling.LANCZOS)
        self.image_2_photo = ImageTk.PhotoImage(file ="path/to/image_2.png")
        self.image_2 = tk.Label(
            self.root,
            image=self.image_2_photo,
        )
        self.image_2.image = self.image_2_photo  # Keep reference
        self.image_2.place(x=170, y=170, width=50, height=20)
        
        # frame_2
        self.frame_2 = tk.Frame(
            self.root,
            bg="#f3f4f6",
            relief="groove",
            bd=1
        )
        self.frame_2.place(x=40, y=370, width=180, height=100)
        
        # label_4
        self.label_4 = tk.Label(
            self.root,
            text="Results",
            fg="#000000",
            font=("Arial", 12),
            anchor="center"
        )
        self.label_4.place(x=50, y=370, width=100, height=24)
        
        # label_5
        self.label_5 = tk.Label(
            self.root,
            text="Car park",
            fg="#000000",
            font=("Arial", 12),
            anchor="center"
        )
        self.label_5.place(x=50, y=400, width=120, height=20)
        
        # label_10
        self.label_10 = tk.Label(
            self.root,
            text="Cinema",
            fg="#000000",
            font=("Arial", 12),
            anchor="center"
        )
        self.label_10.place(x=60, y=420, width=100, height=24)
        
        # image_2
        # Load image for image_2
        self.image_2_photo = tk.PhotoImage(file="path/to/image.png")
        self.image_2 = tk.Label(
            self.root,
            image=self.image_2_photo,
        )
        self.image_2.image = self.image_2_photo  # Keep reference
        self.image_2.place(x=50, y=400, width=20, height=20)
    
    # ==========================================
    # Event Handlers - Implement your logic here
    # ==========================================
    def keys(self, charcater):
        if charcater == "DELETE":
            current_text = self.entry_2.get()
            self.entry_2.delete(0, tk.END)
            self.entry_2.insert(0, current_text[:-1])
        elif charcater.isdigit():
            self.entry_2.insert(tk.END, charcater)
        elif charcater.isalpha():
            if not self.caps_on:
                charcater = charcater.lower()
            self.entry_2.insert(tk.END, charcater)
    def on_button_Q_click(self):
        self.keys("Q")
        pass
    
    def on_button_W_click(self):
        self.keys("W")
        pass
    
    def on_button_E_click(self):
        self.keys("E")
        pass
    
    def on_button_R_click(self):
        self.keys("R")
        pass
    
    def on_button_T_click(self):
        self.keys("T")
        pass
    
    def on_button_Y_click(self):
        self.keys("Y")
        pass
    
    def on_button_U_click(self):
        self.keys("U")
        pass
    
    def on_button_I_click(self):
        self.keys("I")
        pass
    
    def on_button_O_click(self):
        self.keys("O")
        pass
    
    def on_button_10_click(self):
        self.keys("")
        pass
    
    def on_button_P_click(self):
        self.keys("P")
        pass
    
    def on_button_F_click(self):
        self.keys("F")
        pass
    
    def on_button_D_click(self):
        self.keys("D")
        pass
    
    def on_button_S_click(self):
        self.keys("S")
        pass
    
    def on_button_A_click(self):
        
        self.keys("A")
        pass
    
    def on_button_L_click(self):
        self.keys("L")
        pass
    
    def on_button_G_click(self):
        self.keys("G")
        pass
    
    def on_button_K_click(self):
        self.keys("K")
        pass
    
    def on_button_J_click(self):
        self.keys("J")
        pass
    
    def on_button_H_click(self):
        self.keys("H")
        pass
    
    def on_button_DELETE_click(self):
        self.keys("DELETE")
        pass
    
    def on_button_M_click(self):
        self.keys("M")
        pass
    
    def on_button_N_click(self):
        self.keys("N")
        pass
    
    def on_button_B_click(self):
        self.keys("B")
        pass
    
    def on_button_V_click(self):
        self.keys("V")
        pass
    
    def on_button_C_click(self):
        self.keys("C")
        pass
    
    def on_button_X_click(self):
        self.keys("X")
        pass
    
    def on_button_Z_click(self):
        self.keys("Z")
        pass
    def on_button_0_click(self):
        self.keys("0")
        pass
    def on_button_1_click(self):
        self.keys("1")
        pass
    def on_button_2_click(self):
        self.keys("2")
        pass
    def on_button_3_click(self):
        self.keys("3")
        pass
    def on_button_4_click(self):
        self.keys("4")
        pass
    def on_button_5_click(self):
        self.keys("5")
        pass
    def on_button_6_click(self):
        self.keys("6")
        pass
    def on_button_7_click(self):
        self.keys("7")
        pass
    def on_button_8_click(self):
        self.keys("8")
        pass
    def on_button_9_click(self):
        self.keys("9")
        pass
    
    
    def on_button_enter_click(self):
       
        text = self.entry_2.get()
        global typed_reg
        typed_reg = self.entry_2.get()
        self.app.show_parking()
        pass
       
    def on_button_returnb_click(self):
        self.app.show_parking() 
        pass


 
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import base64
from io import BytesIO
from PIL import Image, ImageTk
 
 
class carparking:
    def __init__(self, root):
        self.root = root
        self.root.title("Car_Parking")
        self.root.geometry("1920x1080")
        self.root.resizable(True, True)
       
        # Initialize variables
       
        # Create widgets
        self._create_widgets()
    def _create_widgets(self):
        self.frame = tk.Frame(self.root, width=1900, height=1000)
        self.frame.place(x=0, y=0)

        # Background
        self.Background_photo = tk.PhotoImage(file="assets/Inside_the_Trafford_Centre.png")
        self.Background = tk.Label(self.root, image=self.Background_photo, bg="#000000")
        self.Background.image = self.Background_photo
        self.Background.place(x=0, y=0, width=1740, height=1080)   
    
       
        # Logo
        # Load image for Logo
        self.Logo_photo = tk.PhotoImage(file="assets/Inside/Logo.png")
        self.Logo = tk.Label(
            self.root,
            image=self.Logo_photo,
        )
        self.Logo.image = self.Logo_photo  # Keep reference
        self.Logo.place(x=0, y=0, width=150, height=70)
       
        # Carparking_map
        # Load image for Carparking_map
        self.Carparking_map_photo = tk.PhotoImage(file="path/to/image.png")
        self.Carparking_map = tk.Label(
            self.root,
            image=self.Carparking_map_photo,
        )
        self.Carparking_map.image = self.Carparking_map_photo  # Keep reference
        self.Carparking_map.place(x=320, y=120, width=940, height=480)
       
        # The_Trafford_Centre_Car_parking
        self.The_Trafford_Centre_Car_parking  = tk.Label(
            self.root,
            text="The Trafford Centre Car parking ",
            fg="#ffffff",
            font=("Arial", 23),
            anchor="center"
        )
        self.The_Trafford_Centre_Car_parking .place(x=460, y=20, width=390, height=40)
       
        # Regent _Car_park
        self.Regent_Car_park = tk.Button(
            self.frame,
            text="Regent Car park",
            font=("Arial", 12),
            command=self.on_Regent_Car_park_click
        )
        self.Regent_Car_park.place(x=20, y=240, width=280, height=40)
       
        # Peel_Car_Park
        self.Peel_Car_Park = tk.Button(
            self.frame,
            text="Peel Car Park",
            font=("Arial", 12),
            command=self.on_Peel_Car_Park_click
        )
        self.Peel_Car_Park.place(x=20, y=320, width=280, height=40)
       
        # Orient_Car_Park
        self.Orient_Car_Park = tk.Button(
            self.frame,
            text="Orient Car Park",
            font=("Arial", 12),
            command=self.on_Orient_Car_Park_click
        )
        self.Orient_Car_Park.place(x=20, y=400, width=280, height=40)
       
        # Parking_space
        self.Parking_space = tk.Label(
            self.root,
            text="Find Parking, Check availability and Parking information ",
            fg="#fdfcfc",
            font=("Arial", 18),
            anchor="center"
        )
        self.Parking_space.place(x=20, y=100, width=280, height=70)
       
        # Parking_rates_and_other_information
        self.Parking_rates_and_other_information = tk.Button(
            self.frame,
            text="Parking rates and other information",
            font=("Arial", 12),
            command=self.on_Parking_rates_and_other_information_click
        )
        self.Parking_rates_and_other_information.place(x=20, y=480, width=280, height=40)
       
        # Exit_button
        self.Exit_button = tk.Button(
            self.frame,
            text="Exit",
            font=("Arial", 12),
            command=self.on_Exit_button_click
        )
        self.Exit_button.place(x=20, y=560, width=280, height=40)
       
        # search_button
        self.search_button = tk.Entry(
            self.root,
            font=("Arial", 16),
            bg="#ffffff",
            fg="#000000"
        )
        self.search_button.place(x=600, y=660, width=480, height=50)
        self.search_button.insert(0, "Search for stores, services and facilities")  # Placeholder text
       
        # frame_1
        self.frame_1 = tk.Frame(
            self.root,
            bg="#d1d1d1",
            relief="groove",
            bd=1
        )
        self.frame_1.place(x=270, y=740, width=1120, height=334)
       
        # button_Q
        self.button_Q = tk.Button(
            self.frame,
            text="Q",
            bg="#f0f0f0",
            fg="#000000",
            font=("Times New Roman", 25),
            command=self.on_button_Q_click
        )
        self.button_Q.place(x=310, y=760, width=60, height=50)
       
        # button_E
        self.button_E = tk.Button(
            self.frame,
            text="E",
            bg="#f0f0f0",
            fg="#000000",
            font=("Times New Roman", 25),
            command=self.on_button_E_click
        )
        self.button_E.place(x=490, y=760, width=60, height=50)
       
        # button_W
        self.button_W = tk.Button(
            self.frame,
            text="W",
            bg="#f0f0f0",
            fg="#000000",
            font=("Times New Roman", 25),
            command=self.on_button_W_click
        )
        self.button_W.place(x=400, y=760, width=60, height=50)
       
        # button_R
        self.button_R = tk.Button(
            self.frame,
            text="R",
            bg="#f0f0f0",
            fg="#000000",
            font=("Times New Roman", 25),
            command=self.on_button_R_click
        )
        self.button_R.place(x=580, y=760, width=60, height=50)
       
        # button_T
        self.button_T = tk.Button(
            self.frame,
            text="T",
            bg="#f0f0f0",
            fg="#000000",
            font=("Times New Roman", 25),
            command=self.on_button_T_click
        )
        self.button_T.place(x=670, y=760, width=60, height=50)
       
        # button_Y
        self.button_Y = tk.Button(
            self.frame,
            text="Y",
            bg="#f0f0f0",
            fg="#000000",
            font=("Times New Roman", 25),
            command=self.on_button_Y_click
        )
        self.button_Y.place(x=760, y=760, width=60, height=50)
       
        # button_U
        self.button_U = tk.Button(
            self.frame,
            text="U",
            bg="#f0f0f0",
            fg="#000000",
            font=("Times New Roman", 25),
            command=self.on_button_U_click
        )
        self.button_U.place(x=850, y=760, width=60, height=50)
       
        # button_I
        self.button_I = tk.Button(
            self.frame,
            text="I",
            bg="#f0f0f0",
            fg="#000000",
            font=("Times New Roman", 25),
            command=self.on_button_I_click
        )
        self.button_I.place(x=940, y=760, width=60, height=50)
       
        # button_14
        self.button_14 = tk.Button(
            self.frame,
            text="Button",
            bg="#f0f0f0",
            font=("Arial", 12),
            command=self.on_button_14_click
        )
        self.button_14.place(x=1030, y=760, width=60, height=50)
       
        # button_O
        self.button_O = tk.Button(
            self.frame,
            text="O",
            bg="#f0f0f0",
            fg="#000000",
            font=("Times New Roman", 25),
            command=self.on_button_O_click
        )
        self.button_O.place(x=1030, y=760, width=60, height=50)
       
        # button_P
        self.button_P = tk.Button(
            self.frame,
            text="P",
            bg="#f0f0f0",
            fg="#000000",
            font=("Times New Roman", 25),
            command=self.on_button_P_click
        )
        self.button_P.place(x=1130, y=760, width=60, height=50)
       
        # button_Delete
        self.button_Delete = tk.Button(
            self.frame,
            text="Delete",
            bg="#f0f0f0",
            fg="#000000",
            font=("Times New Roman", 25),
            command=self.on_button_Delete_click
        )
        self.button_Delete.place(x=1220, y=760, width=130, height=50)
       
        # button_A
        self.button_A = tk.Button(
            self.frame,
            text="A",
            bg="#f0f0f0",
            fg="#000000",
            font=("Times New Roman", 25),
            command=self.on_button_A_click
        )
        self.button_A.place(x=358, y=839, width=60, height=50)
       
        # button_S
        self.button_S = tk.Button(
            self.frame,
            text="S",
            bg="#f0f0f0",
            fg="#000000",
            font=("Times New Roman", 25),
            command=self.on_button_S_click
        )
        self.button_S.place(x=450, y=839, width=60, height=50)
       
        # button_D
        self.button_D = tk.Button(
            self.frame,
            text="D",
            bg="#f0f0f0",
            fg="#000000",
            font=("Times New Roman", 25),
            command=self.on_button_D_click
        )
        self.button_D.place(x=540, y=840, width=60, height=50)
       
        # button_F
        self.button_F = tk.Button(
            self.frame,
            text="F",
            bg="#f0f0f0",
            fg="#000000",
            font=("Times New Roman", 25),
            command=self.on_button_F_click
        )
        self.button_F.place(x=630, y=840, width=60, height=50)
       
        # button_G
        self.button_G = tk.Button(
            self.frame,
            text="G",
            bg="#f0f0f0",
            fg="#000000",
            font=("Times New Roman", 25),
            command=self.on_button_G_click
        )
        self.button_G.place(x=720, y=839, width=60, height=50)
       
        # button_H
        self.button_H = tk.Button(
            self.frame,
            text="H",
            bg="#f0f0f0",
            fg="#000000",
            font=("Times New Roman", 25),
            command=self.on_button_H_click
        )
        self.button_H.place(x=810, y=839, width=60, height=50)
       
        # button_J
        self.button_J = tk.Button(
            self.frame,
            text="J",
            bg="#f0f0f0",
            fg="#000000",
            font=("Times New Roman", 25),
            command=self.on_button_J_click
        )
        self.button_J.place(x=900, y=839, width=60, height=50)
       
        # button_K
        self.button_K = tk.Button(
            self.frame,
            text="K",
            bg="#f0f0f0",
            fg="#000000",
            font=("Times New Roman", 25),
            command=self.on_button_K_click
        )
        self.button_K.place(x=990, y=839, width=60, height=50)
       
        # button_L
        self.button_L = tk.Button(
            self.frame,
            text="L",
            bg="#f0f0f0",
            fg="#000000",
            font=("Times New Roman", 25),
            command=self.on_button_L_click
        )
        self.button_L.place(x=1080, y=839, width=60, height=50)
       
        # button_Enter
        self.button_Enter = tk.Button(
            self.frame,
            text="Enter",
            bg="#f0f0f0",
            fg="#000000",
            font=("Times New Roman", 25),
            command=self.on_button_Enter_click
        )
        self.button_Enter.place(x=1169, y=839, width=130, height=50)
       
        # button_Z
        self.button_Z = tk.Button(
            self.frame,
            text="Z",
            bg="#f0f0f0",
            fg="#000000",
            font=("Times New Roman", 25),
            command=self.on_button_Z_click
        )
        self.button_Z.place(x=310, y=912, width=60, height=50)
       
        # button_X
        self.button_X = tk.Button(
            self.frame,
            text="X",
            bg="#f0f0f0",
            fg="#000000",
            font=("Times New Roman", 25),
            command=self.on_button_X_click
        )
        self.button_X.place(x=400, y=910, width=60, height=50)
       
        # button_30
        self.button_30 = tk.Button(
            self.frame,
            text="Button",
            bg="#f0f0f0",
            font=("Arial", 12),
            command=self.on_button_30_click
        )
        self.button_30.place(x=490, y=910, width=60, height=50)
       
        # button_C
        self.button_C = tk.Button(
            self.frame,
            text="C",
            bg="#f0f0f0",
            fg="#000000",
            font=("Times New Roman", 25),
            command=self.on_button_C_click
        )
        self.button_C.place(x=490, y=910, width=60, height=50)
       
        # button_V
        self.button_V = tk.Button(
            self.frame,
            text="V",
            bg="#f0f0f0",
            fg="#000000",
            font=("Times New Roman", 25),
            command=self.on_button_V_click
        )
        self.button_V.place(x=580, y=912, width=60, height=50)
       
        # button_B
        self.button_B = tk.Button(
            self.frame,
            text="B",
            bg="#f0f0f0",
            fg="#000000",
            font=("Times New Roman", 25),
            command=self.on_button_B_click
        )
        self.button_B.place(x=672, y=912, width=60, height=50)
       
        # button_N
        self.button_N = tk.Button(
            self.frame,
            text="N",
            bg="#f0f0f0",
            fg="#000000",
            font=("Times New Roman", 25),
            command=self.on_button_N_click
        )
        self.button_N.place(x=769, y=912, width=60, height=50)
       
        # button_M
        self.button_M = tk.Button(
            self.frame,
            text="M",
            bg="#f0f0f0",
            fg="#000000",
            font=("Times New Roman", 25),
            command=self.on_button_M_click
        )
        self.button_M.place(x=858, y=912, width=60, height=50)
       
        # button_atsymbol
        self.button_atsymbol = tk.Button(
            self.frame,
            text="@",
            bg="#f0f0f0",
            fg="#000000",
            font=("Times New Roman", 25),
            command=self.on_button_atsymbol_click
        )
        self.button_atsymbol.place(x=960, y=911, width=60, height=50)
       
        # button_Space
        self.button_Space = tk.Button(
            self.frame,
            text="Space",
            bg="#f0f0f0",
            fg="#000000",
            font=("Times New Roman", 25),
            command=self.on_button_Space_click
        )
        self.button_Space.place(x=1050, y=911, width=130, height=50)
       
        # 0
        self.zero = tk.Button(
            self.frame,
            text="0",
            bg="#f0f0f0",
            fg="#000000",
            font=("Times New Roman", 25),
            command=self.on_zero_click
        )
        self.zero.place(x=310, y=1000, width=60, height=50)
       
        # 1
        self.one = tk.Button(
            self.frame,
            text="1",
            bg="#f0f0f0",
            fg="#000000",
            font=("Times New Roman", 25),
            command=self.on_one_click
        )
        self.one.place(x=400, y=1000, width=60, height=50)
       
        # 3
        self.three = tk.Button(
            self.frame,
            text="3",
            bg="#f0f0f0",
            fg="#000000",
            font=("Times New Roman", 25),
            command=self.on_three_click
        )
        self.three.place(x=590, y=1000, width=60, height=50)
       
        # 4
        self.four = tk.Button(
            self.frame,
            text="4",
            bg="#f0f0f0",
            fg="#000000",
            font=("Times New Roman", 25),
            command=self.on_four_click
        )
        self.four.place(x=680, y=1000, width=60, height=50)
       
        # 5
        self.five = tk.Button(
            self.frame,
            text="5",
            bg="#f0f0f0",
            fg="#000000",
            font=("Times New Roman", 25),
            command=self.on_five_click
        )
        self.five.place(x=770, y=1000, width=60, height=50)
       
        # 6
        self.six = tk.Button(
            self.frame,
            text="6",
            bg="#f0f0f0",
            fg="#000000",
            font=("Times New Roman", 25),
            command=self.on_six_click
        )
        self.six.place(x=860, y=1000, width=60, height=50)
       
        # 7
        self.seven = tk.Button(
            self.frame,
            text="7",
            bg="#f0f0f0",
            fg="#000000",
            font=("Times New Roman", 25),
            command=self.on_seven_click
        )
        self.seven.place(x=950, y=1000, width=60, height=50)
       
        # 8
        self.eight = tk.Button(
            self.frame,
            text="8",
            bg="#f0f0f0",
            fg="#000000",
            font=("Times New Roman", 25),
            command=self.on_eight_click
        )
        self.eight.place(x=1040, y=1000, width=60, height=50)
       
        # 2
        self.two = tk.Button(
            self.frame,
            text="2",
            bg="#f0f0f0",
            fg="#000000",
            font=("Times New Roman", 25),
            command=self.on_two_click
        )
        self.two.place(x=500, y=1000, width=60, height=50)
       
        # 3
        self.three = tk.Button(
            self.frame,
            text="9",
            bg="#f0f0f0",
            fg="#000000",
            font=("Times New Roman", 25),
            command=self.on_three_click
        )
        self.three.place(x=1130, y=1000, width=60, height=50)
   
    # ==========================================
    # Event Handlers - Implement your logic here
    # ==========================================
    def on_key_click(self, charcter):
        if charcter == 'Delete':
            pass
        else:
            pass
 
    def on_button_Q_click(self):
        self.on_key_click('Q')
        pass
   
    def on_button_E_click(self):
        self.on_key_click('E')
        pass
   
    def on_button_W_click(self):
        self.on_key_click('W')
        pass
   
    def on_button_R_click(self):
        self.on_key_click('R')
        pass
   
    def on_button_T_click(self):
        self.on_key_click('T')
        pass
   
    def on_button_Y_click(self):
        self.on_key_click('Y')
        pass
   
    def on_button_U_click(self):
        self.on_key_click('U')
        pass
   
    def on_button_I_click(self):
        self.on_key_click('I')
        pass
   
    def on_button_14_click(self):
        self.on_key_click('14')
        pass
   
    def on_button_O_click(self):
        self.on_key_click('O')
        pass
   
    def on_button_P_click(self):
        self.on_key_click('P')
        pass
   
    def on_button_Delete_click(self):
        self.on_key_click('Delete')
        pass
   
    def on_button_A_click(self):
        self.on_key_click('A')
        pass
   
    def on_button_S_click(self):
        self.on_key_click('S')
        pass
   
    def on_button_D_click(self):
        self.on_key_click('D')
        pass
   
    def on_button_F_click(self):
        self.on_key_click('F')
        pass
   
    def on_button_G_click(self):
        self.on_key_click('G')
        pass
   
    def on_button_H_click(self):
        self.on_key_click('H')
        pass
   
    def on_button_J_click(self):
        self.on_key_click('J')
        pass
   
    def on_button_K_click(self):
        self.on_key_click('K')
        pass
   
    def on_button_L_click(self):
        self.on_key_click('L')
        pass
   
    def on_button_Enter_click(self):
        self.on_key_click('Enter')
        pass
   
    def on_button_Z_click(self):
        self.on_key_click('Z')
        pass
   
    def on_button_X_click(self):
        self.on_key_click('X')
        pass
   
    def on_button_30_click(self):
        self.on_key_click('30')
        pass
   
    def on_button_C_click(self):
        self.on_key_click('C')
        pass
   
    def on_button_V_click(self):
        self.on_key_click('V')
        pass
   
    def on_button_B_click(self):
        self.on_key_click('B')
       
        pass
   
    def on_button_N_click(self):
        self.on_key_click('N')
        pass
   
    def on_button_M_click(self):
        self.on_key_click('M')
        pass
   
    def on_button_atsymbol_click(self):
        self.on_key_click('@')
        pass
   
    def on_button_Space_click(self):
        self.on_key_click('Space')
        pass
   
    def on_0_click(self):
        self.on_key_click('0')
        pass
   
    def on_one_click(self):
        self.on_key_click('1')
        pass
   
    def on_three_click(self):
        self.on_key_click('3')
        pass
   
    def on_four_click(self):
        self.on_key_click('4')
        pass
   
    def on_five_click(self):
        self.on_key_click('5')
        pass
   
    def on_six_click(self):
        self.on_key_click('6')
        pass
   
    def on_seven_click(self):
        self.on_key_click('7')
        pass
   
    def on_eight_click(self):
        self.on_key_click('8')
        pass
   
    def on_2_click(self):
        self.on_key_click('2')
        pass
   
   
   
   
 
if __name__ == "__main__":
    root = tk.Tk()
    app = carparking(root)
    root.mainloop()
 
 
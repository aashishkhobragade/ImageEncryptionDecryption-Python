import tkinter as tk
from PIL import Image, ImageTk
import cv2


master = tk.Tk()
master.title("")
master.geometry("1000x600")

bgcolor = "#FFF2CC"
bgcolor2 = "#FFD966"



# Container 1 for Encryption Interface
container1 = tk.Frame(master, bg=bgcolor, width=300)
container1.pack(side="left", fill="both", expand=True)

label = tk.Label(container1, text="Image Encryption and Decryption", fg="#000000",bg=bgcolor,font=("Arial", 20))
label.pack(padx=10,pady=20)


containerUpload = tk.Frame(container1,bg =bgcolor2 ,width=300,height=300)
containerUpload.pack(pady=50)



# Container 2 for Decryption Interface
container2 = tk.Frame(master, bg=bgcolor2, width=400)
container2.pack(side="right", fill="both", expand=False)

master.mainloop()

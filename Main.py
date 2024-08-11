import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

# Basic Structure 
master = tk.Tk()
master.title("Image Encryption and Decryption")
master.geometry("1000x600")

# Color scheme
bgcolor = "#FFF2CC"    # Background color for container1
bgcolor2 = "#FFD966"   # Background color for containerUpload and container2
button_bg = "#FFD966"  # Background color for the buttons
button_fg = "#000000"  # Foreground (text) color for the buttons

# Important Functions 
def choose_image():
    # Open a file dialog to select an image
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg"), ("PNG files", "*.png")])
    if file_path:
        # Load and display the selected image
        image = Image.open(file_path)
        image = image.resize((280, 280), Image.Resampling.HAMMING)  # Resize the image if needed
        photo = ImageTk.PhotoImage(image)
        image_label.config(image=photo)
        image_label.image = photo  # Keep a reference to avoid garbage collection

def reset_image():
    # Reset the image to the initial image
    image = Image.open(initial_image_path)
    image = image.resize((100, 100), Image.Resampling.HAMMING)  # Resize the image if needed
    photo = ImageTk.PhotoImage(image)
    image_label.config(image=photo)
    image_label.image = photo  # Keep a reference to avoid garbage collection

# Container 1 for Encryption Interface
container1 = tk.Frame(master, bg=bgcolor, width=250)
container1.pack(side="left", fill="both", expand=True)

label = tk.Label(container1, text="Image Encryption and Decryption", fg=button_fg, bg=bgcolor, font=("Arial", 20))
label.pack(padx=10, pady=20)

labelActual = tk.Label(container1, text="Actual Image", bg=bgcolor ,fg=button_fg)
labelActual.pack(padx=10, pady=10)

containerUpload = tk.Frame(container1, bg=bgcolor2, width=300, height=300)
containerUpload.pack(pady=50, padx=0)

# Initial image display
initial_image_path = 'ImageEncryptionDecryption-Python/Resources/intial.png'  # Ensure the path is correct
image = Image.open(initial_image_path)
image = image.resize((100, 100), Image.Resampling.HAMMING)
photo = ImageTk.PhotoImage(image)

# Create a label to hold the image
image_label = tk.Label(containerUpload, image=photo, bg=bgcolor2)
image_label.place(relx=0.5, rely=0.5, anchor='center')  # Center the image



# Buttons
button_frame = tk.Frame(container1, bg=bgcolor)  # Frame to hold both buttons
button_frame.pack(pady=20)

# Load an image for the choose button with a transparent background
choose_image_path = 'ImageEncryptionDecryption-Python/Resources/reset.png'  # Replace with your image path
choose_img = Image.open(choose_image_path)
choose_img = choose_img.resize((150, 50), Image.Resampling.HAMMING)  # Stretch the image to fit the button
choose_photo = ImageTk.PhotoImage(choose_img)

choose_button = tk.Button(button_frame, image=choose_photo, command=choose_image, bg=bgcolor, bd=0, highlightthickness=0, relief="flat", activebackground=bgcolor)
choose_button.image = choose_photo  # Keep a reference to avoid garbage collection
choose_button.pack(side="left", padx=5)

# Load an image for the reset button
reset_image_path = 'ImageEncryptionDecryption-Python/Resources/upload.png'  # Replace with your image path
reset_img = Image.open(reset_image_path)
reset_img = reset_img.resize((160, 50), Image.Resampling.HAMMING)  # Stretch the image to fit the button
reset_photo = ImageTk.PhotoImage(reset_img)

reset_button = tk.Button(button_frame, image=reset_photo, command=reset_image, bg=bgcolor, bd=0, highlightthickness=0, relief="flat", activebackground=bgcolor)
reset_button.image = reset_photo  # Keep a reference to avoid garbage collection
reset_button.pack(side="left", padx=5)

# Container 2 for Decryption Interface
container2 = tk.Frame(master, bg=bgcolor2, width=400)
container2.pack(side="right", fill="both", expand=False)





master.mainloop()

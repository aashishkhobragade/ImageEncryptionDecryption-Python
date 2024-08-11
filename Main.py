import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox as mbox
from PIL import Image, ImageTk
import numpy as np
import cv2

# Basic Structure
master = tk.Tk()
master.title("Image Encryption and Decryption")
master.geometry("1200x700")

# Color scheme
bgcolor = "#FFF2CC"    # Background color for container1
bgcolor2 = "#FFD966"   # Background color for containerUpload and container2
button_bg = "#FFD966"  # Background color for the buttons
button_fg = "#000000"  # Foreground (text) color for the buttons

# Variables
image_path = None
image_encrypted = None
key = None

# Functions
def choose_image():
    global image_path
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg"), ("PNG files", "*.png")])
    if file_path:
        image_path = file_path
        image = Image.open(file_path)
        image = image.resize((280, 280), Image.Resampling.HAMMING)
        photo = ImageTk.PhotoImage(image)
        image_label.config(image=photo)
        image_label.image = photo  # Keep a reference to avoid garbage collection

def reset_image():
    if image_path:
        image = Image.open(image_path)
        image = image.resize((100, 100), Image.Resampling.HAMMING)
        photo = ImageTk.PhotoImage(image)
        image_label.config(image=photo)
        image_label.image = photo  # Keep a reference to avoid garbage collection

def encrypt_image():
    global image_encrypted, key
    if image_path:
        try:
            image_input = cv2.imread(image_path, 0)
            (x1, y) = image_input.shape
            image_input = image_input.astype(float) / 255.0

            mu, sigma = 0, 0.1  # mean and standard deviation
            key = np.random.normal(mu, sigma, (x1, y)) + np.finfo(float).eps
            image_encrypted = image_input / key
            cv2.imwrite('image_encrypted.jpg', image_encrypted * 255)

            imge = Image.open('image_encrypted.jpg')
            imge = imge.resize((280, 280), Image.Resampling.HAMMING)
            photo = ImageTk.PhotoImage(imge)
            image_label2.config(image=photo)
            image_label2.image = photo  # Keep a reference to avoid garbage collection

            mbox.showinfo("Encrypt Status", "Image Encrypted successfully.")
        except Exception as e:
            mbox.showerror("Encryption Error", f"An error occurred: {e}")

def decrypt_image():
    if image_encrypted is not None and key is not None:
        try:
            image_output = image_encrypted * key
            image_output = np.clip(image_output * 255.0, 0, 255).astype(np.uint8)
            cv2.imwrite('image_output.jpg', image_output)

            imgd = Image.open('image_output.jpg')
            imgd = imgd.resize((280, 280), Image.Resampling.HAMMING)
            photo = ImageTk.PhotoImage(imgd)
            image_label2.config(image=photo)
            image_label2.image = photo  # Keep a reference to avoid garbage collection

            mbox.showinfo("Decrypt Status", "Image decrypted successfully.")
        except Exception as e:
            mbox.showerror("Decryption Error", f"An error occurred: {e}")

def download_image():
    if image_encrypted is not None:
        try:
            filename = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG files", "*.jpg")])
            if filename:
                cv2.imwrite(filename, image_encrypted * 255)
                mbox.showinfo("Save Status", "Encrypted Image Saved Successfully!")
        except Exception as e:
            mbox.showerror("Save Error", f"An error occurred: {e}")

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
initial_image_path = 'ImageEncryptionDecryption-Python/Resources/intial.png'
try:
    image = Image.open(initial_image_path)
    image = image.resize((100, 100), Image.Resampling.HAMMING)
    photo = ImageTk.PhotoImage(image)
    image_label = tk.Label(containerUpload, image=photo, bg=bgcolor2)
    image_label.place(relx=0.5, rely=0.5, anchor='center')
except FileNotFoundError:
    mbox.showwarning("File Not Found", f"Initial image file '{initial_image_path}' not found.")

# Buttons
button_frame = tk.Frame(container1, bg=bgcolor)
button_frame.pack(pady=20)

choose_image_path = 'ImageEncryptionDecryption-Python/Resources/upload.png'
try:
    choose_img = Image.open(choose_image_path)
    choose_img = choose_img.resize((150, 50), Image.Resampling.HAMMING)
    choose_photo = ImageTk.PhotoImage(choose_img)
    choose_button = tk.Button(button_frame, image=choose_photo, command=choose_image, bg=bgcolor, bd=0, highlightthickness=0, relief="flat", activebackground=bgcolor)
    choose_button.image = choose_photo
    choose_button.pack(side="left", padx=5)
except FileNotFoundError:
    mbox.showwarning("File Not Found", f"Image file '{choose_image_path}' not found.")

reset_image_path = 'ImageEncryptionDecryption-Python/Resources/reset.png'
try:
    reset_img = Image.open(reset_image_path)
    reset_img = reset_img.resize((160, 50), Image.Resampling.HAMMING)
    reset_photo = ImageTk.PhotoImage(reset_img)
    reset_button = tk.Button(button_frame, image=reset_photo, command=reset_image, bg=bgcolor, bd=0, highlightthickness=0, relief="flat", activebackground=bgcolor)
    reset_button.image = reset_photo
    reset_button.pack(side="left", padx=5)
except FileNotFoundError:
    mbox.showwarning("File Not Found", f"Image file '{reset_image_path}' not found.")

# Container 2 for Decryption Interface
container2 = tk.Frame(master, bg=bgcolor2, width=400)
container2.pack(side="right", fill="both", expand=False)

label2 = tk.Label(container2, text="Processed Image Result", fg=button_fg, bg=bgcolor2, font=("Arial", 20))
label2.pack(padx=10, pady=20)

labelProcessed = tk.Label(container2, text="Processed Image", bg=bgcolor2 ,fg=button_fg)
labelProcessed.pack(padx=10, pady=10)

containerDownload = tk.Frame(container2, bg=bgcolor, width=300, height=300)
containerDownload.pack(pady=50, padx=90)

# Initial image display
image_label2 = tk.Label(containerDownload, bg=bgcolor)
image_label2.place(relx=0.5, rely=0.5, anchor='center')

# Buttons for Container 2 (Decryption Interface)
button_frame2 = tk.Frame(container2, bg=bgcolor2)
button_frame2.pack(pady=20)

# Load an image for the encrypt button
encrypt_image_path = 'ImageEncryptionDecryption-Python/Resources/enc.png'
try:
    encrypt_img = Image.open(encrypt_image_path)
    encrypt_img = encrypt_img.resize((160, 50), Image.Resampling.HAMMING)
    encrypt_photo = ImageTk.PhotoImage(encrypt_img)
    encrypt_button = tk.Button(button_frame2, image=encrypt_photo, command=encrypt_image, bg=bgcolor2, bd=0, highlightthickness=0, relief="flat", activebackground=bgcolor2)
    encrypt_button.image = encrypt_photo
    encrypt_button.pack(side="left", padx=5)
except FileNotFoundError:
    mbox.showwarning("File Not Found", f"Image file '{encrypt_image_path}' not found.")

# Load an image for the decrypt button
decrypt_image_path = 'ImageEncryptionDecryption-Python/Resources/dec.png'
try:
    decrypt_img = Image.open(decrypt_image_path)
    decrypt_img = decrypt_img.resize((160, 50), Image.Resampling.HAMMING)
    decrypt_photo = ImageTk.PhotoImage(decrypt_img)
    decrypt_button = tk.Button(button_frame2, image=decrypt_photo, command=decrypt_image, bg=bgcolor2, bd=0, highlightthickness=0, relief="flat", activebackground=bgcolor2)
    decrypt_button.image = decrypt_photo
    decrypt_button.pack(side="left", padx=5)
except FileNotFoundError:
    mbox.showwarning("File Not Found", f"Image file '{decrypt_image_path}' not found.")

# Download Image Button
download_image_path = 'ImageEncryptionDecryption-Python/Resources/download.png'
try:
    download_img = Image.open(download_image_path)
    download_img = download_img.resize((340, 50), Image.Resampling.HAMMING)
    download_photo = ImageTk.PhotoImage(download_img)
    download_button = tk.Button(container2, image=download_photo, command=download_image, bg=bgcolor2, bd=0, highlightthickness=0, relief="flat", activebackground=bgcolor2)
    download_button.image = download_photo
    download_button.pack(padx=5, pady=5)
except FileNotFoundError:
    mbox.showwarning("File Not Found", f"Image file '{download_image_path}' not found.")

master.mainloop()

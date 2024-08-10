button = Button(root, text="Click me!")
img = PhotoImage(file="C:/path to image/example.gif") # make sure to add "/" not "\"
button.config(image=img)
button.pack()
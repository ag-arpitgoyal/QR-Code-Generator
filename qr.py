import qrcode
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import Label

def generate_qr():
    website_link = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'

    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(website_link)
    qr.make()

    img = qr.make_image(fill_color='black', back_color='white')
    # img.save('youtube_qr.png')

    # Display the image in the Tkinter window
    img_tk = ImageTk.PhotoImage(img)
    label.config(image=img_tk)
    label.image = img_tk

# Create the main window
root = tk.Tk()
root.title("QR Code Generator")

# Create a button to generate the QR code
button = tk.Button(root, text="Generate QR Code", command=generate_qr)
button.pack(pady=20)

# Create a label to display the QR code
label = Label(root)
label.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()
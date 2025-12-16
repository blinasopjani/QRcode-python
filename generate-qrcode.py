import qrcode
import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk

def generate_qr():
    url = url_entry.get().strip()
    if not url:
        messagebox.showwarning("Warning", "Please enter a URL!")
        return
    
    # Generate QR code
    qr_img = qrcode.make(url)
    
    # Display QR code in the GUI
    qr_img_resized = qr_img.resize((300, 300))  # Resize to fit GUI
    qr_img_tk = ImageTk.PhotoImage(qr_img_resized)
    qr_label.config(image=qr_img_tk)
    qr_label.image = qr_img_tk
    
    # Ask where to save
    file_path = filedialog.asksaveasfilename(defaultextension=".png",filetypes=[("PNG files", "*.png")])
    if file_path:
        qr_img.save(file_path)
        messagebox.showinfo("Success", f"QR code saved as {file_path}")

# Main window
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("500x500")
root.configure(bg="#f0f0f0")

# Title
title = tk.Label(root, text="QR Code Generator", font=("Helvetica", 20, "bold"), bg="#f0f0f0")
title.pack(pady=20)

# URL
url_entry = tk.Entry(root, font=("Helvetica", 14), width=40)
url_entry.pack(pady=10)

# Generate button
generate_button = tk.Button(root, text="Generate QR Code", font=("Helvetica", 14), bg="#4CAF50", fg="white", command=generate_qr)
generate_button.pack(pady=20)

# Display QR code
qr_label = tk.Label(root, bg="#f0f0f0")
qr_label.pack(pady=20)

root.mainloop()

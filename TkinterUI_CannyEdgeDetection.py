import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
import os
from matplotlib import pyplot as plt

class CannyEdgeDetectionApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Canny Edge Detection GUI")

        self.img_path = tk.StringVar()

        self.frame = tk.Frame(self.window)
        self.frame.pack(padx=10, pady=10)

        self.img_label = tk.Label(self.frame)
        self.img_label.pack(padx=5, pady=5)

        self.button = tk.Button(self.frame, text="Open Image", command=self.open_image)
        self.button.pack(padx=5, pady=5)

        self.apply_button = tk.Button(self.frame, text="Apply Canny Edge Detection", command=self.apply_canny)
        self.apply_button.pack(padx=5, pady=5)

        self.canny_edge_img = None

    def open_image(self):
        self.img_path.set(filedialog.askopenfilename())

        self.image = Image.open(self.img_path.get())
        self.photo = ImageTk.PhotoImage(self.image)
        self.img_label.config(image=self.photo)
        self.img_label.image = self.photo

    def apply_canny(self):
        if not self.img_path.get():
            return

        image = cv2.imread(self.img_path.get())
        gray_image = cv2.cvtColor(image, cv2.IMREAD_GRAYSCALE)
        canny_edge_img = cv2.Canny(gray_image, 100, 200)

        cv2.imwrite('canny_edge_image.jpg', canny_edge_img)

        self.canny_edge_img = Image.open('canny_edge_image.jpg')
        self.photo = ImageTk.PhotoImage(self.canny_edge_img)
        self.img_label.config(image=self.photo)
        self.img_label.image = self.photo

root = tk.Tk()
root.title("Canny Edge Detection GUI")
app = CannyEdgeDetectionApp(root)
root.mainloop()

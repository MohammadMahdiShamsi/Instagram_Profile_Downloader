import tkinter as tk
from tkinter import messagebox
import instaloader
import urllib
from urllib.request import urlopen
from PIL import Image, ImageTk
import io


class InstagramProfileDownloader:
    def __init__(self):
        # Window
        self.window = tk.Tk()
        self.window.title("Instagram Profile Downloader")
        self.window.geometry("700x700")

        # Widgets
        self.create_widgets()

        self.window.mainloop()

    def create_widgets(self):
        # Label
        self.title_label = tk.Label(
            self.window,
            text="Enter Instagram Username",
            font=("Arial", 14)
        )
        self.title_label.pack(pady=10)

        # Entry
        self.username_entry = tk.Entry(self.window, width=40, font=("Arial", 12))
        self.username_entry.pack(pady=10)

        # Button
        self.download_button = tk.Button(
            self.window,
            text="Download Profile Image",
            command=self.get_profile_image
        )
        self.download_button.pack(pady=10)

        # Image Label
        self.image_label = tk.Label(self.window)
        self.image_label.pack(pady=20)

    def get_profile_image(self):
        username = self.username_entry.get().strip()

        if not username:
            messagebox.showwarning("Warning", "Please enter a username")
            return

        try:
            image_data = self.download_image(username)
            self.show_image(image_data)

        except Exception:
            messagebox.showerror(
                "Error",
                "Username not found or internet problem"
            )

    def download_image(self, username):
        loader = instaloader.Instaloader()
        profile = instaloader.Profile.from_username(
            loader.context, username
        )

        with urlopen(profile.get_profile_pic_url()) as response:
            return response.read()

    def show_image(self, image_data):
        image = Image.open(io.BytesIO(image_data))
        image = image.resize((300, 300))

        photo = ImageTk.PhotoImage(image)
        self.image_label.config(image=photo)
        self.image_label.image = photo  # prevent garbage collection


if __name__ == "__main__":
    InstagramProfileDownloader()

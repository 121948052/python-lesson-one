
import tkinter as tk
from PIL import Image, ImageTk

class ImageViewer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Image Viewer")

        # 创建一个标签用于显示图片
        self.image_label = tk.Label(self.root)
        self.image_label.pack()

        # 加载默认图片
        self.load_image("images/default.png")

    def load_image(self, image_path):
        try:
            image = Image.open(image_path)
            photo = ImageTk.PhotoImage(image)
            self.image_label.config(image=photo)
            self.image_label.image = photo
        except Exception as e:
            print(f"Error loading image: {e}")

if __name__ == '__main__':
    viewer = ImageViewer()
    viewer.root.mainloop()
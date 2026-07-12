from tkinter import *
import os
from PIL import ImageTk , Image

class ImageDownloader:
    def __init__(self):
        self.download_count=1
        self.current_index=0
        self.images_list = []
        self.load_gui()
        self.load_images()
        self.display_image()
        self.load_buttons()
        self.root.mainloop()

    def load_gui(self):
        self.root=Tk()
        self.root.title("Image Downloader")
        self.root.configure(background="black")
        self.root.geometry("350x400")
        self.root.maxsize(350,400)
        self.root.minsize(350,400)
        self.img_label = Label(self.root, bg="black")
        self.img_label.pack(pady=2)

    def load_images(self):
        for image in os.listdir("photos"):
            img_path = os.path.join("photos", image)
            if os.path.isfile(img_path):
                self.images_list.append(img_path)
    
    def display_image(self):
        image_path= self.images_list[self.current_index]
        image=Image.open(image_path)
        resized_image=image.resize((300,280))
        photo=ImageTk.PhotoImage(image=resized_image)
        self.img_label.config(image=photo)
        self.img_label.image=photo



    def load_buttons(self):
        frame=Frame(self.root,bg="black")
        frame.pack(expand=True, fill=BOTH,pady=3)
        prev=Button(frame,text="<=Prev",background="white",height=3,width=15,command=self.prev_btn)
        prev.pack(side=LEFT)
        download=Button(frame,text="Download Image",background="white",height=3,width=15,command=self.download_btn)
        download.pack(side=LEFT)
        next=Button(frame,text="Next=>",background="white",height=3,width=15,command=self.next_btn)
        next.pack(side=LEFT)


    def next_btn(self):
        if self.current_index == len(self.images_list) -1:
            self.current_index=0
        else:
            self.current_index +=1
        self.display_image()

    def prev_btn(self):
        if self.current_index == 0:
            self.current_index=len(self.images_list)-1
        else:
            self.current_index -=1
        self.display_image()

    def download_btn(self):
        
        with open(self.images_list[self.current_index],"rb") as f:
            content = f.read()

        with open(f"download{self.download_count}.jpg", "wb") as f:
            f.write(content)

        self.download_count += 1
        success= Label(self.root,text="Image Downloaded!",background="black", font=("verdana",8),fg="white")
        success.pack(pady=3)


obj=ImageDownloader()
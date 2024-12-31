import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk
import os,cv2,sys
from PIL import Image, ImageTk

        
class WebcamGUI:
    def __init__(self, root, active_filter=None):
        self.root = root
        self.root.title("✨ Magical Face Filters ✨")
        
        
        self.filters_path = {
            'glasses': os.path.join(os.getcwd(), 'images', 'glasses.png'),
            'hat': os.path.join(os.getcwd(), 'images', 'hat.png'),
            'animal': os.path.join(os.getcwd(), 'images', 'animal.png')
        }

        
        from main import FilterApplication
        
        self.filter_app = FilterApplication(self.filters_path)
        self.active_filter = active_filter
        self.running = True
        self.setup_gui()
        
        
        self.cap = cv2.VideoCapture(0)
        
        
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.update_frame()
        

    def setup_gui(self):
        
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        
        header = ttk.Label(
            main_frame,
            text=f"Active Filter: {self.active_filter.capitalize() if self.active_filter else 'None'}",
            font=('Helvetica', 16),foreground='#FFFF00'
        )

        header.pack(pady=5)

        
        video_frame = ttk.Frame(main_frame)
        video_frame.pack(padx=10, pady=10)
        
        self.video_label = ttk.Label(video_frame)
        self.video_label.pack()

        
        self.status_label = ttk.Label(
            main_frame,
            text="Waiting for face detection...",
            font=('Helvetica', 10),
            foreground='#FFFF00'
        )

        self.status_label.pack(pady=10)

    def update_frame(self):
        if not self.running:
            return

        ret, frame = self.cap.read()
        if ret:
            frame = cv2.flip(frame, 1)
            
            if self.active_filter:
                frame = self.filter_app.process_frame(frame, self.active_filter)
               
                self.status_label.configure(
                    text="Face detected! 😍" if self.filter_app.face_detected else "No face detected 🔍"
                )
            
            
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = cv2.resize(frame, (600, 400))
            img = Image.fromarray(frame)
            imgtk = ImageTk.PhotoImage(image=img)
            
            self.video_label.imgtk = imgtk
            self.video_label.configure(image=imgtk)
        
        if self.running:
            self.root.after(10, self.update_frame)



    def on_closing(self):
        self.cleanup()
        self.root.destroy()
        sys.exit(0)

    def cleanup(self):
        self.running = False
        if hasattr(self, 'cap'):
            self.cap.release()
        self.filter_app.cleanup()

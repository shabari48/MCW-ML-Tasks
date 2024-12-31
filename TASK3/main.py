import argparse
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

from filter import FilterOverlay, ImageProcessor
from gui import WebcamGUI
from sound import SoundPlayer
from face import FaceDetector


class FilterApplication:
    def __init__(self, filters_config):
        self.detector = FaceDetector()
        self.filters = {}
        self.sound_player = SoundPlayer()
        self.load_filters(filters_config)
        self.face_detected = False


    def load_filters(self, filters_config):
        for filter_name, filter_path in filters_config.items():
            try:
                self.filters[filter_name] = FilterOverlay(filter_path)
            except Exception as e:
                print(f"Error loading {filter_name} filter: {e}")


    def process_frame(self, frame, active_filter):
        frame = ImageProcessor.apply_smoothing(frame)
        faces = self.detector.detect_faces(frame)
        
        self.face_detected = len(faces) > 0

        if self.face_detected:
            self.sound_player.play_sound(active_filter)
            
        for (x, y, w, h) in faces:

            if active_filter == 'glasses':
                eyes = self.detector.detect_eyes(frame, x, y, w, h)
                if len(eyes) >= 2:
                    y = y + eyes[0][1] - int(h * 0.2)
                    self.filters['glasses'].apply(frame, x, y, w, int(h * 0.7))

            elif active_filter == 'hat':
                hat_width = int(w * 1.2)
                hat_height = int(h * 1.0)
                hat_x = x - int(w * 0.45)
                hat_y = y - int(h * 1.0)
                self.filters['hat'].apply(frame, hat_x, hat_y, hat_width, hat_height,scale_x=1.5,scale_y=1.5)

            elif active_filter == 'animal':
               
                x = x - int(w * 0.08)  
                self.filters['animal'].apply(frame, x, y, w, h)

        return frame

    def cleanup(self):
        self.sound_player.cleanup()


def main():
    parser = argparse.ArgumentParser(description='Apply filters to webcam feed')
    parser.add_argument('-g', '--glasses', action='store_true', help='Apply glasses filter')
    parser.add_argument('-t', '--hat', action='store_true', help='Apply hat filter')
    parser.add_argument('-a', '--animal', action='store_true', help='Apply animal filter')
    args = parser.parse_args()

    active_filter = None
    if args.glasses:
        active_filter = 'glasses'
    elif args.hat:
        active_filter = 'hat'
    elif args.animal:
        active_filter = 'animal'

    root = ttk.Window(themename="darkly")
    app = WebcamGUI(root, active_filter)
    root.mainloop()

if __name__ == "__main__":
    main()
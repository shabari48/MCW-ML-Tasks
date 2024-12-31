import pygame.mixer
from threading import Timer
import os

class SoundPlayer:
    def __init__(self):
        pygame.mixer.init()
        self.sounds = {
            'glasses': os.path.join(os.getcwd(), 'sounds', 'glass.mp3'),
            'hat': os.path.join(os.getcwd(), 'sounds', 'hat.mp3'),
            'animal': os.path.join(os.getcwd(), 'sounds', 'dog.mp3')
        }
        self.last_play = None
        self.sound_timer = None

    def play_sound(self, filter_name):
        if filter_name in self.sounds and self.last_play != filter_name:
            try:
                pygame.mixer.music.load(self.sounds[filter_name])
                pygame.mixer.music.play()
                self.last_play = filter_name
                if self.sound_timer:
                    self.sound_timer.cancel()
                self.sound_timer = Timer(20.0, self.reset_last_play)
                self.sound_timer.start()
            except Exception as e:
                print(f"Error playing sound for {filter_name}: {e}")

    def reset_last_play(self):
        self.last_play = None

    def cleanup(self):
        if self.sound_timer:
            self.sound_timer.cancel()
        pygame.mixer.quit()
import kivy
import random

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.core.audio import SoundLoader

class CatMeowApp(App):
    sound = SoundLoader.load('cat_meow_x.wav')
    img_still = Image(source='output-onlineimagetools.png', allow_stretch=True)
    img_playing = Image(source='meow.gif', allow_stretch=True)
    LengthGifInSeconds = 2
    layout = BoxLayout(padding=10, orientation='vertical')
    playing = False
    
    def build(self):
        btn = Button(text = "Meow?")
        btn.bind(on_press=self.button_pressed)

        if (self.playing):
            self.layout.add_widget(self.img_playing)
            Clock.schedule_once(self.set_still_layout, self.LengthGifInSeconds)
        else:
            self.layout.add_widget(self.img_still)
        self.layout.add_widget(btn)

        return self.layout

    def button_pressed(self, instance):
        if (not self.playing):
            self.set_layout(True)
            self.sound.play()

    def set_layout(self, playing):
        self.layout.clear_widgets()
        self.playing = playing
        self.build()

    def set_still_layout(self, dt) :
        self.set_layout(False)

if __name__ == "__main__":
    app = CatMeowApp()
    app.run()
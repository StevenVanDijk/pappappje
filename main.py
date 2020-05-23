import kivy
import random

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image

red = [1,0,0,1]
green = [0,1,0,1]
blue =  [0,0,1,1]
purple = [1,0,1,1]

class HBoxLayoutExample(App):
    def build(self):
        rootLayout = BoxLayout()
        layout = BoxLayout(padding=10, orientation='vertical')
        colors = [red, green, blue, purple]

        for i in range(5):
            btn = Button(text=f"Button #{i+1}",
                         background_color=random.choice(colors)
                         )
            layout.add_widget(btn)
        
        rootLayout.add_widget(layout)
        rootLayout.add_widget(Image(source='ramiz-dedakovic-jerh2Nj1XWY-unsplash.jpg'))    
        
        return rootLayout

if __name__ == "__main__":
    app = HBoxLayoutExample()
    app.run()
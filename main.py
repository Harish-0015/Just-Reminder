import kivy
from kivy.app import App  # create app
from kivy.uix.label import Label
from kivy.core.window import Window

Window.clearcolor=(1,0,0,1)      #last 1 stands for transperance or opacity
                 # R G B
class ImageClassifierApp(App):
    def build(self):  # build app
        label = Label(text='This is Sharpova.',font_size='20sp',bold=True,
                      color=(0,0,1,1),
                      italic =True)  # label is variable
        return label
ImageClassifierApp().run()

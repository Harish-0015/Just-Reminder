from kivy.app import App
from kivy.uix.button import Button


class ImageClassifier(App):
    def build(self):
        button = Button(text='print this', size_hint=(0.2, 0.2),font_size='20sp',          #size_hint will be in tuple
                        pos_hint={'center_x':0.5,'center_y':0.5},
                        on_press=self.printpress,
                        on_release=self.printrelease)

        return button
    def printpress(self,obj):
        print("Button has be pressed")
    def printrelease(self,obj):
        print("Button has been released")

ImageClassifier().run()

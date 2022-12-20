from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout  # this is imppported because we can't return multiple values at a time
from kivy.core.window import Window

Window.clearcolor = (1, 1, 1, 1)
Window.size = (360, 600)


class ImageClassifier(App):
    def build(self):
        """"
         Layout=BoxLayout(orientation='vertical',spacing=10,padding=40)    #by default it will be horizontal
         btn=Button(text="Button1")                                            #spacing is for space between buttons
         btn2=Button(text="Button2")                                           #passing is for space between window and buttons
         btn3= Button(text="Button3")
         Layout.add_widget(btn)
         Layout.add_widget(btn2)
         Layout.add_widget(btn3)
         return Layout
         """
        layout = BoxLayout(orientation='vertical', spacing=100, padding=40)
        img = Image(
            source="data:image/jpeg;base64,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")
        button = Button(text='Login', size_hint=(None, None), width=100, height=50
                        , pos_hint={'center_x': 0.5})
        layout.add_widget(img)
        layout.add_widget(button)
        return layout


ImageClassifier().run()

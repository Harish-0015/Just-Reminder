from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRectangleFlatButton

class Demo(MDApp):
    def build(self):      #self refers to the mobile application we are building
        self.theme_cls.primary_palette='Yellow'  #color of word
        self.theme_cls.primary_hue='A700'   #Darkness of word
        self.theme_cls.theme_style="Dark"   #by default theme is Light

        screen=MDScreen()
        btn_flat=MDRectangleFlatButton(text='Hello Ajay',pos_hint={'center_x':0.5,'center_y':0.5})
        screen.add_widget(btn_flat)
        return screen

Demo().run()
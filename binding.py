from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.lang import Builder
from UserTextMD import username_helper
from kivymd.uix.button import MDRectangleFlatButton

class Demo(MDApp):
    def build(self):
        screen=Screen()
        self.theme_cls.primary_palette="Green"
        btn=MDRectangleFlatButton(text="Show",
                                  pos_hint={'center_x': 0.5,'center_y': 0.4},
                                  on_release=self.show_data)
        self.username = Builder.load_string(username_helper)
        screen.add_widget(self.username)
        screen.add_widget(btn)
        return screen
    def show_data(self,obj):
        print(self.username.text)
Demo().run()
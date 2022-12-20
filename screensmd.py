from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFlatButton,MDRectangleFlatButton,MDIconButton,MDFloatingActionButton


class Demo(MDApp):

    def build(self):
        screen = Screen()
        btn_flat = MDRectangleFlatButton(text='Hello Ajay',
                                pos_hint={'center_x': 0.5, 'center_y': 0.5})
        icon_btn=MDIconButton(icon='language-python',pos_hint={'center_x': 0.5, 'center_y': 0.5})
        icon_btn =MDFloatingActionButton(icon='language-python', pos_hint={'center_x': 0.5, 'center_y': 0.5})
        #screen.add_widget(btn_flat)
        screen.add_widget(icon_btn)       #Screen in kivyMD is same as Layout in kivy
        return screen


Demo().run()

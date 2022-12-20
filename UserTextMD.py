from kivymd.app import MDApp
from kivymd.uix.screen import Screen
#from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder

username_helper = """
MDTextField:
    hint_text:"Enter username"
    helper_text: "Click on forgot password"
    helper_text_mode: "persistent"  #by default it will be in on_focus
    icon_right:"language-python"
    pos_hint:{'center_x':0.5,'center_y':0.5}
    size_hint_x:None
    width:300    
"""
class Demo(MDApp):
    def build(self):
        screen=Screen()
        self.theme_cls.primary_palette="Green"
        '''username=MDTextField(text='Enter username',
                             pos_hint={'center_x':0.5, 'center_y':0.5},
                             size_hint_x=None,
                             width=300)
                             '''
        username=Builder.load_string(username_helper)
        screen.add_widget(username)
        return screen

Demo().run()
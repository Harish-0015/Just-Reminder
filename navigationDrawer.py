from kivymd.app import MDApp
from kivymd.theming import ThemeManager

class Demo(MDApp):
    theme_cls=ThemeManager()
    def build(self):
        s
NavigationLayout:
    NavigationDrawer:
        NavigationDrawerIconButton:
            text:"Screen1"
            on_release:
                screen_manager.current="screen1"
        NavigationDrawerIconButton:
            text:"Screen 2"
            on_release:
                screen_manager.current
    ScreenManager:
        id : screen_manager
        Screen:
            name:"screen1"
            MDLabel:
                text:"Screen1"
        Screen:
            name:"screen2"
            MDLabel:
                text: "Screen2"
Demo().run()
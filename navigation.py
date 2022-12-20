from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

Window.size=(3000,500)

navigation_helper="""
Screen:
    NavigationLayout:
        ScreenManager:
            Screen: 
                BoxLayout:
                    orientation: 'vertical'
                    MDTopAppBar:
                        title: 'Just-Remainder'
                        left_action_items: [["menu",lambda x:app.nav_drawer.toggle_nav_drawer()]]
                        #right_action_items: [["dots-vertical",lambda x: app.navigation_draw()]]
                        elevation:8
                        Widget:
        MDNavigationDrawer:
            id:nav_drawer   
    
"""
class Demo(MDApp):
    def build(self):
        screen=Builder.load_string(navigation_helper)
        return screen
    def navigation_draw(self):
        print("Navigation")

Demo().run()
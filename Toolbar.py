from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window  # automatically resized to mobile size
from kivymd.uix.snackbar import Snackbar   #for adding tooltips to the toolbar icons by adding a text string to the toolbar item

Window.size = (300, 500)  # make sure not to use this while creating application
screen_helper = """
Screen:
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:    #only MDTopAppBar or MDBottomAppBar will be used in latest version
            title: 'Just-Remainder' 
            left_action_items: [["menu",lambda x:app.navigation_draw(),"show content in our app"]]
            #right_action_items: [["clock",lambda x:app.navigation_draw()]]
            right_action_items: [["dots-vertical",lambda x:app.navigation_draw(),"More Actions"]]   #this is for more actions

            elevation:8
        MDLabel:
            text: 'Time is precious so manage it with our application.'
            halign : 'center' 
            
        MDBottomAppBar:
            MDTopAppBar:    #only MDTopAppBar or MDBottomAppBar will be used in latest version
                title: 'Help'
                icon:"git"
                icon_color:0,1,0,1
                type:"bottom"
                mode:"free-end" 
                left_action_items: [["Coffee",lambda x:app.navigation_draw()]]
"""


class Demo(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Cyan"
        screen = Builder.load_string(screen_helper)
        return screen

    def navigation_draw(self):
        print("Navigation")


Demo().run()

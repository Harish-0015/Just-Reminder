from kivymd.app import MDApp
from kivymd.uix.screen import Screen
#from kivymd.uix.list import MDList,ThreeLineIconListItem,ThreeLineListItem
from kivymd.uix.list import MDList,ThreeLineAvatarListItem,ThreeLineListItem
from kivymd.uix.list import IconLeftWidget,ImageLeftWidget
from kivy.uix.scrollview import ScrollView

class Demo(MDApp):
    def build(self):
        screen=Screen()
        scroll=ScrollView()
        list_view=MDList()
        scroll.add_widget(list_view)

        for i in range(20):
            #icon=IconLeftWidget(icon="language-python")
            image = ImageLeftWidget(source="https://png.pngtree.com/png-clipart/20180515/ourmid/pngtree-facebook-logo-facebook-icon-png-image_3566127.png")
            items = ThreeLineAvatarListItem(text="Item"+str(i),secondary_text="Hello",tertiary_text="World")
            items.add_widget(image)
            list_view.add_widget(items)

        screen.add_widget(scroll)
        return screen

Demo().run()
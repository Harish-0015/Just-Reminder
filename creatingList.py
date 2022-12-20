from kivymd.app import MDApp
from kivymd.uix.screen import Screen
#from kivymd.uix.list import MDList, OneLineListItem
#from kivymd.uix.list import MDList,TwoLineListItem
from kivymd.uix.list import MDList,ThreeLineListItem
from kivy.uix.scrollview import ScrollView


class Demo(MDApp):
    def build(self):
        screen = Screen()
        list_view = MDList()
        scroll = ScrollView()
        scroll.add_widget(list_view)

        for i in range(20):
            #items = OneLineListItem(text="Item"+str(i))
            #items= TwoLineListItem(text="Item"+str(i),secondary_text="Hello")
            items = ThreeLineListItem(text="Item" + str(i), secondary_text="Hello",tertiary_text="World")
            list_view.add_widget(items)
        screen.add_widget(scroll)
        return screen


Demo().run()

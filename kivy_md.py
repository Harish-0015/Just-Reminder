from kivymd.app import MDApp
from kivymd.uix.label import MDLabel,MDIcon

class Demo(MDApp):
    def build(self):
        #label = MDLabel(text='Ajay', halign='center', theme_text_color='Primary')
        #label = MDLabel(text='Ajay', halign='center', theme_text_color='Secondary')
        #label = MDLabel(text='Ajay', halign='center', theme_text_color='Hint')
        #label = MDLabel(text='Ajay', halign='center', theme_text_color='Error')
        '''
        label = MDLabel(text='Ajay', halign='center', theme_text_color='Custom',
                        text_color=(236/255.0,98/255.0,81/255.0,1),
                        font_style='H2')
        '''
        icon_label= MDIcon(icon='language-python', po_hint={'center_x':0.5,'center_y':0.5})
        #return label
        return icon_label
Demo().run()

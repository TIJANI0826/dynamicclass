from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.behaviors import RectangularElevationBehavior
from kivymd.uix.menu import MDDropdownMenu
from kivy.properties import NumericProperty, ObjectProperty, StringProperty
from kivy.storage.jsonstore import JsonStore
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.spinner import Spinner
from kivy.uix.stacklayout import StackLayout
from kivy.uix.textinput import TextInput
from kivy.uix.accordion import Accordion, AccordionItem
# from kivymd.uix.accordion import MDAccordion, MDAccordionItem, MDAccordionSubItem
from kivymd.theming import ThemeManager
from kivymd.uix.list import MDList, OneLineListItem, \
    OneLineAvatarListItem, OneLineIconListItem, ThreeLineListItem, \
    TwoLineListItem
from kivymd.uix.button import MDIconButton
from kivymd.uix.list import ILeftBody, ILeftBodyTouch, IRightBodyTouch, BaseListItem
from kivymd.material_resources import DEVICE_TYPE
from kivymd.uix.navigationdrawer import MDNavigationDrawer, NavigationLayout
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.snackbar import Snackbar
from kivy.uix.image import Image
from kivymd import images_path
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelThreeLine
from kivymd.uix.label import MDLabel
from kivy.properties import BooleanProperty
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from readsubject import read_text

import datetime
from readsubject import read_text
class CustomToolbar(ThemableBehavior,RectangularElevationBehavior, BoxLayout):
    def __init__(self,**kwargs):
        super(CustomToolbar,self).__init__(**kwargs)
        self.md_bg_color = self.theme_cls.primary_color


class CreateSubject( GridLayout):
    def __init__(self, **kwargs):
        super(CreateSubject, self).__init__(**kwargs)
        self.cols = 1
        self.sub_text = TextInput(hint_text='Input Your Subject', write_tab=False)
        self.sub_button = Button(text='Create Subject', on_press=self.create_subject)
        self.sub_button2 = Button(text='Clear', on_press =self.clear)

        self.add_widget(self.sub_text)
        self.add_widget(self.sub_button)
        self.add_widget(self.sub_button2)

    def create_subject(self, instance):
        subject = self.sub_text.text.upper()
    
        subject_file = open('subject.txt', 'at')
        subject_file.write('\n' + subject)
        subject_file.close()
        sub_pop = Popup(title='Subject Creation', size_hint=(.5, .5), auto_dismiss=True)
        sub_pop_text = Label(text=self.sub_text.text)
        sub_pop.add_widget(sub_pop_text)
        sub_pop.open()
    def clear(self,instance):
        self.sub_text.text = ''

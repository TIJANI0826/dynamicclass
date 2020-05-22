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

import datetime
from readsubject import read_text
from createSubject import CreateSubject
from createQuestion import CreateQuestion
from viewQuestion import ViewQuestion

KV = '''
<CustomToolbar>:
    size_hint_y: None
    height: self.theme_cls.standard_increment
    padding:"5dp"
    spacing: "12dp"

    MDIconButton:
        id:icon_button
        icon:'menu'
        pos_hint:{"center_y":.5}
    MDLabel:
        text: "QUIZAPP"
        post_hint:{"center":.5}
        size_hint_x: None
        width:self.texture_size[0]
        text_size: None,None
        font_style:"H6"

<CreateSubject>:

<CreateQuestion>:

<ViewQuestion>:


BoxLayout:
    orientation: 'vertical'
    # CustomToolbar:
    #     id:toolbar
    MDBottomNavigation:
        MDBottomNavigationItem:
            name: 'screen 1'
            text: 'CREATE'
            icon:'home'            
            CreateSubject:
                id : create_subject
                name : 'create_subject'
        MDBottomNavigationItem:
            name: 'screen 2'
            text: 'QUESTION'
            icon:'box'
            CreateQuestion:
                id : create_question
                name : 'create_question'
        MDBottomNavigationItem:
            name: 'screen 3'
            text: 'VIEW'
            icon:'settings'
            ViewQuestion:
                id : view_question
                name : 'view_question'
'''






class ViewQuestion(Screen,BoxLayout):
    def __init__(self, **kwargs):
        super(ViewQuestion, self).__init__(**kwargs)
        subjects = read_text()
        self.data = [{'text': str(x)} for x in subjects]
        print(self.data)

class MainApp(MDApp):
        
    def build(self):
        self.screen = Builder.load_string(KV)
        return self.screen
MainApp().run()

from kivy.app import App
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
from kivy.core.window import Window

class TestApp(App):
    def build(self):

        # store = JsonStore('{}.json'.format(self.subject.text.strip('\n').upper()))
        store = JsonStore('MATHEMATICS.json')
        count = 1
        box = GridLayout(cols=1, spacing=10, size_hint_y=None)        
        box.bind(minimum_height=box.setter('height'))
        while count <= len(store):
            if store.exists(str(count)):
                for data in store.get(str(count)).values():
                    box.add_widget(Label(text = str(data),size_hint_y=None, height=40))
            count = count + 1
        root = ScrollView(size_hint=(1, None),size =(400,600))
        root.add_widget(box)
        return root
if __name__ == '__main__':
    TestApp().run()
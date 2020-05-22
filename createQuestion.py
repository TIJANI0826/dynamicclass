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
class CreateQuestion(Screen, GridLayout):
    def __init__(self, **kwargs):
        super(CreateQuestion, self).__init__(**kwargs)
        self.cols = 1

        subjects = read_text()
        self.subject = Spinner(
            text=subjects[0],
            values=tuple([x for x in subjects]),
            size_hint=(.1, 0.1))

        # The Question number and question itself inside a boxlayout
        ques_box_layout = GridLayout(cols=2, rows=6)
        self.question_no = TextInput(hint_text='put the question no', input_filter='int', write_tab=False)
        self.question = TextInput(hint_text='put the question here e.g What is this', write_tab=False)

        # self.add_widget(ques_box_layout)

        # The options inside a box layout
        # option_box_layout = GridLayout(cols=4, rows=1)
        self.option1 = TextInput(hint_text='put your options here e.g A. A boy', write_tab=False)
        self.option2 = TextInput(hint_text='put your options here e.g B. A girl', write_tab=False)
        self.option3 = TextInput(hint_text='put your options here e.g C. A boygirl', write_tab=False)
        self.option4 = TextInput(hint_text='put your options here e.g D. A girlboy', write_tab=False)

        # self.add_widget(ques_box_layout)

        # the answer
        # answ_buton_layout = GridLayout(cols = 2, rows = 1)
        self.answer = TextInput(hint_text='put the answer e.g A or B or C or D', write_tab=False)

        # The question button to create the question
        self.quest_button = Button(text='Create Question')

        ques_box_layout.add_widget(self.subject)
        ques_box_layout.add_widget(self.question_no)
        ques_box_layout.add_widget(self.question)

        ques_box_layout.add_widget(self.option1)
        ques_box_layout.add_widget(self.option2)
        ques_box_layout.add_widget(self.option3)
        ques_box_layout.add_widget(self.option4)
        ques_box_layout.add_widget(self.answer)

        ques_box_layout.add_widget(self.quest_button)

        self.add_widget(ques_box_layout)
        self.quest_button.bind(on_press=self.save_question)

    def save_question(self, instance):
        store = JsonStore('{}.json'.format(self.subject.text.strip('\n').upper()))
        store.put(self.question_no.text,
                  question=self.question.text,
                  option1=self.option1.text,
                  option2=self.option2.text,
                  option3=self.option3.text,
                  option4=self.option4.text,
                  answer=self.answer.text)
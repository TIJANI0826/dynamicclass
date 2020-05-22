from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

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

import datetime




KV = '''
<ContentNavigationDrawer>:
    orientation: "vertical"
    padding: "8dp"
    spacing: "8dp"

    AnchorLayout:
        anchor_x: "left"
        size_hint_y: None
        height: avatar.height

        Image:
            id: avatar
            size_hint: None, None
            size: "56dp", "56dp"
            source: "kivymd_logo.png"
    MDLabel:
        text: "KivyMD library"
        font_style: "Button"
        size_hint_y: None
        height: self.texture_size[1]

    MDLabel:
        text: "kivydevelopment@gmail.com"
        font_style: "Caption"
        size_hint_y: None
        height: self.texture_size[1]


    ScrollView:

        MDList:

            OneLineListItem:
                text: "ADD A SUBJECT"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "create_subject"

            OneLineListItem:
                text: "QUESTION"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "create_question"
            OneLineListItem:
                text: "VIEW QUESTION"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "view_question"

<CreateSubject>:

<CreateQuestion>:

<ViewQuestion>:


Screen:
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            id: toolbar
            pos_hint: {"top": 1}
            elevation: 10
            title: "MDNavigationDrawer"
                    
    
    NavigationLayout:
        x:toolbar.height
                
        ScreenManager:
            id: screen_manager
                        



            CreateSubject:
                id : create_subject
                name : 'create_subject'
            CreateQuestion:
                id : create_question
                name : 'create_question'
            ViewQuestion:
                id : view_question
                name : 'view_question'

        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                screen_manager: screen_manager
                nav_drawer: nav_drawer

'''

list_of_subject = []


class MySceens(ScreenManager):
    def __init__(self, **kwargs):
        super(MySceens, self).__init__(**kwargs)


class MyScreen(Screen, GridLayout):
    def __init__(self, **kwargs):
        super(MyScreen, self).__init__(**kwargs)
        self.cols = 2


class MainAppScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(MainAppScreen, self).__init__(**kwargs)
        self.screen_manager = ObjectProperty(None)
        self.createSub = ObjectProperty(None)
        self.sub = ObjectProperty(None)

class CreateSubject(Screen, BoxLayout):
    def __init__(self, **kwargs):
        super(CreateSubject, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.sub_text = TextInput(hint_text='Input Your Subject', write_tab=False)
        sub_button = Button(text='Create Subject', size_hint=(.2, .1), on_press=self.create_subject)
        self.add_widget(self.sub_text)
        self.add_widget(sub_button)

    def create_subject(self, instance):
        subject = self.sub_text.text.upper()
        list_of_subject.append(subject)
        subject_file = open('subject.txt', 'at')
        subject_file.write(subject + '\n')
        subject_file.close()
        sub_pop = Popup(title='Subject Creation', size_hint=(.5, .5), auto_dismiss=True)
        sub_pop_text = Label(text=self.sub_text.text)
        sub_pop.add_widget(sub_pop_text)
        return sub_pop.open()


class CreateQuestion(Screen, GridLayout):
    def __init__(self, **kwargs):
        super(CreateQuestion, self).__init__(**kwargs)
        self.cols = 1

        with open('subject.txt', 'rt') as f:
            for n in f.readlines():
                list_of_subject.append(n)
        self.subject = Spinner(
            text=list_of_subject[0],
            values=tuple([x for x in list_of_subject]),
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


class ViewQuestion(Screen, BoxLayout):
    def __init__(self, **kwargs):
        super(ViewQuestion, self).__init__(**kwargs)
        self.accordion = Accordion(orientation='vertical')
        self.get_question()

    def get_question(self):
        list_for_accord = []
        list_for_sub_item = []

        for i in list_of_subject:
            store = JsonStore('{}.json'.format(i.strip('').upper()))
            list_for_accord.append(i)
            accord_item = AccordionItem(title=i, orientation='horizontal')
            for key in store.keys():
                p = Popup(title=key, size_hint=(.5, .5), auto_dismiss=True)
                accord_sub_item = OneLineListItem(text=str(key))
                accord_sub_item.bind(on_press=p.open)
                accord_item.add_widget(accord_sub_item)

                grid = GridLayout(cols=1)
                l1 = Button(text=store[key]['question'])
                l2 = Button(text=store[key]['option1'])
                l3 = Button(text=store[key]['option2'])
                l4 = Button(text=store[key]['option3'])
                l5 = Button(text=store[key]['option4'])
                l7 = TextInput(text='')
                l6 = Button(text='see answer')
                l6.bind(on_release=lambda x: setattr(l7, 'text', store[p.title]['answer']))

                grid.add_widget(l1)
                grid.add_widget(l2)
                grid.add_widget(l3)
                grid.add_widget(l4)
                grid.add_widget(l5)
                grid.add_widget(l6)
                grid.add_widget(l7)

                p.add_widget(grid)
            self.accordion.add_widget(accord_item)
        self.add_widget(self.accordion)


class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()


class DrawerList(ThemableBehavior, MDList):
    def set_color_item(self, instance_item):
        """Called when tap on a menu item."""

        # Set the color of the icon and text for the menu item.
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color

class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class MainApp(MDApp):

    def build(self):
        return Builder.load_string(KV)


MainApp().run()

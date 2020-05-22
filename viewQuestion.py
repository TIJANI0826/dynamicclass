from kivy.app import App
from kivy.lang import Builder
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.label import Label
from kivy.properties import BooleanProperty
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.popup import Popup
from kivy.storage.jsonstore import JsonStore
from readsubject import read_text
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.uix.button import Button
from kivymd.uix.button import MDFlatButton
from kivy.uix.accordion import Accordion, AccordionItem
from kivy.uix.carousel import Carousel
from kivy.uix.image import AsyncImage
from kivy.uix.rst import RstDocument

Builder.load_string('''
<SelectableLabel>:
    # Draw a background to indicate selection
    canvas.before:
        Color:
            rgba: (.0, 0.9, .1, .3) if self.selected else (0, 0, 0, 1)
        Rectangle:
            pos: self.pos
            size: self.size
<ViewQuestion>:
    viewclass: 'SelectableLabel'
    SelectableRecycleBoxLayout:
        default_size: None, dp(56)
        default_size_hint: 1, None
        size_hint_y: None
        height: self.minimum_height
        orientation: 'vertical'
        multiselect: True
        touch_multiselect: True
''')
class SelectableRecycleBoxLayout(FocusBehavior, LayoutSelectionBehavior,
RecycleBoxLayout):
    ''' Adds selection and focus behaviour to the view. '''
class SelectableLabel(RecycleDataViewBehavior, Label):
    ''' Add selection support to the Label '''
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)
    def refresh_view_attrs(self, rv, index, data):
        ''' Catch and handle the view changes '''
        self.index = index
        return super(SelectableLabel, self).refresh_view_attrs(rv, index, data)
    def on_touch_down(self, touch):
        ''' Add selection on touch down '''
        if super(SelectableLabel, self).on_touch_down(touch):
            return True
        if self.collide_point( *touch.pos) and self.selectable:
            return self.parent.select_with_touch(self.index, touch)
    def apply_selection(self, rv, index, is_selected):
        ''' Respond to the selection of items in the view. '''
        self.selected = is_selected

        if is_selected:
            store = JsonStore('{}.json'.format(rv.data[index]['text'].strip('\n')))
            ques_box = RelativeLayout()
            count = 1
            count = 1
            box = GridLayout(cols=1, spacing=10, size_hint_y=None)        
            box.bind(minimum_height=box.setter('height'))
            while count <= len(store):
                if store.exists(str(count)):
                    for data in store.get(str(count)).values():
                        box.add_widget(Label(text = str(data),size_hint_y=None, height=40))
                count = count + 1
            root = ScrollView()
            root.add_widget(box)
            Popup(title="{}".format(rv.data[index]['text'].strip('\n')), content= root,size_hint=(.5,1),auto_dismiss=True).open()

class ViewQuestion(RecycleView):
    def __init__ (self, **kwargs):
        super(ViewQuestion, self).__init__ ( **kwargs)
        subjects = read_text()
        self.data = [{'text': str(x)} for x in subjects]
class TestApp(App):
    def build(self):
        return ViewQuestion()
if __name__ == '__main__':
    TestApp().run()
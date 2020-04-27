from math import sqrt
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder


class for_quadratic(FloatLayout):
    def solve_solution(self):
        self.result_box = self.ids.result_label
        self.value_a = self.ids.value_one.text
        self.value_b = self.ids.value_two.text
        self.value_c = self.ids.value_three.text

        if (self.value_a == ""):
            self.value_a = "1"
        if (self.value_b == ""):
            self.value_b = "1"
        if (self.value_c == ""):
            self.value_c = "1"

        self.a = int(self.value_a) ** 2
        self.b = int(self.value_b)
        self.c = int(self.value_c)

        self.g = self.b ** 2
        self.h = 4 * self.a * self.c
        self.I = abs(self.g - self.h)
        self.k = self.I
        self.formula = sqrt(self.k)
        self.root_one = (-self.b - self.formula) / 2 * self.a
        self.root_two = (-self.b + self.formula) / 2 * self.a
        self.result_box.text = ("the roots are \n {} and {}"
                                .format(round(self.root_one), round(self.root_two)))


class QuadraticApp(App):
    def build(self):
        return for_quadratic()

QuadraticApp().run()

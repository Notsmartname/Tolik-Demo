from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget


class WindowManager(ScreenManager):
    pass


class GlobalMain(Screen):
    pass


class BetonMain(Screen):
    pass


class KladkaMain(Screen):
    pass


# Расчет отделки помещений
class OtdelkaMain(Screen):
    pass


class PolMain(Screen):
    pass


class MyLayout(Widget):
    def spinner_clicked(self, value):
        self.ids.click_label.text = value


class TolicApp(App):
    pass


TolicApp().run()

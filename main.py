from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen


class WindowManager(ScreenManager):
    pass


class MainScreen(Screen):
    pass


class CvScreen(Screen):
    # Выводит переменные на экран
    def output_num(self):
        self.output_a.text = self.text_input_a.text
        self.output_b.text = self.text_input_b.text

    # Вычисляет квадратуру
    def col(self):
        a = int(self.output_a.text)
        b = int(self.output_b.text)

        self.summa.text = str(a * b)


class KvScreen(Screen):
    # Выводит Переменые на экран
    def output_num(self):

        try:
            self.output_x.text = self.text_input_x.text
            self.output_y.text = self.text_input_y.text
            self.output_h.text = self.text_input_h.text
        except:
            self.output_x.text = 0
            self.output_y.text = 0
            self.output_h.text = 0

    # Вычисляет Кубатуру
    def col(self):
        a = int(self.output_x.text)
        b = int(self.output_y.text)
        h = int(self.output_h.text)

        self.summa_k.text = str(a * b * h)


class TolicApp(App):
    pass


TolicApp().run()

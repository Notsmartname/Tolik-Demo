from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window


Window.size = (600, 400)


class FaceMain(BoxLayout):

    # Выводит переменные на экран
    def output_num(self):

        self.output_a.text = self.text_input_a.text
        self.output_b.text = self.text_input_b.text


    # Вычисляет квадратуру
    def col(self):
        a = int(self.output_a.text)
        b = int(self.output_b.text)

        self.summa.text = str(a * b)


class MainApp(App):
    pass


MainApp().run()

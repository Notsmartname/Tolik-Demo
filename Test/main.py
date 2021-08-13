from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

Window.size = (600, 400)



class FaceMain(BoxLayout):


    # Выводит ширину на экран
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


class MainApp(App):
    pass


MainApp().run()

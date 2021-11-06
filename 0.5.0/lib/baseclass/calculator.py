# Калькулятор
from kivy.uix.popup import Popup


class Calculator(Popup):
    # Очистиь строку
    def clear(self):
        self.ids.calc_input.text = '0'

    # Нажатие кнопки чифры
    def button_press(self, button):
        prior = self.ids.calc_input.text

        if prior == '0':
            self.ids.calc_input.text = ''
            self.ids.calc_input.text = f'{button}'
        else:
            self.ids.calc_input.text = f'{prior}{button}'

    # Кнопка удалить последний символ из текста
    def remove(self):
        prior = self.ids.calc_input.text
        prior = prior[:-1]
        self.ids.calc_input.text = prior

    # Кнопка против. знак
    def pos_neg(self):
        prior = self.ids.calc_input.text
        if '-' in prior:
            self.ids.calc_input.text = f'{prior.replace("-", "")}'
        else:
            self.ids.calc_input.text = f'-{prior}'

    # Кнопка точка
    def dot(self):
        prior = self.ids.calc_input.text

        # знак +
        num_list = prior.split('+')
        if '+' in prior and '.' not in num_list[-1]:
            prior = f'{prior}.'
            self.ids.calc_input.text = prior

        # знак -
        num_list = prior.split('-')
        if '-' in prior and '.' not in num_list[-1]:
            prior = f'{prior}.'
            self.ids.calc_input.text = prior

        # знак *
        num_list = prior.split('*')
        if '*' in prior and '.' not in num_list[-1]:
            prior = f'{prior}.'
            self.ids.calc_input.text = prior

        # знак /
        num_list = prior.split('/')
        if '/' in prior and '.' not in num_list[-1]:
            prior = f'{prior}.'
            self.ids.calc_input.text = prior

        elif '.' in prior:
            pass
        else:
            prior = f'{prior}.'
            self.ids.calc_input.text = prior

    # Кнопка плюс
    def math_sign(self, sign):
        prior = self.ids.calc_input.text

        self.ids.calc_input.text = f'{prior}{sign}'

    # Кнопка равно
    def equals(self):
        prior = self.ids.calc_input.text

        try:
            answer = eval(prior)
            num_list = str(answer)
            if num_list[-1] == '0' and num_list[-2] == '.':
                self.ids.calc_input.text = str(int(answer))
            else:
                self.ids.calc_input.text = str(answer)
        except:
            self.ids.calc_input.text = 'Error'

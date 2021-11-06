# Расчет меню бетона
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen
from kivymd.uix.boxlayout import MDBoxLayout


class BetonMain(MDBoxLayout):
    pass


# Ленточный фундамент
class OneBeton(Popup):
    def calculate_beton_1(self):

        cub_pr = self.ids.pr_cub_input.text
        a = self.ids.a_input.text
        b = self.ids.b_input.text
        c = self.ids.c_input.text
        h = self.ids.h_input.text
        
        if a != '':
            if b != '':
                if c != '':
                    if h != '':
                        if cub_pr != '':
                            beton = (int(a) + int(b)) * 2 * int(h) * int(c)
                            pr_beton = beton * cub_pr

                            self.ids.answer_beton.text = str(beton)
                            self.ids.answer_pr_beton.text = str(pr_beton)
                        else:
                            beton = (int(a) + int(b)) * 2 * int(h) * int(c)

                            self.ids.answer_beton.text = str(beton)
                            self.ids.answer_pr_beton.text = 'Введите цену за бетон'
                    else:
                        self.ids.answer_beton.text = 'Заполните поле со высщтой "H"'
                        self.ids.answer_pr_beton.text = 'Заполните все поля'
                else:
                    self.ids.answer_beton.text = 'Заполните поле с шириной "C"'
                    self.ids.answer_pr_beton.text = 'Заполните все поля'
            else:
                self.ids.answer_beton.text = 'Заполните поле со стороной "B"'
                self.ids.answer_pr_beton.text = 'Заполните все поля'
        else:
            self.ids.answer_beton.text = 'Заполните поле со стороной "A"'
            self.ids.answer_pr_beton.text = 'Заполните все поля'






class TwoBeton(Popup):
    def calculate_beton_2(self):
        cub_pr = self.ids.pr_cub_input.text
        a = self.ids.a_input.text
        b = self.ids.b_input.text
        c = self.ids.c_input.text
        h = self.ids.h_input.text
        d = self.ids.d_input.text

        
        if a != '':
            if b != '':
                if c != '':
                    if d != '':
                        if h != '':
                            if cub_pr != '':
                                beton = (int(a) + int(b)) * 2 * int(h) * \
                                        int(c) + (int(d) * int(h) * int(c))
                                pr_beton = beton * cub_pr
                                self.ids.answer_beton.text = str(beton)
                                self.ids.answer_pr_beton.text = str(pr_beton)        
                            else:
                                beton = (int(a) + int(b)) * 2 * int(h) * \
                                        int(c) + (int(d) * int(h) * int(c))

                                self.ids.answer_beton.text = str(beton)        
                                self.ids.answer_pr_beton.text = 'Введите цену за бетон'
                        else:
                            self.ids.answer_beton.text = 'Заполните поле со высотой'
                            self.ids.answer_pr_beton.text = 'Заполните все поля'
                    else:
                        self.ids.answer_beton.text = 'Заполните поле со стороной "D"'
                        self.ids.answer_pr_beton.text = 'Заполните все поля'
                else:
                    self.ids.answer_beton.text = 'Заполните поле с шириной "C"'
                    self.ids.answer_pr_beton.text = 'Заполните все поля'
            else:
                self.ids.answer_beton.text = 'Заполните поле со стороной "B"'
                self.ids.answer_pr_beton.text = 'Заполните все поля'
        else:
            self.ids.answer_beton.text = 'Заполните поле со стороной "A"'
            self.ids.answer_pr_beton.text = 'Заполните все поля'




class TreeBeton(Popup):
    def calculate_beton_3(self):
        cub_pr = self.ids.pr_cub_input.text
        a = self.ids.a_input.text
        b = self.ids.b_input.text
        c = self.ids.c_input.text
        h = self.ids.h_input.text
        d = self.ids.d_input.text
        f = self.ids.f_input.text

        if a != '':
            if b != '':
                if c != '':
                    if d != '':
                        if f != '':
                            if h != '':
                                if cub_pr != '':
                                    beton = (int(a) + int(b)) * 2 * int(h) * int(c) + \
                                        ((int(d) + int(f)) * int(h) * int(c))
                                    pr_beton = beton * cub_pr

                                    self.ids.answer_beton.text = str(beton)
                                    self.ids.answer_pr_beton.text = str(pr_beton)      
                                else:
                                    beton = (int(a) + int(b)) * 2 * int(h) * int(c) + \
                                        ((int(d) + int(f)) * int(h) * int(c))
                                            
                                    self.ids.answer_beton.text = str(beton)        
                                    self.ids.answer_pr_beton.text = 'Введите цену за бетон'
                            else:
                                self.ids.answer_beton.text = 'Заполните поле со высотой'
                                self.ids.answer_pr_beton.text = 'Заполните все поля'
                        else:
                            self.ids.answer_beton.text = 'Заполните поле со стороной "F"'
                            self.ids.answer_pr_beton.text = 'Заполните все поля'
                    else:
                        self.ids.answer_beton.text = 'Заполните поле со стороной "D"'
                        self.ids.answer_pr_beton.text = 'Заполните все поля'
                else:
                    self.ids.answer_beton.text = 'Заполните поле с шириной "C"'
                    self.ids.answer_pr_beton.text = 'Заполните все поля'
            else:
                self.ids.answer_beton.text = 'Заполните поле со стороной "B"'
                self.ids.answer_pr_beton.text = 'Заполните все поля'
        else:
            self.ids.answer_beton.text = 'Заполните поле со стороной "A"'
            self.ids.answer_pr_beton.text = 'Заполните все поля'


class FourBeton(Popup):
    def calculate_beton_4(self):
        cub_pr = self.ids.pr_cub_input.text
        a = self.ids.a_input.text
        b = self.ids.b_input.text
        c = self.ids.c_input.text
        h = self.ids.h_input.text
        d1 = self.ids.d2_input.text
        d2 = self.ids.d2_input.text
        f = self.ids.f_input.text

        if a != '':
            if b != '':
                if c != '':
                    if d1 != '' or d2 != '':
                        if f != '':
                            if h != '':
                                if cub_pr != '':
                                    beton = (int(a) + int(b)) * 2 * int(h) * int(c) + \
                                        ((int(d1) + int(f) + int(d2)) * int(h) * int(c))
                                    pr_beton = beton * cub_pr

                                    self.ids.answer_beton.text = str(beton)
                                    self.ids.answer_pr_beton.text = str(pr_beton)   
                                else:
                                    beton = (int(a) + int(b)) * 2 * int(h) * int(c) + \
                                        ((int(d1) + int(f) + int(d2)) * int(h) * int(c))
                                            
                                    self.ids.answer_beton.text = str(beton)        
                                    self.ids.answer_pr_beton.text = 'Введите цену за бетон'
                            else:
                                self.ids.answer_beton.text = 'Заполните поле со высотой'
                                self.ids.answer_pr_beton.text = 'Заполните все поля'
                        else:
                            self.ids.answer_beton.text = 'Заполните поле со стороной "F"'
                            self.ids.answer_pr_beton.text = 'Заполните все поля'

                    else:
                        self.ids.answer_beton.text = 'Заполните поле со стороной "D"'
                        self.ids.answer_pr_beton.text = 'Заполните все поля'
                else:
                    self.ids.answer_beton.text = 'Заполните поле с шириной "C"'
                    self.ids.answer_pr_beton.text = 'Заполните все поля'
            else:
                self.ids.answer_beton.text = 'Заполните поле со стороной "B"'
                self.ids.answer_pr_beton.text = 'Заполните все поля'
        else:
            self.ids.answer_beton.text = 'Заполните поле со стороной "A"'
            self.ids.answer_pr_beton.text = 'Заполните все поля'


# Колонна
class ColonaBeton(Screen):
    pass

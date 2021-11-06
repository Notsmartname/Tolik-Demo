from kivy.uix.popup import Popup
from kivymd.uix.screen import MDScreen
from math import ceil

from kivy.metrics import dp

# Расчет отделки помещений
class OtdelkaMain(MDScreen):
    pass


# Шпаклефка
class Shpaklefka(Popup):
    pass


# Покраска стен
class OtdelkaFirst(Popup):
    vid_kraski = None

    def spiner_clicked(self, value):
        if value == 'Силикатная':
            self.vid_kraski = 0.40
        if value == 'Латексная':
            self.vid_kraski = 0.60
        if value == 'Акриловая':
            self.vid_kraski = 0.25
        if value == 'Силиконовая':
            self.vid_kraski = 0.30
        if value == 'Поливинилацетатная':
            self.vid_kraski = 0.55

    def calculate_kraska(self):
        kraska = self.vid_kraski

        if self.kvadrat_input.text != '':
            kv = int(self.kvadrat_input.text)
            if self.pr_color_input.text != '':
                pr = int(self.pr_color_input.text)
            else:
                pr = 0
            self.answer_output.text = str(kv * kraska)
            self.answer_pr_color.text = str(kv * kraska * pr)
        else:
            if kraska is None:
                self.answer_output.text = 'Выберите вид краски'
            if self.answer_output.text == 'Выберите вид краски':
                self.answer_output.text = 'Введите квадратуру'
            else:
                self.answer_output.text = 'Введите квадратуру'


# Меню расчета обоев
class OtdelkaSecend(Popup):
    def calculate_oboi(self):
        if self.perimetr_input.text != '':
            pe = int(self.perimetr_input.text)
        else:
            pe = 0
        if self.shirina_input.text != '':
            shir = int(self.shirina_input.text)
        else:
            shir = 0
        if self.h_input.text != '':
            h = int(self.h_input.text)
        else:
            h = 0
        if self.pr_oboi_input.text != '':
            ob = int(self.pr_oboi_input.text)
        else:
            ob = 0

        mat = ceil(pe / shir * h)
        self.answer_output.text = str(mat)

        self.answer_pr_oboi.text = str(mat * ob)


# Меню расчета облицовки
class OtdelkaThird(Popup):
    def calculate_oblisovka(self):
        if self.dlina_input.text != '':
            dl = int(self.dlina_input.text)
        else:
            dl = 0
        if self.shirina_input.text != '':
            sh = int(self.shirina_input.text)
        else:
            sh = 0
        if self.shirina_kafel_input.text != '':
            sh_kaf = int(self.shirina_input.text)
        else:
            sh_kaf = 0
        if self.dlina_kafel_input.text != '':
            dl_kaf = int(self.dlina_kafel_input.text)
        else:
            dl_kaf = 0
        if self.shov_input.text != '':
            shov = int(self.shov_input.text)
        else:
            shov = 0
        if self.pr_kafel_input.text != '':
            pr_kaf = int(self.pr_kafel_input.text)
        else:
            pr_kaf = 0

        if shov == 0:
            kol_kaf = dl * sh / (sh_kaf * dl_kaf)
        else:
            # Определение количества кафеля и шва-м2 в высоту и длину стены
            dl_col_kaf = dl / dl_kaf * shov
            sh_col_kaf = sh / sh_kaf * shov
            kol_kaf = (dl * sh -(dl_col_kaf + sh_col_kaf)) / (sh_kaf * dl_kaf)

        mat = ceil(kol_kaf)
        self.answer_kafel.text = str(mat)
        self.answer_output.text = str(mat * pr_kaf)


# Меню расчета Штукатурка
class OtdelkaFourth(Popup):
    chek_norma = None
    def switch_smes(self, switchObject, switchValue):
        if (switchValue):
            print('гипс')
            self.chek_norma = 'гипс'
        else:
            print('цемент')
            self.chek_norma = 'цемент'

    norma = 1.7

    def calculate_shtukaturka(self):

        if self.chek_norma == 'цемент':
            self.norma = 1.7
            print(self.norma)
        if self.chek_norma == 'гипс':
            self.norma = 0.9
            print(self.norma)

        if self.kvadrat_input.text != '':
            kv = int(self.kvadrat_input.text)
        else:
            kv = 0
        if self.pr_smes_input.text != '':
            smes = int(self.pr_smes_input.text)
        else:
            smes = 0
        if self.tol_smes_input.text != '':
            tol = int(self.tol_smes_input.text)
        else:
            tol = 0

        mat = self.norma * tol * kv
        self.answer_smes.text = str(mat)
        self.answer_output.text = str(mat * smes)


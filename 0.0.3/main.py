from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp

from kivy.metrics import dp
from kivy.properties import StringProperty
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.list import OneLineIconListItem


Window.size = (340, 600)


class WindowManager(ScreenManager):
    pass


class GlobalMain(Screen):
    pass


# Расчет отделки помещений
class OtdelkaMain(Screen):
    pass

# Покраска стен
class OtdelkaFirst(Screen):
    def calculate_kraska(self):
        if self.kvadrat_input.text != '':
            kv = int(self.kvadrat_input.text)
        else:
            kv = 0
        if self.pr_shpak_input.text != '':
            sh = int(self.pr_shpak_input.text)
        else:
            sh = 0
        if self.pr_color_input.text != '':
            co = int(self.pr_color_input.text)
        else:
            co = 0
        if self.pr_gruntovka_input.text != '':
            gr = int(self.pr_gruntovka_input.text)
        else:
            gr = 0
        if self.pr_shkur_input.text != '':
            shk = int(self.pr_shkur_input.text)
        else:
            shk = 0
        if self.workmans_input.text != '':
            man = int(self.workmans_input.text)
        else:
            man = 0

        self.answer_output.text = str(kv + sh + co + gr + shk + man)


# Меню расчета обоев
class OtdelkaSecend(Screen):
    def calculate_oboi(self):
        if self.kvadrat_input.text != '':
            kv = int(self.kvadrat_input.text)
        else:
            kv = 0
        if self.shirina_input.tex != '':
            shir = int(self.shirina_input.text)
        else:
            shir = 0
        if self.pr_shpak_input.text != '':
            sh = int(self.pr_shpak_input.text)
        else:
            sh = 0
        if self.pr_oboi_input.text != '':
            ob = int(self.pr_oboi_input.text)
        else:
            ob = 0
        if self.pr_gruntovka_input.text != '':
            gr = int(self.pr_gruntovka_input.text)
        else:
            gr = 0
        if self.pr_shkur_input.text != '':
            shk = int(self.pr_shkur_input.text)
        else:
            shk = 0
        if self.workmans_input.text != '':
            man = int(self.workmans_input.text)
        else:
            man = 0

        self.answer_output.text = str(kv + shir + sh + ob + gr + shk + man)


# Меню расчета облицовки
class OtdelkaThird(Screen):
    def calculate_oblisovka(self):
        if self.kvadrat_input.text != '':
            kv = int(self.kvadrat_input.text)
        else:
            kv = 0
        if self.shirina_kafel_input.text != '':
            sh_kaf = int(self.shirina_kafel_input.text)
        else:
            sh_kaf = 0
        if self.dlina_kafel_input.text != '':
            dli_kaf = int(self.dlina_kafel_input.text)
        else:
            dli_kaf = 0
        if self.pr_gruntovka_input.text != '':
            gr = int(self.pr_gruntovka_input.text)
        else:
            gr = 0
        if self.pr_kafel_input.text != '':
            pr_kaf = int(self.pr_kafel_input.text)
        else:
            pr_kaf = 0
        if self.pr_kley_input.text != '':
            pr_kl = int(self.pr_kley_input.text)
        else:
            pr_kl = 0
        if self.workmans_input.text != '':
            man = int(self.workmans_input.text)
        else:
            man = 0

        self.answer_output.text = str(kv + sh_kaf + dli_kaf + pr_kaf + pr_kl + gr + man)


# Меню расчета Штукатурка
class OtdelkaFourth(Screen):
    def calculate_shtukaturka(self):
        if self.kvadrat_input.text != '':
            kv = int(self.kvadrat_input.text)
        else:
            kv = 0
        if self.smes_input.text != '':
            smes = int(self.smes_input.text)
        else:
            smes = 0
        if self.tsement_input.text != '':
            ts = int(self.tsement_input.text)
        else:
            ts = 0
        if self.pr_gruntovka_input.text != '':
            gr = int(self.pr_gruntovka_input.text)
        else:
            gr = 0
        if self.pesok_input.text != '':
            ps = int(self.pesok_input.text)
        else:
            ps = 0
        if self.setka_input.text != '':
            se = int(self.setka_input.text)
        else:
            se = 0
        if self.workmans_input.text != '':
            man = int(self.workmans_input.text)
        else:
            man = 0

        self.answer_output.text = str(kv + smes + ts + ps + se + gr + man)

# Расчет меню бетона
class BetonMain(Screen):
    pass

# Ленточный фундамент
class OneBeton(Screen):
    pass

# Колонна
class ColonaBeton(Screen):
    pass


# Рвсчет меню кладки
class KladkaMain(Screen):
    pass

# Расчет меню пола
class PolMain(Screen):
    pass


class Cafel(Screen):
    def calculate_cafel(self):
        if self.kvadrat_input.text != '':
             kv = int(self.kvadrat_input.text)
        else:
            kv = 0
        if self.shirina_cafel_input.text != '':
            shi = int(self.shirina_cafel_input.text)
        else:
            shi = 0
        if self.dlina_cafel_input.text != '':
            dli= int(self.dlina_cafel_input.text)
        else:
            dli = 0
        if self.kley_input.text != '':
            kley = int(self.kley_input.text)
        else:
            kley = 0
        if self.pr_gruntovka_input.text != '':
            grunt = int(self.pr_gruntovka_input.text)
        else:
            grunt = 0
        if self.workmans_input.text != '':
            man = int(self.workmans_input.text)
        else:
            man = 0
        if self.fuga_input.text != '':
            fuga = int(self.fuga_input.text)
        else:
            fuga = 0

        self.answer_output.text = str(kv + shi + dli + kley + grunt + man + fuga)

class Laminat(Screen):
    def calculate_laminat(self):
        if self.kvadrat_input.text != '':
            kv = int(self.kvadrat_input.text)
        else:
            kv = 0
        if self.shirina_laminat_input.text != '':
            shi = int(self.shirina_laminat_input.text)
        else:
            shi = 0
        if self.dlina_laminat_input.text != '':
            dli = int(self.dlina_laminat_input.text)
        else:
            dli = 0
        if self.podstilka_input.text != '':
            pod = int(self.podstilka_input.text)
        else:
            pod = 0
        if self.samorezi_input.text != '':
            sam = int(self.samorezi_input.text)
        else:
            sam = 0
        if self.workmans_input.text != '':
            man = int(self.workmans_input.text)
        else:
            man = 0

        self.answer_output.text = str(kv + shi + dli + pod + sam + man)



class Parkent(Screen):
    def calculate_parkent(self):
        if self.kvadrat_input.text != '':
            kv = int(self.kvadrat_input.text)
        else:
            kv = 0
        if self.shirina_parket_input.text != '':
            shi = int(self.shirina_parket_input.text)
        else:
            shi = 0
        if self.dlina_parket_input.text != '':
            dli = int(self.dlina_parket_input.text)
        else:
            dli = 0
        if self.podstilka_input.text != '':
            pod = int(self.podstilka_input.text)
        else:
            pod = 0
        if self.samorezi_input.text != '':
            sam = int(self.samorezi_input.text)
        else:
            sam = 0
        if self.workmans_input.text != '':
            man = int(self.workmans_input.text)
        else:
            man = 0

        self.answer_output.text = str(kv + shi + dli + pod + sam + man)




class IconListItem(OneLineIconListItem):
    icon = StringProperty()

class TolikApp(MDApp):
        #self.screen = Builder.load_file('Main.kv')

    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'DeepPurple'
     
        return Builder.load_file('Main.kv')


TolikApp().run()
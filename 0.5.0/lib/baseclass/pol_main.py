# Расчет меню пола
from kivy.uix.popup import Popup
from kivymd.uix.boxlayout import MDBoxLayout


class PolMain(MDBoxLayout):
    pass


class Cafel(Popup):
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
            dli = int(self.dlina_cafel_input.text)
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


class Laminat(Popup):
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


class Parkent(Popup):
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

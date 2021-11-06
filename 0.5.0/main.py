# ver: 0.5.0
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import StringProperty, ListProperty, ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp

from kivymd.theming import ThemableBehavior
from kivymd.uix.boxlayout import MDBoxLayout

from kivymd.uix.list import OneLineIconListItem, MDList
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.tab import MDTabsBase

from kivy.metrics import dp

from kivymd.uix.filemanager import MDFileManager
from kivymd.toast import toast

from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineAvatarIconListItem


# Window.size = (340, 600)



# Насторойки цвета в кнопках меню "MDNavigationDrawer"
class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()
    text_color = ListProperty((0, 0, 0, 1))
    text = StringProperty()


class DrawerList(ThemableBehavior, MDList):
    def set_color_item(self, instance_item):
        """Called when tap on a menu item."""

        # Set the color of the icon and text for the menu item.
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color


class Tab(MDFloatLayout, MDTabsBase):
    pass


class IconListItem(OneLineIconListItem):
    icon = StringProperty()


class ItemConfirm(OneLineAvatarIconListItem):
    divider = None

    def set_icon(self, instance_check):
        instance_check.active = True
        check_list = instance_check.get_widgets(instance_check.group)
        for check in check_list:
            if check != instance_check:
                check.active = False


class TolikApp(MDApp):
    title = 'Строительный калькулятор'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_file('Main.kv')

        kirpich_items = ['Одинарный: 250*120*65мм', 'Полуторный: 250*120*88мм', 'Двойной: 250*120*140мм']

        menu_kirpich = [{'viewclass': 'IconListItem', 'height': dp(56), 'text': kirpich_items[i],
                         'on_release': lambda x=kirpich_items[i]: self.set_item_kirpich(x)} for i in range(3)]
        kladka_items = ['Кирпичей 0.5', 'Кирпичей 1', 'Кирпичей 1.5', 'Кирпичей 2']

        menu_items = [{'viewclass': 'IconListItem', # 'icon': 'git',
            'height': dp(56), 'text': kladka_items[i], 'on_release': lambda x=kladka_items[i]: self.set_item_kladka(x)}
            for i in range(4)]

        self.menu = MDDropdownMenu(caller=self.screen.ids.kladka, items=menu_items, position='auto', width_mult=4)

        self.menu2 = MDDropdownMenu(caller=self.screen.ids.kirpich, items=menu_kirpich, position='auto', width_mult=7)

        # Типы полового покрытия
        pol_items = ['Ламинат', 'Паркет', 'Линолеум', 'Ковролин']

        menu_pol = [{'viewclass': 'IconListItem', # 'icon': 'git',
            'height': dp(56), 'text': pol_items[i], 'on_release': lambda x=pol_items[i]: self.set_item_pol(x)} for i in
            range(4)]

        self.menu3 = MDDropdownMenu(caller=self.screen.ids.pol, items=menu_pol, position='auto', width_mult=4)

        # Файлменеджер
        Window.bind(on_keyboard=self.events)
        self.manager_open = False
        self.file_manager = MDFileManager(exit_manager=self.exit_manager, select_path=self.select_path, preview=True, )

    def build(self):

        return self.screen

    def on_tab_switch(self, instance_tabs, instance_tab, instance_tab_label, tab_text):

        print('tab cliced' + tab_text)

    # Кладка расчет
    vid_kladki = None
    vid_kirpicha = None
    text_vid_kladki = ''
    shov_da_net = 'normal'
    # м3 кирпича на 3м2 сетки
    setka_norma = 3

    # Вид пола
    vid_pola = None

    # Флажок учитывать швы или нет
    def on_checkbox_active(self, checkbox, value):
        print(checkbox.state)
        self.shov_da_net = checkbox.state
        print(self.shov_da_net)

    # Выбор размера кирпича
    def set_item_kirpich(self, text_item):
        print('set item ' + text_item)
        self.screen.ids.kirpich.text = text_item
        self.vid_kirpicha = text_item
        print(self.vid_kirpicha)
        self.menu2.dismiss()

    # Выбор вида кладки
    def set_item_kladka(self, text_item):
        print('set item ' + text_item)
        self.screen.ids.kladka.text = text_item
        self.vid_kladki = text_item
        print(self.vid_kladki)
        self.menu.dismiss()

    # Выбор типа покрытия пол
    def set_item_pol(self, text_item):
        print('set item ' + text_item)
        self.screen.ids.pol.text = text_item
        self.vid_pola = text_item
        print(self.vid_pola)
        self.menu3.dismiss()

    def calculate_kladka(self, *args):
        global kladka, rostvor, setka
        if self.screen.ids.kvadrat_input.text != '':
            kv = int(self.screen.ids.kvadrat_input.text)
        else:
            kv = 0
        # Выбор кладки(количетво кирпичей в кв.м)
        if self.vid_kladki == 'Кирпичей 0.5':
            if self.shov_da_net == 'down':
                if self.vid_kirpicha == 'Одинарный: 250*120*65мм':
                    kladka = 51
                    rostvor = 0.023

                if self.vid_kirpicha == 'Полуторный: 250*120*88мм':
                    kladka = 39
                    rostvor = 0.021

                if self.vid_kirpicha == 'Двойной: 250*120*140мм':
                    kladka = 26
                    rostvor = 0.019
            else:
                if self.vid_kirpicha == 'Одинарный: 250*120*65мм':
                    kladka = 61
                if self.vid_kirpicha == 'Полуторный: 250*120*88мм':
                    kladka = 45
                if self.vid_kirpicha == 'Двойной: 250*120*140мм':
                    kladka = 30
                rostvor = 0

            setka = kladka * 0.025

        if self.vid_kladki == 'Кирпичей 1':
            if self.shov_da_net == 'down':
                if self.vid_kirpicha == 'Одинарный: 250*120*65мм':
                    kladka = 102
                    rostvor = 0.058  # setka = kladka * 0.025
                if self.vid_kirpicha == 'Полуторный: 250*120*88мм':
                    kladka = 78
                    rostvor = 0.051
                    setka = kladka * 0.025
                if self.vid_kirpicha == 'Двойной: 250*120*140мм':
                    kladka = 52
                    rostvor = 0.042  # setka = kladka * 0.025
            else:
                if self.vid_kirpicha == 'Одинарный: 250*120*65мм':
                    kladka = 128
                if self.vid_kirpicha == 'Полуторный: 250*120*88мм':
                    kladka = 95
                if self.vid_kirpicha == 'Двойной: 250*120*140мм':
                    kladka = 60
                rostvor = 0

            setka = kladka * 0.025

        if self.vid_kladki == 'Кирпичей 1.5':
            if self.shov_da_net == 'down':
                if self.vid_kirpicha == 'Одинарный: 250*120*65мм':
                    kladka = 153
                    rostvor = 0.088  # setka = kladka * 0.025
                if self.vid_kirpicha == 'Полуторный: 250*120*88мм':
                    kladka = 117
                    rostvor = 0.077  # setka = kladka * 0.025
                if self.vid_kirpicha == 'Двойной: 250*120*140мм':
                    kladka = 78
                    rostvor = 0.064  # setka = kladka * 0.025
            else:
                if self.vid_kirpicha == 'Одинарный: 250*120*65мм':
                    kladka = 189
                if self.vid_kirpicha == 'Полуторный: 250*120*88мм':
                    kladka = 140
                if self.vid_kirpicha == 'Двойной: 250*120*140мм':
                    kladka = 90
                rostvor = 0

        if self.vid_kladki == 'Кирпичей 2':
            if self.shov_da_net == 'down':
                if self.vid_kirpicha == 'Одинарный: 250*120*65мм':
                    kladka = 204
                    rostvor = 0.24 / 394 * kladka # setka = kladka * 0.025
                if self.vid_kirpicha == 'Полуторный: 250*120*88мм':
                    kladka = 156
                    rostvor = 0.22 / 294 * kladka # setka = kladka * 0.025
                if self.vid_kirpicha == 'Двойной: 250*120*140мм':
                    kladka = 104
                    rostvor = 0.086  # setka = kladka * 0.025
            else:
                if self.vid_kirpicha == 'Одинарный: 250*120*65мм':
                    kladka = 256
                    setka = kladka * 0.025
                if self.vid_kirpicha == 'Полуторный: 250*120*88мм':
                    kladka = 190
                    setka = kladka * 0.025
                if self.vid_kirpicha == 'Двойной: 250*120*140мм':
                    kladka = 120
                    setka = kladka * 0.025
                rostvor = 0

            setka = kladka * 0.025

        if self.screen.ids.kirpich_input.text != '':
            kirpich = int(self.screen.ids.kirpich_input.text)
        else:
            kirpich = 0
        if self.screen.ids.tsement_input.text != '':
            tsement = int(self.screen.ids.tsement_input.text)
        else:
            tsement = 0
        if self.screen.ids.setka_input.text != '':
            pr_setka = int(self.screen.ids.workmans_input.text)
        else:
            pr_setka = 0
            stoimost_setka = 0

        # Количество раствора
        try:
            stoimost_rastvor = (kv * kladka) * rostvor
            self.screen.ids.col_rostvor.text = str(stoimost_rastvor) + ' м3'
        except:
            self.screen.ids.col_rostvor.text = 'Заполните все поля'

        # Стоимость всего раствора
        try:
            self.screen.ids.col_pr_rostvor.text = str(((kv * kladka) * rostvor) * tsement)
        except:
            self.screen.ids.col_pr_rostvor.text = 'Введите стоимость раствора кладочеого за м3'

        # Количество сетки
        try:
            self.screen.ids.col_setki.text = str(setka * (kv * kladka)) + ' кг'
        except:
            self.screen.ids.col_setki.text = 'Заполните все поля'

        # Стоимость всей сетки
        try:
            stoimost_setka = setka * (kv * kladka) * pr_setka
            self.screen.ids.col_pr_setki.text = str(stoimost_setka)
        except:
            self.screen.ids.col_pr_setki.text = 'Введите стоимость сетки кладочной'

        # Количество кирпича
        try:
            self.screen.ids.col_kirpich.text = str(kladka * kv) + ' шт'
        except:
            self.screen.ids.col_kirpich.text = 'Заполните все поля'

        # Стоимость всех кирпичей
        try:
            pr_kirpich = kladka * kv * kirpich
            self.screen.ids.col_pr_kirpich.text = str(pr_kirpich)
        except:
            self.screen.ids.col_pr_kirpich.text = 'Введите стоимость кирпича за штуку'

        # Общая стоимость
        try:
            if tsement != 0:
                stoimost_rastvor = kv * kladka * rostvor * tsement
            else:
                stoimost_rastvor = 0
            if pr_setka != 0:
                stoimost_setka = setka * (kv * kladka) * pr_setka
            else:
                stoimost_setka = 0
            if pr_kirpich != 0:
                pr_kirpich = kladka * kv * kirpich
            self.screen.ids.answer_output.text = str(pr_kirpich + stoimost_setka + stoimost_rastvor)
        except:
            self.screen.ids.answer_output.text = 'Заполните все поля'

    # Расчет пола
    def calculate_pol(self, *args):
        print('start')
        if self.screen.ids.pr_pok.text != '':
            print('пустой')
            pr = int(self.screen.ids.pr_pok.text)
        else:
            print('заполнен')
            self.screen.ids.answer_output.text = 'Введите цену'
            pr = 0
        if self.screen.ids.shirina_pok.text != '':
            sh_pol = int(self.screen.ids.shirina_pok.text)
        else:
            sh_pol = 0
        if self.screen.ids.dlina_pok.text != '':
            dl_pok = int(self.screen.ids.dlina_pok.text)
        else:
            dl_pok = 0
        if self.screen.ids.shirina.text != '':
            sh = int(self.screen.ids.shirina.text)
        else:
            sh = 0
        if self.screen.ids.dlina.text != '':
            dl = int(self.screen.ids.dlina.text)
        else:
            dl = 0

        shtuka = sh_pol * dl_pok
        pol = sh * dl

        #self.screen.ids.answer_output.text = 'Введено неверное значение'

        if self.vid_pola == 'Ламинат' or self.vid_pola == 'Паркет':
            itog = (pol + (pol / 100 * 5)) / shtuka
            self.screen.ids.col_pol.text = str(itog)
            if pr != 0:
                self.screen.ids.answer_output.text = str(itog * pr)
        if self.vid_pola == 'Линолеум':
            pass
        if self.vid_pola == 'Ковролин':
            pass

    # Файлменеджер
    def file_manager_open(self):
        self.file_manager.show('/')  # output manager to the screen
        self.manager_open = True

    def select_path(self, path):
        '''It will be called when you click on the file name
        or the catalog selection button.

        :type path: str;
        :param path: path to the selected directory or file;
        '''

        self.exit_manager()
        toast(path)

    def exit_manager(self, *args):
        '''Called when the user reaches the root of the directory tree.'''

        self.manager_open = False
        self.file_manager.close()

    def events(self, instance, keyboard, keycode, text, modifiers):
        '''Called when buttons are pressed on the mobile device.'''

        if keyboard in (1001, 27):
            if self.manager_open:
                self.file_manager.back()
        return True

    color_text_a = 1, .05, .02, 1
    color_text_b = .97, 1, .08, 1
    color_text_c = .06, 1, .06, 1
    color_text_d = .18, .02, 1, 1
    color_text_f = .96, .11, .96, 1

    # Button and Labels
    text_color_button = 0, 0, 0, 1  # Светлый
    text_color_label = (0, 0, 0, 1)
    menu_text_color_button = 0, 0, 0, 1
    popup_color = (1, 1, 1, 1)
    set_md_bg_color = (.73, .73, .73, 1)

    def switch_theme_style(self):
        self.theme_cls.theme_style = ("Light" if self.theme_cls.theme_style == "Dark" else "Dark")
        # self.root.ids.backdrop.ids._front_layer.md_bg_color = [0, 0, 0, 0]

        if self.theme_cls.theme_style == "Dark":
            #  self.theme_text_color = "Dark"
            self.text_color_button = (1, 1, 1, 1)  # Темный
            self.text_color_label = (1, 1, 1, 1)
            self.popup_color = (0, 0, 0, 1)
            self.set_md_bg_color = (.78, .78, .78, 1)  # self.menu_text_color_button = (0, 0, 0, 1)
        else:
            self.text_color_button = (0, 0, 0, 1)  # Светлый
            self.text_color_label = (0, 0, 0, 1)
            self.popup_color = (1, 1, 1, 1)
            self.set_md_bg_color = (.73, .73, .73, 1)  # self.menu_text_color_button = (0, 0, 0, 1)


if __name__ == '__main__':
    TolikApp().run()

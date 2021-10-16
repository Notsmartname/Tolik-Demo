# ver: 0.4.0
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


class Content(MDBoxLayout):
    pass


class WindowManager(ScreenManager):
    pass


class GlobalMain(MDBoxLayout):
    pass


# Расчет отделки помещений
class OtdelkaMain(Screen):
    pass


# Покраска стен
class OtdelkaFirst(Popup):
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
class OtdelkaSecend(Popup):
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
class OtdelkaThird(Popup):
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
class OtdelkaFourth(Popup):
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
class BetonMain(MDBoxLayout):
    pass


# Ленточный фундамент
class OneBeton(Popup):
    pass


class TwoBeton(Popup):
    pass


class TreeBeton(Popup):
    pass


class FourBeton(Popup):
    pass


# Колонна
class ColonaBeton(Screen):
    pass


# Рвсчет меню кладки
class KladkaMain(MDBoxLayout):
    pass

# Расчет меню пола
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

    # self.screen = Builder.load_file('Main.kv')

    title = 'Строительный калькулятор'

    # Нужна функцыя на тему
    # Ц


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_file('Main.kv')



        kladka_items = [
            'Кирпичей 0.5', 'Кирпичей 1', 'Кирпичей 1.5', 'Кирпичей 2'
        ]
        menu_items = [
            {
                'viewclass': 'IconListItem',
                # 'icon': 'git',
                'height': dp(56),
                'text': kladka_items[i],
                'on_release': lambda x=kladka_items[i]: self.set_item(x)
            } for i in range(4)]

        self.menu = MDDropdownMenu(
            caller=self.screen.ids.field,
            items=menu_items,
            position='auto',
            width_mult=4
        )

        # Файлменеджер
        Window.bind(on_keyboard=self.events)
        self.manager_open = False
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
            preview=True,
        )

    def set_item(self, text_item):
        print('set item ' + text_item)
        self.screen.ids.field.text = text_item
        self.menu.dismiss()

    def build(self):


        # self.theme_cls.theme_style = self.theme_set
            # 'Dark'
        # self.theme_cls.accent_palette = 'Gray'
        # self.theme_cls.primary_palette = 'DeepPurple'

        # return Builder.load_file('Test.kv')
        return self.screen

    '''def on_start(self):
        icons_item_menu_lines = {
            "folder": "My files",
            "calculator": "Калькулятор",
            "cog-outline": "Настройки",
            "upload": "Обновить",
            'content-save-outline': 'Сохранить',
            'delete-circle-outline': 'Удалить',
            'decagram': 'Dark',
            'decagram-outline': 'Laught',

        }
        for icon_name in icons_item_menu_lines.keys():
            self.root.ids.content_drawer.ids.md_list.add_widget(
             ItemDrawer(icon=icon_name, text=icons_item_menu_lines[icon_name])
            )'''
            
    #def on_touch_down(self, touch):

        # Пробный список меню
        # for name_tab in list(icon_name_for_tabs.keys()):
        #     self.root.ids.tabs.add_widget(Tab(icon=name_tab, title=icon_name_for_tabs[name_tab]))

    def on_tab_switch(self, instance_tabs, instance_tab, instance_tab_label, tab_text):

        print('tab cliced' + tab_text)

    def on_star_click(self):
        pass

    def calculate_kladka(self, *args):
        if self.screen.ids.pogonash_input.text != '':
            kv = int(self.screen.ids.pogonash_input.text)
        else:
            kv = 0
        if self.screen.ids.shirina_input.text != '':
            shi = int(self.screen.ids.shirina_input.text)
        else:
            shi = 0
        if self.screen.ids.dlina_input.text != '':
            dli = int(self.screen.ids.dlina_input.text)
        else:
            dli = 0
        if self.screen.ids.kirpich_input.text != '':
            kley = int(self.screen.ids.kirpich_input.text)
        else:
            kley = 0
        if self.screen.ids.tsement_input.text != '':
            grunt = int(self.screen.ids.tsement_input.text)
        else:
            grunt = 0
        if self.screen.ids.workmans_input.text != '':
            man = int(self.screen.ids.workmans_input.text)
        else:
            man = 0
        if self.screen.ids.pesok_input.text != '':
            fuga = int(self.screen.ids.pesok_input.text)
        else:
            fuga = 0

        self.screen.ids.answer_output.text = str(kv + shi + dli + kley + grunt + man + fuga)

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

    # Настройки окно, в приложении
    '''dialog = None

    def show_confirmation_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Насторйки",
                type="confirmation",
                items=[                    
                    ItemConfirm(text="Dark"),
                    ItemConfirm(text="Light"),
                ],
                buttons=[
                    MDFlatButton(
                        text="CANCEL", text_color=self.theme_cls.primary_color, on_press=self.dialog_close
                    ),
                    MDFlatButton(
                        text="OK", text_color=self.theme_cls.primary_color, on_release=self.change_theme, on_press=self.dialog_close
                    ),
                ],
            )
        self.dialog.open()'''

    text_color_button = 0, 0, 0, 1  # Светлый
    text_color_label = (0, 0, 0, 1)
    menu_text_color_button = 0, 0, 0, 1
    popup_color = (1, 1, 1, 1)
    set_md_bg_color = (.73, .73, .73, 1)
    # theme_text_color = "Light"

    def switch_theme_style(self):
        self.theme_cls.theme_style = (
            "Light" if self.theme_cls.theme_style == "Dark" else "Dark"
        )
        # self.root.ids.backdrop.ids._front_layer.md_bg_color = [0, 0, 0, 0]

        if self.theme_cls.theme_style == "Dark":
           #  self.theme_text_color = "Dark"
            self.text_color_button = (1, 1, 1, 1)  # Темный
            self.text_color_label = (1, 1, 1, 1)
            self.popup_color = (0, 0, 0, 1)
            self.set_md_bg_color = (.78, .78, .78, 1)
            self.menu_text_color_button = (0, 0, 0, 1)
        else:
            self.text_color_button = (0, 0, 0, 1)  # Светлый
            self.text_color_label = (0, 0, 0, 1)
            self.popup_color = (1, 1, 1, 1)
            self.set_md_bg_color = (.73, .73, .73, 1)
            self.menu_text_color_button = (0, 0, 0, 1)

    # Выбор бетона





TolikApp().run()

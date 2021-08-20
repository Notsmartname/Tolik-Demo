__all__=('OnemainCont')

from kivy.factory import Factory
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

kv = Builder.load_file('onemain.kv')

class OnemainCont(BoxLayout):
    pass


Factory.register('OnemainCont', cls=OnemainCont)
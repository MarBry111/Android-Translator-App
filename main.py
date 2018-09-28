#version.regex
#__version__= '1.0'
from googletrans import Translator

import kivy
kivy.require('1.9.0')
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window

class TestApp(App):

    title = 'Translate^3'
    lan = 'pl'
    f_size = 20

    def translator(self, text, org_lan='pl', trans_lan='en'):
        translator = Translator()
        trans_text = translator.translate(text, src=org_lan, dest=trans_lan)
        return trans_text.text

    def build(self):
        #Window.size = (300, 400)

        def update(instance):
            if self.lan == 'pl':
                t_ru.text = self.translator(text=t_pl.text, org_lan='pl', trans_lan='ru')
                t_en.text = self.translator(text=t_pl.text, org_lan='pl', trans_lan='en')
            elif self.lan == 'ru':
                t_pl.text = self.translator(text=t_ru.text, org_lan='ru', trans_lan='pl')
                t_en.text = self.translator(text=t_ru.text, org_lan='ru', trans_lan='en')
            elif self.lan == 'en':
                t_pl.text = self.translator(text=t_en.text, org_lan='en', trans_lan='pl')
                t_ru.text = self.translator(text=t_en.text, org_lan='en', trans_lan='ru')

        def update_lan(instance, value):
            coordinate_y = value.pos[1]
            height = Window.size[1]
            if coordinate_y > height*3/4 and coordinate_y <= height:
                self.lan = 'pl'
            elif coordinate_y > height/2 and coordinate_y <= height*3/4:
                self.lan = 'ru'
            elif coordinate_y > height/4 and coordinate_y <= height/2:
                self.lan = 'en'

        b = BoxLayout(orientation='vertical')
        translate_button = Button(text='Translate')

        t_pl = TextInput(text="jakiś tekst",
                         font_size=self.f_size)
        t_ru = TextInput(text=self.translator(text=t_pl.text, org_lan='pl', trans_lan='ru'),
                         font_size=self.f_size)
        t_en = TextInput(text=self.translator(text=t_pl.text, org_lan='pl', trans_lan='en'),
                         font_size=self.f_size)

        b.bind(on_touch_down=update_lan)

        translate_button.bind(on_press=update)

        b.add_widget(t_pl)
        b.add_widget(t_ru)
        b.add_widget(t_en)
        b.add_widget(translate_button)

        return b


if __name__ == '__main__':
    TestApp().run()





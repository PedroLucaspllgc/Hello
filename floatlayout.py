from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button

class MinhaApp(App):
    def build(self):
        layout_float = FloatLayout()

        btn1 = Button(text='Botão 1', size_hint=(None, None), size=(100, 50), pos_hint=('x': 0.1, 'y': 0.8))
        btn2 = Button(text='Botão 2', size_hint=(None, None), size=(100, 50), pos_hint=('center_x': 0.5, 'center_y': 0.5))
        btn3 = Button(text='Botão 3', size_hint=(None, None), size=(100, 50), pos_hint=('right': 0.9, 'y': 0.1))

        layout_float.add_widget(btn1)
        layout_float.add_widget(btn2)
        layout_float.add_widget(btn3)

        return layout_float
    
if _name__ == "__main":
    MinhaApp().run()

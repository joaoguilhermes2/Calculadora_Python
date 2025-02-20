from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
import math

class CalculatorApp(App):
    def build(self):
        self.entrada = TextInput(
            font_size=32, readonly=True, halign='right', multiline=False,
            background_color=(0.2, 0.2, 0.2, 1), foreground_color=(1, 1, 1, 1)
        )
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        layout.add_widget(self.entrada)
        
        botoes = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['C', '0', '=', '+'],
            ['^', '√', '⌫', 'AC']
        ]
        
        for linha in botoes:
            h_layout = BoxLayout(spacing=10)
            for label in linha:
                botao = Button(
                    text=label, font_size=24, background_color=(0.3, 0.3, 0.3, 1),
                    color=(1, 1, 1, 1), size_hint=(1, 1)
                )
                botao.bind(on_press=self.on_button_press)
                h_layout.add_widget(botao)
            layout.add_widget(h_layout)
        
        return layout
    
    def on_button_press(self, instance):
        texto = instance.text
        if texto == "C":
            self.entrada.text = ""
        elif texto == "AC":
            self.entrada.text = ""
        elif texto == "⌫":
            self.entrada.text = self.entrada.text[:-1]
        elif texto == "=":
            try:
                self.entrada.text = str(eval(self.entrada.text))
            except:
                self.entrada.text = "Erro"
        elif texto == "^":
            self.entrada.text += "**"
        elif texto == "√":
            try:
                self.entrada.text = str(math.sqrt(float(self.entrada.text)))
            except:
                self.entrada.text = "Erro"
        else:
            self.entrada.text += texto

if __name__ == "__main__":
    CalculatorApp().run()
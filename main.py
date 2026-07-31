from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock

class OrigenApp(App):
    def build(self):
        self.layout = BoxLayout()
        self.label = Label(text="ORIGEN NX1", font_size=40, color=(0,1,0,1))
        self.layout.add_widget(self.label)
        Clock.schedule_once(self.paso1, 1)
        return self.layout

    def paso1(self, dt):
        self.label.text = "5VpulseOS v0.1"
        Clock.schedule_once(self.paso2, 1.5)

    def paso2(self, dt):
        self.label.text = "Cargando Nucleo..."
        Clock.schedule_once(self.paso3, 2)

    def paso3(self, dt):
        self.label.text = "Sistema Listo"

if __name__ == '__main__':
    OrigenApp().run()

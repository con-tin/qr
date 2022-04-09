import qrcode
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.app import App
class TestApp(App):
    def build(self):
        self.layout = GridLayout(cols=2)
        self.text = TextInput(text="Введите ссылку")
        self.btn = Button(text="Создать")
        self.layout.add_widget(self.text)
        self.layout.add_widget(self.btn)
        self.btn.bind(on_press=self.generation)

        return self.layout

    def generation(self, f):
        print(self.text.text)
        data = self.text.text
        File = "QR.png"
        QRimage = qrcode.make(data)
        QRimage.save("QR.png")



TestApp().run()


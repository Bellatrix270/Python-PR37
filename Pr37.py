from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config
Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 400)
Config.set('graphics', 'height', 500)

class CalculatorApp(App):
    def update_lblOutput(self):
        self.lblOutput.text = self.formula

    def add_number(self, instance):
        if (self.formula == "0"):
            self.formula = ""

        self.formula += str(instance.text)
        print(self.formula)
        self.update_lblOutput()
    
    def add_operation(self, instance):
        self.formula += str(instance.text)
        self.update_lblOutput()

    def getResult(self, instance):
        self.lblOutput.text = str(eval(self.lblOutput.text))
        self.formula = self.lblOutput.text

    def clearResult(self, instance):
        self.lblOutput.text = "0"
        self.formula = "0"

    def build(self):
        self.formula = "0"
        boxLayout = BoxLayout(orientation='vertical', padding = 25)
        grid = GridLayout(cols = 4, spacing = 5)

        self.lblOutput = Label(text="0", font_size = 45, halign="right", valign="center", size_hint=(1, .4), text_size=(400-50, 500 * .4 - 50))
        boxLayout.add_widget( self.lblOutput )

        grid.add_widget( Button(text="9", on_press = self.add_number) )
        grid.add_widget( Button(text="8", on_press = self.add_number) )
        grid.add_widget( Button(text="7", on_press = self.add_number) )
        grid.add_widget( Button(text="*", on_press = self.add_operation) )

        grid.add_widget( Button(text="6", on_press = self.add_number) )
        grid.add_widget( Button(text="5", on_press = self.add_number) )
        grid.add_widget( Button(text="4", on_press = self.add_number) )
        grid.add_widget( Button(text="-", on_press = self.add_operation) )

        grid.add_widget( Button(text="1", on_press = self.add_number) )
        grid.add_widget( Button(text="2", on_press = self.add_number) )
        grid.add_widget( Button(text="3", on_press = self.add_number) )
        grid.add_widget( Button(text="+", on_press = self.add_operation) )

        grid.add_widget( Button(text="C", on_press = self.clearResult) )
        grid.add_widget( Button(text="0", on_press = self.add_number) )
        grid.add_widget( Button(text=".", on_press = self.add_number) )
        grid.add_widget( Button(text="=", on_press = self.getResult) )

        boxLayout.add_widget(grid)
        return boxLayout

if __name__ == "__main__":
    CalculatorApp().run()
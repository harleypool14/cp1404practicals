from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934  # Conversion constant


class MilesConverterApp(App):
    """Converting miles to kilometers using kivy app"""
    output_km = StringProperty()

    def build(self):
        """Build the Kivy app from the kv file"""
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self, text):
        """Handle calculation"""
        try:
            miles = float(text)
            self.output_km = str(miles * MILES_TO_KM)
        except ValueError:
            self.output_km = "0.0"

    def handle_increment(self, text, change):
        """Handle up and down button press"""
        try:
            result = float(text) + change
        except ValueError:
            result = change
        self.root.ids.input_miles.text = str(result)


MilesConverterApp().run()

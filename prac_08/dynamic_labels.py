from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """Kivy app to demo dynamic label creation"""

    def __init__(self, **kwargs):
        """Construct main app"""
        super().__init__(**kwargs)
        self.names = ["Bob Brown", "Cat Cyan", "Oren Ochre", "Pete Purple"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)
        return self.root


DynamicLabelsApp().run()
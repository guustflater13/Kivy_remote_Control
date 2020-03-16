from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.clock import Clock
import time


# Builder.load_file('Control.kv')


class Control(BoxLayout):
    your_time = StringProperty()
    rotate_value = StringProperty()
    arm_under_value = StringProperty()
    arm_above_value = StringProperty()
    gripper_value = StringProperty()

    def __init__(self, **kwargs):
        super(Control, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.padding = 10
        self.rotate_value = "10"
        self.arm_under_value = "10"
        self.arm_above_value = "10"
        self.gripper_value = "10"

        Clock.schedule_interval(self.set_time, 0.1)

    def set_time(self, dt):
        self.your_time = time.strftime("%m/%d/%Y %H:%M")


class ControlApp(App):
    def build(self):
        return Control()


if __name__ == "__main__":
    ControlApp().run()

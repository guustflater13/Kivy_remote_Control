from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.properties import NumericProperty
from kivy.clock import Clock
import time


# Builder.load_file('Control.kv')


def calc_vert(up):
    up = up
    x = 666
    y = 666
    return x, y


class Control(BoxLayout):
    your_time = StringProperty()
    str_rotate = StringProperty()
    str_arm_under = StringProperty()
    str_arm_above = StringProperty()
    str_gripper = StringProperty()
    str_posy = StringProperty()
    str_posx = StringProperty()
    str_posr = StringProperty()

    # arm_under = 0
    # arm_above = 0
    # gripper = 0

    def __init__(self, **kwargs):
        super(Control, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.padding = 10
        self.posy = 0  # vertical position
        self.posx = 0  # horizontal position
        self.posr = rotate = 0  # rotate
        arm_under = 0
        arm_above = 0
        self.step = 1
        self.gripper = 0  # 0 = closed, 1 = open
        self.str_rotate = str(rotate)
        self.str_arm_under = str(arm_under)
        self.str_arm_above = str(arm_above)
        self.str_gripper = str(self.gripper)
        self.str_posy = str(self.posy)
        self.str_posx = str(self.posx)
        self.str_posr = str(self.posr)

        Clock.schedule_interval(self.set_time, 0.1)

    def set_time(self, dt):
        self.your_time = time.strftime("%m/%d/%Y %H:%M")

    def up(self):
        self.posy = self.posy + 1
        self.str_posy = str(self.posy)
        # calculate new values arm_under and arm_above
        arm_under, arm_above = calc_vert(self.posy)
        self.str_arm_under = str(arm_under)
        self.str_arm_above = str(arm_above)

    def down(self):
        self.posy = self.posy - 1
        self.str_posy = str(self.posy)

    def gripper_change(self):
        if self.gripper:
            self.gripper = 0
            self.str_gripper = str(self.gripper)
        else:
            self.gripper = 1
            self.str_gripper = str(self.gripper)

    def steps(self):
        self.step = 10


class ControlApp(App):

    def build(self):
        return Control()


if __name__ == "__main__":
    ControlApp().run()

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.properties import NumericProperty
from kivy.clock import Clock
import time
from RC_Client import *
from threading import Thread
from kivy.uix.button import Button


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
        self.step = 1  # default step
        self.ids.btn_step1.background_color = [1, 0, 1, 1]  # pressed
        self.gripper = 0  # 0 = cloes, 1 = open
        self.str_rotate = str(rotate)
        self.str_arm_under = str(arm_under)
        self.str_arm_above = str(arm_above)
        # self.str_gripper = self.gripper
        self.str_gripper = "Closed"
        self.str_posy = str(self.posy)
        self.str_posx = str(self.posx)
        self.str_posr = str(self.posr)
        self.connect = 0

        self.host = "localhost"
        self.port = 6666
        self.sock = MySocket(self.host, self.port)

        Clock.schedule_interval(self.set_time, 0.1)
        # get all known ids for debugging
        print(self.ids)

    def connect_to_robot(self):
        if self.connect == 0:
            if self.sock.open_connection():
                print("connected to: ", self.host, "with port ", self.port)
                self.ids.btn_con.text = "Disconnect"
                self.connect = 1
        else:
            print("disconnected from: ", self.host, "with port ", self.port)
            self.sock.close_connection()
            self.ids.btn_con.text = "Connect"
            self.connect = 0
            self.sock = MySocket()

    def set_time(self, dt):
        self.your_time = time.strftime("%m/%d/%Y %H:%M")

    def up(self):
        self.posy = self.posy + self.step
        self.str_posy = str(self.posy)
        # calculate new values arm_under and arm_above
        arm_under, arm_above = calc_vert(self.posy)
        self.str_arm_under = str(arm_under)
        self.str_arm_above = str(arm_above)
        message_list = [self.str_rotate, self.str_arm_under, self.str_arm_above, self.str_gripper]
        delimiter = ";"
        message = delimiter.join(message_list)
        self.sock.send_data(message)

    def down(self):
        self.posy = self.posy - self.step
        self.str_posy = str(self.posy)

    def left(self):
        self.posr = self.posr - self.step
        self.str_posr = str(self.posr)

    def right(self):
        self.posr = self.posr + self.step
        self.str_posr = str(self.posr)

    def forwards(self):
        self.posx = self.posx + self.step
        self.str_posx = str(self.posx)

    def backwards(self):
        self.posx = self.posx - self.step
        self.str_posx = str(self.posx)

    def gripper_change(self):
        if self.gripper:
            self.gripper = 0
            self.str_gripper = "Closed"
        else:
            self.gripper = 1
            self.str_gripper = "Open"

    def steps(self, inp_step):
        current_step = self.step
        self.step = inp_step
        all_steps = [1, 2, 5, 10]
        # reset current step
        self.ids.btn_step1.background_color = [1, 1, .5, 1]
        self.ids.btn_step2.background_color = [1, 1, .5, 1]
        self.ids.btn_step5.background_color = [1, 1, .5, 1]
        self.ids.btn_step10.background_color = [1, 1, .5, 1]
        if self.step == 1:
            self.ids.btn_step1.background_color = [1, 0, 1, 1]
        elif self.step == 2:
            self.ids.btn_step2.background_color = [1, 0, 1, 1]
        elif self.step == 5:
            self.ids.btn_step5.background_color = [1, 0, 1, 1]
        elif self.step == 10:
            self.ids.btn_step10.background_color = [1, 0, 1, 1]


class ControlApp(App):

    def build(self):
        return Control()


if __name__ == "__main__":
    ControlApp().run()

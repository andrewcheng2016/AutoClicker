import sys
from PyQt5 import QtWidgets
from pynput import keyboard
from pynput.mouse import Button, Controller

from raw_AutoClicker import Bot, start_click, exit_click

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('AutoClicker')
        self.resize(200, 100)
        self.click_interval = 1
        self.ui()

    def ui(self):
        self.input_reqest = QtWidgets.QLabel(self)
        self.input_reqest.setGeometry(20, 20, 300, 20)
        self.is_input_valid = False

        self.input_reqest.setText("Please input click Interval (sec)")


        self.input = QtWidgets.QLineEdit(self)
        self.input.setGeometry(40,40,100,20)
        self.input.textChanged.connect(self.check_input)


        self.instruction_label = QtWidgets.QLabel(self)
        self.instruction_label.setGeometry(20, 60, 300, 20)
        self.instruction_label.setText("Press (<ctrl>+ ,) to start/stop clicking and (<ctrl>+ .) to exit the program.")
        self.autoclick()

    def check_input(self):
        try:
            self.click_interval = float(self.input.text())
        except ValueError:
            return False

    def autoclick(self):
        self.mouse = Controller()  # the mouse
        self.click_thread = Bot(click_interval=self.click_interval)  # thread
        self.click_thread.start()  # starts the thread
        with keyboard.GlobalHotKeys({
                '<ctrl>+,': start_click,
                '<ctrl>+.': exit_click}) as listener:
            listener.join()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec_())
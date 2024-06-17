import os
import sys
import time
import threading
from pynput import keyboard
from pynput.mouse import Button, Controller
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit, QLabel,\
    QMessageBox, QAction, QMenuBar, QMenu
from PyQt5.QtGui import QIcon

class MyMainWindow(QMainWindow):
    def closeEvent(self, event):
        print("Close Window")
        super().closeEvent(event)
        exit_click()


class Bot(threading.Thread):
    def __init__(self, click_interval=1):
        super(Bot, self).__init__()
        self.click_interval = click_interval
        self.running = False
        self.program_running = True

    def start_clicking(self, click_interval):
        self.click_interval = click_interval
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                mouse.click(Button.left, count=1)
                # print(self.click_interval)
                time.sleep(self.click_interval)
            time.sleep(0.00001)

def start_click(click_interval=1):
    if click_thread.running:
        print("Stop clicking")
        click_thread.stop_clicking()
    else:
        print("Start clicking")
        click_thread.start_clicking(click_interval=click_interval)

def exit_click():
    print("Exit clicking")
    click_thread.exit()
    print("click_thread.exit()")
    listener_thread.program_running = False
    print("listener_thread.exit()")
    app.quit()
    print("app.quit()")
    window.close()
    print("window.close()")
    os.exit(0)
    print("os.exit()")


def show_warning_dialog(message):
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Warning)
    msg_box.setWindowTitle("Warning")
    msg_box.setText(message)
    msg_box.exec_()

def validate_input():
    user_input = text_edit.toPlainText()
    try:
        click_interval = float(user_input)
        if click_interval <= 0:
            show_warning_dialog("Interval must be positive")
            raise ValueError("Interval must be positive")
        start_click(click_interval=click_interval)
    except ValueError:
        show_warning_dialog("Invalid input. Please enter a positive number.")

def run_listener():
    with keyboard.GlobalHotKeys({
            '<ctrl>+.': validate_input}) as listener:
        listener.join()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.resize(220, 150)
    window.setWindowTitle("Clicker")
    window.setWindowIcon(QIcon('Icon.ico'))

    # menubar = QMenuBar(window)
    # menu_file = QMenu('About')
    # menubar.addMenu(menu_file)

    text_edit = QTextEdit(window)
    text_edit.setPlaceholderText("Click Interval (sec)")
    text_edit.setGeometry(20, 20, 180, 30)

    label = QLabel("Start/Stop: <Ctrl + .>", window)
    label.setGeometry(55, 60, 300, 30)


    start_button = QPushButton("Start/Stop Clicking", window)
    start_button.setGeometry(20, 100, 100, 30)
    start_button.clicked.connect(validate_input)

    exit_button = QPushButton("Exit", window)
    exit_button.setGeometry(150, 100, 50, 30)
    exit_button.clicked.connect(exit_click)
    mouse = Controller()
    click_thread = Bot()
    click_thread.start()
    window.show()

    listener_thread = threading.Thread(target=run_listener)
    listener_thread.start()

    sys.exit(app.exec_())

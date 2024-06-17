import time
import threading
from pynput import keyboard
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, Key, KeyCode
import pyautogui



# mouse click code
class Bot(threading.Thread):  # class that extends threading, allows us to mouse click
    def __init__(self, click_interval=1):
        super(Bot, self).__init__()
        self.click_interval = click_interval
        self.running = False
        self.program_running = True

    def start_clicking(self):  # start clicking
        self.running = True

    def stop_clicking(self):  # stop clicking
        self.running = False

    def exit(self):  # exit the program
        self.stop_clicking()
        self.program_running = False

    def run(self):  # running
        global time_diff
        while self.program_running:  # program isn't exited
            while self.running: #while the program is running
                mouse.click(Button.left, count = 1)
                time.sleep(click_interval) #delay in between, needed big time because the actual website must register the click
            time.sleep(0.00001)  # delay


def start_click():  # key press
    if click_thread.running:
        print("Stop clicking")
        click_thread.stop_clicking()  # stop

    else:
        print("Start clicking")
        click_thread.start_clicking()  # start



def exit_click():  # exit
    print("Exit clicking")
    click_thread.exit()
    quit()




if __name__ == "__main__":
    click_interval = float(input("Click Interval (sec)： "))
    print("Press (<ctrl>+ ,) to start/stop clicking and (<ctrl>+ .) to exit the program.")

    # creates everything
    mouse = Controller()  # the mouse
    click_thread = Bot(click_interval=click_interval)  # thread
    click_thread.start()  # starts the thread

    with keyboard.GlobalHotKeys({
            '<ctrl>+,': start_click,
            '<ctrl>+.': exit_click}) as listener:
        listener.join()


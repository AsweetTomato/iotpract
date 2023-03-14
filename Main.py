import time, datetime
import telepot
import RPi.GPIO as GPIO
from telepot.loop import MessageLoop
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(8, GPIO.OUT)
GPIO.output(8, False)
def action(msg):
chat_id = msg['chat']['id']
command = msg['text']
if 'alternate' in command:
message = "Alternate LED Scrolling " GPIO.output(11, True)
GPIO.output(15, True)
GPIO.output(13, False)
GPIO.output(8, False)
time.sleep(2)
telegram_bot= telepot.Bot('5908091289:AAGedw6IED-
ILMjpx5jBez2sCEGY5DKu3hE')
print(telegram_bot.getMe())
MessageLoop(telegram_bot, action).run_as_thread()
print('Up and Running....')
while 1:
time.sleep(10)

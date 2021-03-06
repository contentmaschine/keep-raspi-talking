from gpiozero import LED
from signal import pause
import concurrent.futures
import lcd_assets
import time

strike_counter = 0
wires_done = False
simon_says_done = False
sms_done = False


def strike(strike_pins: tuple=(23, 24, 25)):
    global strike_counter, sms_done
    if not sms_done:
        strike_pin = strike_pins[strike_counter]
        executor = concurrent.futures.ThreadPoolExecutor()
        executor.submit(strike_led_on, strike_pin)
        strike_counter += 1
        if strike_counter > 2:
            lcd_assets.explode(lcd_assets.countdown_process)
        # to prevent immediate 3 strikes, not elegant but what can you do
        time.sleep(0.75)

def strike_led_on(strike_pin: int):
    strike_led = LED(strike_pin)
    strike_led.on()
    pause()

def success(success_pin: int):
    executor = concurrent.futures.ThreadPoolExecutor()
    executor.submit(success_led_on, success_pin)

def success_led_on(success_pin):
    success_led = LED(success_pin)
    success_led.on()
    pause()

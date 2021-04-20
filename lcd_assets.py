import RPi_I2C_driver
import time

rows = [0x80, 0xC0, 0x94, 0xD4]
mylcd = RPi_I2C_driver.lcd()


# functions

def start_screen():
    mylcd.lcd_display_string_pos("KEEP RASPI", 2, 5)
    mylcd.lcd_display_string_pos("TALKING", 3, 6)


def explode():
    try:
        explode_rows = rows.copy()
        explode_rows.reverse()
        while True:
            for index, row in enumerate(explode_rows):
                mylcd.lcd_load_custom_chars(shroom_data_list[index])
                mylcd.lcd_write(row)
                for i in range(5):
                    mylcd.lcd_write_char(i)
                time.sleep(0.15)
                mylcd.lcd_clear()
    except:
        mylcd.lcd_clear()


def countdown(minutes: int, seconds: int):
    try:
        while True:
            # to clear any lingering numbers
            mylcd.lcd_clear()
            mylcd.lcd_display_string_pos(f"{minutes} : {seconds}", 2, 7)
            time.sleep(1)
            seconds -= 1
            if seconds < 0:
                if minutes <= 0:
                    time.sleep(1)
                    explode()
                minutes -= 1
                seconds = 59
    except:
        mylcd.lcd_clear()


# custom chars

# shroom
shroom_top = [
    [
        0b00000,
        0b00000,
        0b00000,
        0b00000,
        0b00001,
        0b00011,
        0b00111,
        0b00011
    ], [
        0b00001,
        0b00111,
        0b01111,
        0b11111,
        0b11111,
        0b11111,
        0b11111,
        0b11111
    ], [
        0b11111,
        0b11111,
        0b11111,
        0b11111,
        0b11111,
        0b11111,
        0b11111,
        0b11111
    ], [
        0b00000,
        0b11000,
        0b11110,
        0b11111,
        0b11111,
        0b11111,
        0b11111,
        0b11111
    ], [
        0b00000,
        0b00000,
        0b00000,
        0b00000,
        0b11000,
        0b11000,
        0b11100,
        0b11000
    ]]
shroom_upper_mid = [
    [
        0b00011,
        0b00011,
        0b00001,
        0b00001,
        0b00000,
        0b00000,
        0b00000,
        0b00000
    ], [
        0b11111,
        0b11111,
        0b11111,
        0b11111,
        0b11111,
        0b01111,
        0b00111,
        0b00011
    ], [
        0b11111,
        0b11111,
        0b11111,
        0b11111,
        0b11111,
        0b11111,
        0b11111,
        0b11111
    ], [
        0b11111,
        0b11111,
        0b11111,
        0b11111,
        0b11111,
        0b11110,
        0b11100,
        0b11000
    ], [
        0b11100,
        0b11100,
        0b11000,
        0b10000,
        0b00000,
        0b00000,
        0b00000,
        0b00000
    ]]
shroom_lower_mid = [
    [
        0b00001,
        0b00011,
        0b00011,
        0b00001,
        0b00000,
        0b00000,
        0b00000,
        0b00000
    ], [
        0b11111,
        0b11111,
        0b11111,
        0b11111,
        0b00111,
        0b00000,
        0b00000,
        0b00001
    ], [
        0b11111,
        0b11111,
        0b11111,
        0b11111,
        0b11111,
        0b01110,
        0b11111,
        0b11111
    ], [
        0b11111,
        0b11111,
        0b11111,
        0b11111,
        0b11110,
        0b00000,
        0b00000,
        0b10000
    ], [
        0b10000,
        0b11000,
        0b11000,
        0b10000,
        0b00000,
        0b00000,
        0b00000,
        0b00000
    ]]
shroom_bot = [
    [
        0b00000,
        0b00000,
        0b00000,
        0b00000,
        0b00000,
        0b00000,
        0b00001,
        0b00111
    ], [
        0b00001,
        0b00000,
        0b00000,
        0b00000,
        0b00000,
        0b00011,
        0b11111,
        0b11111
    ], [
        0b11111,
        0b11111,
        0b01110,
        0b01110,
        0b11111,
        0b11111,
        0b11111,
        0b11111
    ], [
        0b10000,
        0b00000,
        0b00000,
        0b00000,
        0b00000,
        0b11000,
        0b11111,
        0b11111
    ], [
        0b00000,
        0b00000,
        0b00000,
        0b00000,
        0b00000,
        0b00000,
        0b00000,
        0b11110
    ]]

shroom_data_list = [shroom_bot, shroom_lower_mid, shroom_upper_mid, shroom_top]

# hourglass

hourglass_top = [
    [
        0b11111,
        0b11111,
        0b01110,
        0b00100,
        0b01010,
        0b10001,
        0b11111,
        0b00000
    ]]
hourglass_middle = [
    [
        0b11111,
        0b10001,
        0b01110,
        0b00100,
        0b01110,
        0b10001,
        0b11111,
        0b00000
    ]]
hourglass_bot = [
    [
        0b11111,
        0b10001,
        0b01010,
        0b00100,
        0b01110,
        0b11111,
        0b11111,
        0b00000]
]

hourglass_data_list = [hourglass_top, hourglass_middle, hourglass_bot]
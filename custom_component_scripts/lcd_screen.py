import socket
from custom_component_scripts import LCD_16x2_I2C_driver
import time

screen = LCD_16x2_I2C_driver.lcd()

custom_icons = []

icon_empty = [0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0]
icon_success = [0x0, 0x1, 0x3, 0x16, 0x1c, 0x8, 0x0, 0x0]
icon_pca9685 = [0x1f, 0x11, 0x15, 0x15, 0x15, 0x15, 0x11, 0x1f]
icon_gpio = [0x4, 0x4, 0x1f, 0x0, 0x0, 0xe, 0x4, 0x4]
icon_remote_controller = [0x11, 0xa, 0xe, 0xa, 0xa, 0xe, 0xa, 0x11]
icon_temperature = [0x18, 0x18, 0x3, 0x4, 0x4, 0x4, 0x3, 0x0]
icon_problem = [0x0, 0x1b, 0xe, 0x4, 0xe, 0x1b, 0x0, 0x0]
icon_success_reverse = [0x1f, 0x1e, 0x1c, 0x9, 0x3, 0x17, 0x1f]

# There is only memory for 7 in the lcd screen controller
custom_icons.insert(0, icon_empty)
custom_icons.insert(1, icon_success)
custom_icons.insert(2, icon_pca9685)
custom_icons.insert(3, icon_gpio)
custom_icons.insert(4, icon_remote_controller)
custom_icons.insert(5, icon_temperature)
custom_icons.insert(6, icon_problem)
custom_icons.insert(7, icon_success_reverse)

"""
screen.lcd_load_custom_chars(custom_icons)
screen.lcd_write(0x80)
screen.lcd_write_char(0)
screen.lcd_write_char(1)
screen.lcd_write_char(2)
screen.lcd_write_char(3)
screen.lcd_write_char(4)
screen.lcd_write_char(5)
screen.lcd_write_char(6)
screen.lcd_write_char(7)
time.sleep(2)
"""

def get_ip_address():
    ip_address = 'ERROR';
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8",80))
    ip_address = s.getsockname()[0]
    s.close()
    return ip_address


screen.lcd_display_string("SpotMicro AI", 1)

str_pad = " " * 16
display = "Running tests on spot micro" 

for i in range (0, len(display)):
    lcd_text = display[i:(i+16)]
    screen.lcd_display_string(lcd_text,2)
    time.sleep(0.4)
    screen.lcd_display_string(str_pad,2)

screen.lcd_display_string("Testing ..", 2)
time.sleep(2)
screen.lcd_clear()
time.sleep(1)
screen.lcd_display_string("IP Address:", 1)
screen.lcd_display_string(get_ip_address(), 2)
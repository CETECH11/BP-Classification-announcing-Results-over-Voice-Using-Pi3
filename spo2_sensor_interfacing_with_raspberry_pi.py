import RPi.GPIO as GPIO
import time
import board
import digitalio
import adafruit_character_lcd.character_lcd as characterlcd
import max30102
import hrcalc
switch = 16
GPIO.setmode(GPIO.BCM)
GPIO.setup(switch,GPIO.IN)
sensor = max30102.MAX30102()
lcd_columns = 16
lcd_rows = 2

lcd_rs = digitalio.DigitalInOut(board.D26)
lcd_en = digitalio.DigitalInOut(board.D19)
lcd_d7 = digitalio.DigitalInOut(board.D27)
lcd_d6 = digitalio.DigitalInOut(board.D22)
lcd_d5 = digitalio.DigitalInOut(board.D24)
lcd_d4 = digitalio.DigitalInOut(board.D25)
lcd_backlight = digitalio.DigitalInOut(board.D4)

# Initialise the lcd class
lcd = characterlcd.Character_LCD_Mono(
    lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight
)
while True:
    
    if GPIO.input(switch) == 0:
        red, ir = sensor.read_sequential()
        hrcalc.calc_hr_and_spo2(ir,red)
    else:
        lcd.clear()
        lcd.cursor_position(0, 0)
        lcd.message ="Place the finger"
        lcd.cursor_position(0, 1)
        lcd.message ="on the sensor"
        time.sleep(0.5)

import RPi.GPIO as GPIO
import time
import board
import digitalio
import adafruit_character_lcd.character_lcd as characterlcd
from smbus2 import SMBus
from mlx90614 import MLX90614
import os
import time
from pygame import mixer
from gtts import gTTS
import os
from os import path
from pydub import AudioSegment

lcd_columns = 16
lcd_rows = 2
irt = 6 # Proximity Sensor Pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(irt,GPIO.IN)# Proximity Sensor Pin
bus = SMBus(1)
sensor = MLX90614(bus, address=0x5A)
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

file = open('IRTEMP_readings.txt', 'w')
file.write(' Your BODY TEMPERATURE Details Are As Follows.\n')
mixer.init()

while True:   
    if GPIO.input(irt) == 1:
        print (sensor.get_obj_temp())
        temp_c = sensor.get_obj_temp()
        a = int(temp_c)
        lcd.clear()
        lcd.cursor_position(0, 0)# coloumn,row
        lcd.message = 'Temp = %.1f C' % temp_c
        file.write('TEMPERATURE:' + str(a) +'. Degree celcius')
        time.sleep(1)
        file.close()
        f = open("/home/pi/IRTEMP_readings.txt", "r")
        p = (f.read())
        print(p)
        tts = gTTS(p, lang='en', tld='com.au')
        tts.save('IR.mp3')
        input_file = "IR.mp3"
        output_file = "IR.wav"
        sound = AudioSegment.from_mp3(input_file)
        sound.export(output_file, format="wav")
        sound = mixer.Sound("/home/pi/IR.wav")
        sound.play()
        time.sleep(5)
    else:
        lcd.clear()
        lcd.cursor_position(0, 0)# coloumn,row
        lcd.message = "Place hand"
        lcd.cursor_position(0, 1)# coloumn,row
        lcd.message = "near the sensor"
        print("please place hand near the sensor")
    time.sleep(1)

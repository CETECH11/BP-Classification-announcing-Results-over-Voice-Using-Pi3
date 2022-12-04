import serial, time
import RPi.GPIO as GPIO
import re
import time
import board
import digitalio
import adafruit_character_lcd.character_lcd as characterlcd
import os
import time
from pygame import mixer
from gtts import gTTS
import os
from os import path
from pydub import AudioSegment

bp = 23# BP sensor Status 
lcd_columns = 16 #LCD Display Size
lcd_rows = 2

# Raspberry Pi Pin Config For Interfacing LCD:
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

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(bp,GPIO.IN)
ser = serial.Serial("/dev/ttyS0",9600)# The Bp sensor Baud Rate
ser.bytesize = serial.EIGHTBITS #number of bits per bytes
ser.parity = serial.PARITY_NONE #set parity check: no parity
ser.stopbits = serial.STOPBITS_ONE #number of stop bits
ser.timeout = 1            #non-block read
ser.xonxoff = False     #disable software flow control
ser.rtscts = False     #disable hardware (RTS/CTS) flow control
ser.dsrdtr = False       #disable hardware (DSR/DTR) flow control
file = open('BP_sensor_readings.txt', 'w') # creating A text file in folder
file.write(' Your Blood Pressure Details Are As Follows\n')
mixer.init()

while True:
    response = ser.readline().decode('ASCII')
    x = len(response)# checking the avalible bytes in the serial data
    if x >= 10:
        print("systolic,diastolic,Pulse")
        print(response)
        y = response.split(',') #spliting the each bytes with comma
        print(y)
        z = re.findall('[0-9]+', response) # extracting each byte
        print(z)
        a = [z] # creating extracted each byte in a array
        b = int(z[0]) # first byte in a array (Systollic)
        bb = z[0]
        c = int(z[1]) # second byte in a array (diastollic)
        cc = z[1]
        d = int(z[2])# third byte in a array (pulse)
        dd = z[2]
        print("Systolic :", b)
        print("Diastollic :",c)
        print("Pulse:" , d)
        lcd.cursor_position(0, 0)# coloumn,row
        lcd.message = "SYS:"
        lcd.cursor_position(4, 0)# coloumn,row
        lcd.message = bb
        lcd.cursor_position(8, 0)# coloumn,row
        lcd.message = "DIA:"
        lcd.cursor_position(12, 0)# coloumn,row
        lcd.message = cc
        lcd.cursor_position(0, 1)# coloumn,row
        lcd.message = "Pulse:"
        lcd.cursor_position(6, 1)# coloumn,row
        lcd.message = dd
        if b < 90 and c < 60:
            #print('Hypotension')
            file.write('Systollic:' + str(b) + ' . Diastolic:'+ str(c)+' . Pulse rate:' + str(d)+'. ,You have Hypotension')
            time.sleep(1)
            file.close()
            print('Hypotension')
        elif b > 120 and b < 139 and c > 80 and c < 90:
            #print('Prehypertension')
            file.write('Systolic:' + str(b) + ' . Diastolic:'+ str(c)+' . Pulse rate:' + str(d)+'. ,You have Prehypertension' + '\n')
            time.sleep(1)
            file.close()
            print('Prehypertension')
        elif b > 140 and b < 159 and c > 90 and c < 99:
            #print('stage 1 Hypertension')
            file.write('Systolic:' + str(b) + ' . Diastolic:'+ str(c)+' . Pulse rate:' + str(d)+'. ,You Have stage 1 Hypertension' + '\n')
            time.sleep(1)
            file.close()
            print('stage 1 Hypertension')
        elif b > 160 and b < 179 and c > 100 and c < 109:
            #print('stage 2 Hypertension')
            file.write('Systolic:' + str(b) + ' . Diastolic:'+ str(c)+' . Pulse rate:' + str(d)+'. ,You Have stage 2 Hypertension' + '\n')
            time.sleep(1)
            file.close()
            print('stage 2 Hypertension')
        elif b > 180 and c > 110:
            #print('Hypertensive Crisis')
            file.write('Systolic:' + str(b) + ' . Diastolic:'+ str(c)+' . Pulse rate:' + str(d)+'. ,You Have Hypertensive Crisis' + '\n')
            time.sleep(1)
            file.close()
            print('Hypertensive Crisis')
        else:
            file.write('Systolic:' + str(b) + ' . Diastolic:'+ str(c)+' . Pulse rate:' + str(d)+'. ,Normal Blood Pressure' + '\n')
            time.sleep(1)
            file.close()
            print('Normal_blood_pressure')
            
        print("file written")
        lcd.clear()
        lcd.cursor_position(0, 0)# coloumn,row
        lcd.message = "Details Saved In"
        lcd.cursor_position(0, 1)# coloumn,row
        lcd.message = "Text Format"
        f = open("/home/pi/BP_sensor_readings.txt", "r")# Opening File To read The data
        p = (f.read())
        print(p)#Display the data saved in the text file
        tts = gTTS(p, lang='en', tld='com.au')# GTTS Text Input For Converting Text To Voice
        tts.save('BP.mp3')#Saving The Voice file recieved from GTTS in MP3 Format
        input_file = "BP.mp3"# Converrting the MP3 FILE INTO .WAV Format
        output_file = "BP.wav"#Saving the WAV Converted File 
        sound = AudioSegment.from_mp3(input_file)
        sound.export(output_file, format="wav")
        sound = mixer.Sound("/home/pi/BP.wav")#Locating the Wav File 
        sound.play()#Play The audio
        time.sleep(5)
        



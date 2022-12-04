# BP-Classification-announcing-Results-over-Voice-Using-Pi3

![alt text](https://hackster.imgix.net/uploads/attachments/1529215/_b03FCvwpDG.blob?auto=compress%2Cformat&w=900&h=675&fit=min)

This project that we have made this time is capable of Classification Of Blood Pressure, Spo2, Body Temperature Monitoring, and announcing sensor Results Over The Voice Using Raspberry Pi. In this Upgrade Project, I Have provided the following parameters:-
1. SpO2 Monitoring
2. IR Temperature Sensor
3. LCD Display
4. Voice Broadcasting
5. Data Saving For Future ML Training
I added the basic details of different Classifications of blood pressure for adults (18 years and older). I will utilize the same chart to create this Project.

I have used Python 3 for writing code for this project. I have used Python Idle3 to write and Run The code. By default, Raspberry Pi Will have Thonny IDE. If you want to use the same IDE as mine you need to download it by typing the following command in the Raspberry Pi terminal.

sudo apt-get install idle3

The BP Sensor Exchanges the Data Over the UART Terminal in Half Duplex Mode. This sensor Communicates the Raspberry Pi by 9600 Baud Rate. To receive the data In the Raspberry Pi We need to Configure UART Channel in the Raspberry Pi.

![alt text](https://hackster.imgix.net/uploads/attachments/1529970/bp_sensor_Ap0MofdJVY.jpg?auto=compress%2Cformat&w=740&h=555&fit=max)

PL011 UART is an ARM-based UART. This UART has better throughput than mini UART. In Raspberry Pi 3, mini UART is used for Linux console output whereas PL011 is connected to the Onboard Bluetooth module. And in the other versions of Raspberry Pi, PL011 is used for Linux console output.

Mini UART uses the frequency which is linked to the core frequency of the GPU. So as the GPU core frequency changes, the frequency of UART will also change which in turn will change the baud rate for UART. This makes the mini UART unstable which may lead to data loss or corruption. To make mini UART stable, fix the core frequency. mini UART doesn’t have parity support.

The PL011 is a stable and high-performance UART. For better and more effective communication use PL011 UART instead of mini UART.

It is recommended to enable the UART of Raspberry Pi for serial communication. Otherwise, we cannot communicate serially as UART ports are used for Linux console output and Bluetooth module.

![alt text](https://hackster.imgix.net/uploads/attachments/1529340/image_MNpQbOTwpj.png?auto=compress%2Cformat&w=740&h=555&fit=max)

gTTS (Google Text-to-Speech), a Python library and CLI tool to interface with Google Translate's text-to-speech API. Write spoken mp3 data to a file, a file-like object (byte string) for further audio manipulation, or stdout. Or simply pre-generate Google Translate TTS request URLs to feed to an external program.
Run The Below command in the Raspberry Pi terminal To download the gTTS.

pip install gTTS

To interface the SpO2 With the raspberry pi we use I2C Communication, Since We already Installed All the Required Configuration For I2C, LCD There is no need to enable Them Again. You Just Need To add the Library Called max30102, This Library is modified for the Raspberry Pi based on My requirements.

![alt text](https://hackster.imgix.net/uploads/attachments/1518136/8_tJuwoRM3dI.JPG?auto=compress%2Cformat&w=740&h=555&fit=max)

You must check out [PCBWAY](https://www.pcbway.com/) for ordering PCBs online for cheap!

You get 10 good-quality PCBs manufactured and shipped to your doorstep for cheap. You will also get a discount on shipping on your first order. Upload your Gerber files onto PCBWAY to get them manufactured with good quality and quick turnaround time. [PCBWay](https://www.pcbway.com/) now could provide a complete product solution, from design to enclosure production. Check out their online Gerber viewer function. With reward points, you can get free stuff from their gift shop.

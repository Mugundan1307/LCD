# LCD

'''*sudo apt install -y python3-pip python3-pil python3-numpy git*'''

'''*sudo vim /boot/config.txt*''' (OR) '''*sudo vim /boot/firmware/config.txt*'''
gpio=6,19,5,26,13,21,20,16=pu


*sudo raspi-config*
Interface Options -> SPI -> Enable
*sudo reboot*

*ls -l /dev/spidev*

*grep -E "spi|gpio" /boot/config.txt*

*sudo apt install python3-rpi-lgpio -y*

*cd ~
git clone https://github.com/kudesnick/1.44inch-LCD-HAT-Code.git
cd 1.44inch-LCD-HAT-Code/python*

*sudo python3 main.py*

# Keys and Joystick

*sudo apt install -y python3-rpi.gpio*

*vim ~/test_joystick_keys.py*

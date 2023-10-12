from machine import Pin, I2C
from dht import *
from ssd1306 import *
from ds3231_gen import *
from sdcard import *

# temp sensor
led = Pin(25, Pin.OUT)
sensor = DHT22(Pin(2)) 

# display
i2c_port = 0
i2c_sda = 16
i2c_scl = 17

i2c_0 = I2C(i2c_port, scl=Pin(i2c_scl), sda=Pin(i2c_sda))

WIDTH = 128
HEIGHT = 64

display = SSD1306_I2C(WIDTH, HEIGHT, i2c_0)

# RTC
i2c_port = 1
i2c_sda = 14
i2c_scl = 15

i2c_1 = I2C(i2c_port, scl=Pin(i2c_scl), sda=Pin(i2c_sda))

rtc = DS3231(i2c_1)


# sd card
SPI = 1
SCK = 10
MOSI = 11
MISO = 8
CS = 9

sd = SDCard(SPI, SCK, MOSI, MISO, CS, baudrate=1000000, led=25)

# write test file
with open("/sd/test01.txt", "w") as file:
    file.write("Hello, SD World!\r\n")
    file.write("This is a test\r\n")

# read test file
with open("/sd/test01.txt", "r") as file:
    data = file.read()
    print(data)



# # text is 7 pixels high
# # 16 characters per line
# # 8 lines
# #             0000000000000000
# display.text('temp    humidity', 0, 0, 1)
# display.text(f'{temp}C      {hum:.0f}', 0, 20, 1)
# #             0000000000000000
# display.show()



#while True:
#   t = rtc.get_time()[:6]
#
#   sensor.measure()
#   temp = sensor.temperature()
#   hum = sensor.humidity()
#   
#   f = open("utc-log-pico1.csv", 'a')
#   f.write(f"{t[0]%100}{t[1]:02}{t[2]:02}t{t[3]:02}{t[4]:02}{t[5]:02},{temp},{hum:.0f}\n")
#   f.close()
#
#   display.text('temp    humidity', 0, 0, 1)
#   display.text(f'{temp}C     {hum:.0f}%', 0, 18, 1)
#   display.text(f'     {t[3]:02}:{t[4]:02}', 0, 36, 1)
#   display.text(f'   {t[2]:02}/{t[1]:02}/{t[0]}', 0, 54, 1)
#   display.show()
#   display.fill(0)
#
#   led(0)
#   time.sleep(30)
#   led(1)

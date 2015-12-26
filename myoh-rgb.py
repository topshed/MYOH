from gpiozero import RGBLED
from time import sleep

led = RGBLED(22,27,17)

led.on()
sleep(0.5)
led.off()
led.red = 1
sleep(0.5)
led.red =0
led.green=1
sleep(0.5)
led.green = 0
led.blue = 1
sleep(0.5)
led.blue=0



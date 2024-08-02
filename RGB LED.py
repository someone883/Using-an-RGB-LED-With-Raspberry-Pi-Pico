#importing libraries
from machine import Pin,PWM
import time
#making variables
redPin=14
greenPin=13
bluePin=15
redLED=PWM(Pin(redPin))
greenLED=PWM(Pin(greenPin))
blueLED=PWM(Pin(bluePin))
redLED.freq(1000)
redLED.duty_u16(0)
greenLED.freq(1000)
greenLED.duty_u16(0)
blueLED.freq(1000)
blueLED.duty_u16(0)
while True:
    redBright=65550 #<-- change value for different brightness
    greenBright=0 #<-- make higher for this color to turn on
    blueBright=0#<-- make higher for this color to turn on
    #makes LEDs do their job
    redLED.duty_u16(redBright)
    greenLED.duty_u16(greenBright)
    blueLED.duty_u16(blueBright)
    time.sleep_ms(100)
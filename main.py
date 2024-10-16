import board
from digitalio import DigitalInOut, Direction
from analogio import AnalogIn
from time import sleep

# setup pins
microphone = AnalogIn(board.IO1)

status = DigitalInOut(board.IO17)
status.direction = Direction.OUTPUT

led_pins = [
    board.IO21,
    board.IO26, # type: ignore
    board.IO47,
    board.IO33,
    board.IO34,
    board.IO48,
    board.IO35,
    board.IO36,
    board.IO37,
    board.IO38,
    board.IO39
]

leds = [DigitalInOut(pin) for pin in led_pins]

for led in leds:
    led.direction = Direction.OUTPUT


# Helper function that uses microphone value to light up LED
def lightUp(volume, maxVolume, numberLeds):
    lighting = maxVolume/numberLeds
    return min(numberLeds, int(volume/lighting))
    # return int ((volume/maxVolume) * numberLeds)


# main loop
while True:
    volume = microphone.value

    print(volume)

    ledsOn = lightUp(volume, 45000, len(leds)) # lights up led based on microphone

    # Turning on leds
    for i in range(len(leds)):
        leds[i].value = i < ledsOn # This should turn leds on

    leds[0].value = not leds[0].value
    leds[1].value = not leds[0].value

    sleep(0.1)

    # instead of blinking,
    # how can you make the LEDs
    # turn on like a volume meter?

import board
import neopixel_spi
import time
import busio

spi = busio.SPI(board.SCK_1, MOSI=board.MOSI_1, MISO=board.MISO_1)

def setup(br):
    global pixels
    pixels = neopixel_spi.NeoPixel_SPI(spi, 8, brightness=br)

# Turn off all the leds
def leds_off():
    global pixels
    pixels.deinit()

# Blink frequency and timer
BLINK = .1
t1 = time.monotonic()

# Needed variables
shift_changed = 10

def action(rpm, STEP, END):
    global pixels
    global shift_changed
    global t1
    shift = (END - rpm) // STEP + 1
    # Blinker
    if rpm > END + STEP:
        if t1 + BLINK < time.monotonic():
            pixels.fill(0x00ffff)
        if t1 + BLINK * 2 < time.monotonic():
            pixels.deinit()
            t1 = time.monotonic()
    # If shift light step is exceeded
    elif shift_changed != shift:
        # LED steps control
        print("Shift:", shift)
        print("Shift_changed:", shift_changed)
        if shift <= 3:
            pixels[0] = (0x00ff00)
            pixels[7] = (0x00ff00)
        else:
            pixels[0] = (0x000000)
            pixels[7] = (0x000000)

        if shift <= 2:
            pixels[1] = (0x00ff00)
            pixels[6] = (0x00ff00)
        else:
            pixels[1] = (0x000000)
            pixels[6] = (0x000000)

        if shift <= 1:
            pixels[2] = (0xffff00)
            pixels[5] = (0xffff00)
        else:
            pixels[2] = (0x000000)
            pixels[5] = (0x000000)

        if shift <= 0:
            pixels[3] = (0xff0000)
            pixels[4] = (0xff0000)
        else:
            pixels[3] = (0x000000)
            pixels[4] = (0x000000)

    # Save the new state
    shift_changed = shift

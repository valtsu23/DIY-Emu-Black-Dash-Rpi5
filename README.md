# DIY-Emu-Black-Dash-Rpi5
No longer supported. Checkout new version: https://github.com/valtsu23/DIY-Emu-Black-Dash-Rpi5-V2

Raspberry pi 5 4Gb based digital dash working with Ecumaster Emu Black

### Based on: https://github.com/valtsu23/DIY-Emu-Black-Dash
- Setup is pretty close to above. Excpect: install the Neopixel SPI library, setup the rtc battery (guide on Raspberry Pi homepage) and don't overclock. 
- Hardware remains the same, expect the rtc, which is Rpi5:s internal with official rtc battery

### Software differences
- HardwarePWM uses different channel and different chip (wiring remains the same)
- Standard Adafruit Neopixel library won't work with Rpi5, so I'm using Neopixel SPI library: https://github.com/adafruit/Adafruit_CircuitPython_NeoPixel_SPI
- Because of the Neopixel SPI library usage there is no need to run the code with Sudo
- You also need to add this line to the config.txt:
`dtoverlay=spi1-1cs,cs0_pin=16`

### Performance
- Python program is pretty light (cpu usage usually less than 10% and memory usage less than 200Mb on the whole system)
- Boot time is under 15s, so few seconds better than with Rpi 4
- Active cooler was needed (using the official Rpi 5 cooler)

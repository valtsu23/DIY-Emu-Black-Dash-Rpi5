# DIY-Emu-Black-Dash-Rpi5
Raspberry pi 5 based digital dash working with Ecumaster Emu Black

### Based on: https://github.com/valtsu23/DIY-Emu-Black-Dash
- Setup is pretty close to above. Excpect: install the Neopixel SPI library, setup the rtc battery (guide on Raspberry Pi homepage) and don't overclock. 
- Hardware remains the same, expect the rtc, which is Rpi5:s internal with official rtc battery

### Software differences
- HardwarePWM uses different channel and different chip (wiring remains the same)
- Standard Adafruit Neopixel library won't work with Rpi5, so I'm using Neopixel SPI library: https://github.com/adafruit/Adafruit_CircuitPython_NeoPixel_SPI

### Performance
- Boot time is under 15s, so few seconds better than with Rpi 4
- Active cooler was needed (using the official Rpi 5 cooler)

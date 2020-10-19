import time
import board
import neopixel_spi as neopixel
 
NUM_PIXELS = 8
PIXEL_ORDER = neopixel.GRB
COLORS = (0xFF0000, 0x00FF00, 0x0000FF, 0xFFFFFF, 0x31E3DF, 0x4b09dd)
DELAY = 0.1
 
spi = board.SPI()
 
pixels = neopixel.NeoPixel_SPI(
    spi, NUM_PIXELS, pixel_order=PIXEL_ORDER, auto_write=False
)


for i in range(10):
    pixels[0] = 0xFF0000
    pixels[1] = 0xFF0000
    pixels[2] = 0xFF0000
    pixels[3] = 0xFF0000
    pixels.show()
    time.sleep(DELAY)
    pixels.fill(0)
    pixels[4] = 0x0000FF
    pixels[5] = 0x0000FF
    pixels[6] = 0x0000FF
    pixels[7] = 0x0000FF    
    pixels.show()
    time.sleep(DELAY)
    pixels.fill(0)

for i in range(1):
    for color in COLORS:
        for i in range(NUM_PIXELS):
            pixels[i] = color
            pixels.show()
            time.sleep(DELAY)
            pixels.fill(0)

pixels.fill(0xFF0000)
pixels.show()
time.sleep(1)
pixels.fill(0x7CFC00)
pixels.show()
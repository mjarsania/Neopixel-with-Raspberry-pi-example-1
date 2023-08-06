import time
from rpi_ws281x import PixelStrip, Color

# LED strip configuration:
LED_COUNT = 16        # Number of LED pixels.
LED_PIN = 18          # GPIO pin connected to the pixels (PWM pin).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10          # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False    # True to invert the signal (when using NPN transistor level shift)

# Create NeoPixel object
strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)

# Initialize the library
strip.begin()

# Set all LEDs to red color
for i in range(LED_COUNT):
    strip.setPixelColor(i, Color(255, 0, 0))

# Update the LED strip to show the set colors
strip.show()

# Wait for a few seconds before turning off the LEDs
time.sleep(5)

# Turn off all LEDs
for i in range(LED_COUNT):
    strip.setPixelColor(i, Color(0, 0, 0))
strip.show()   

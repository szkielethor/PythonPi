import spidev
import time

spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 5000000

while True:
    print spi.xfer2([0x20,0x32])
    time.sleep(0.3)

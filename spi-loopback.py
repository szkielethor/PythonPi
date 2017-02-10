import spidev
import time
spi = spidev.SpiDev()
spi.open(0,1)
while True:
    resp = spi.xfer2([0x00])
    print resp[0]
    time.sleep(0.1)

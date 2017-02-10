import spidev
import time
spi = spidev.SpiDev()

x = spi.readbytes(20)

k=0
for i in x:
    print(k, hex(i), i)
    k = k+1

import spi
spi.openSPI(speed=1000000, mode=0)
print spi.transfer((0x00)(0x01)
spi.closeSPI()


import spidev
import time

spi = spidev.SpiDev() # tworzy obiekt spi
spi.open(0,1)         # otwiera port spi 0,
                      # urzdzenie na linii selekcyjnej 1
try:
    while True:
        resp = spi.xfer2([0xAA, 0x29, 0x2B, 0x2D])  # transfer 1 bajta
        time.sleep(0.9)           # pol sekundy spania
  #      odczyt = spi.readbytes(16)
   #     print odczyt
        print resp
  #      odczytane = spi.read(1)
  #      print odczytane[0]
    #koniec while
except KeyboardInterrupt:   # CTLR+C kto wcisn, przeto
                            # zamykamy port przed wyjciem
    spi.close()
# koniec bloku try

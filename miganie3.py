import RPi.GPIO as piny
import time
#Ustawiam wyjście na 11stym pinie (17 GPIO):
piny.setup(11, piny.OUT)
#piny.setmode(piny.BOARD)
#Miganie wuchte razy:
for i in range (1,100000):
    piny.output(11,True)
    time.sleep(0.500)
    piny.output(11,False)
    time.sleep(0.200)
piny.cleanup()

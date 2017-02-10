#coding: utf-8
import RPi.GPIO as piny
import time
#blinking funcion
def blink(pin):
    piny.output(pin,True)
    time.sleep(0.5)
    piny.output(pin,False)
    time.sleep(0.99)
    return
#piny.setmode(piny.BOARD)
#set up GPIO output channel
piny.setup(11, piny.OUT)
#blink GPIO15 50 times
powtorzenia = input("Ile razy mrugnac, ciulu? ")
print("Chcesz, zebym mignal " + str(powtorzenia)
      + " razy. Mam to w tyle. Ciulu")
for i in range (0, 100):
    piny.output(11,1)
    time.sleep(0.05)
    piny.output(11,0)
    time.sleep(0.15)
    # blink(11)
#piny.cleanup()

#!/usr/bin/python3
# spiTest.py
import wiringpi2
print("Weź podłącz pętelkę - połącz razem MISO i MOSI (piny 19 i 21")
print("[Naciśnij Enter jak ogarniesz]")
input()
wiringpi2.wiringPiSPISetup(1,500000)
buffer=str.encode("HELLO")
print("Buffer sent %s" % buffer)
wiringpi2.wiringPiSPIDataRW(1,buffer)
print("Buffer received %s" % buffer)
print("Weź odłącz pętlę")
print("[Jak ogarniesz naduś enter]")
input()
buffer = str.encode("Hello")
print("Buffer sent %s" % buffer)
wiringpi2.wiringPiSPIDataRW(1,buffer)
print("Buffer received %s" %buffer)
#End

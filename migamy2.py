import RPi.GPIO as OneToRuleThemAll #rzondzem
import time
OneToRuleThemAll.setup(11,OneToRuleThemAll.OUT)
#ma wychodzic sygnal z tego
# n=10 #niech to sie stanie konfigurowalne
licznik=1
while (licznik<8):
    OneToRuleThemAll.output(11,True)
    jasneSpanie=1-1/licznik+0.005
    print "jasneSpanie wynosi teraz:"
    print jasneSpanie
    time.sleep(1)
    OneToRuleThemAll.output(11,False)
    float ciemneSpanie
    ciemneSpanie = 1/licznik
    print "ciemneSpanie wynosie teraz:"
    print ciemneSpanie
    time.sleep(1)
    print licznik
    licznik=licznik+1
OneToRuleThemAll.cleanup()
    

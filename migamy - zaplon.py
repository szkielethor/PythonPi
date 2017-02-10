import RPi.GPIO as piny

piny.setmode(piny.BOARD) #tą numerację pinów wole

piny.setup (11, piny.OUT) #ustawiam 11stkę jako wyjście

piny.output(11, True)   #daję na wyjście 11stki logiczną 1
                          #a że mam tam diodę, to sie zapala
piny.cleanup()

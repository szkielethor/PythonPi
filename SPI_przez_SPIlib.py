# -*- coding: utf-8 -*-
"""
This example prints acceleration values from a ST LIS302DL 3d accelerometer.
"""


from spi import SPIDev, spi_transfer
import struct

# write and read operations are defined in the datasheet, those are convenience
# functions to do a read or write command. Probably other devices use different 
# rules

def write(addr, data, auto_increment=False):
    """ prepare the command to write a register from the accel"""
    a_i = int(auto_increment) << 6
    out = chr(addr | a_i) + data
    return out


def read(addr, auto_increment=False):
    """ prepare the command to read a register from the accel"""
    out = chr(addr | 1 << 7 | int(auto_increment) << 6)
    return out

#setup device
s = SPIDev('/dev/spidev0.0')

cmd = read(0xf)  # identify chip command
# build a 1 byte write transfer (identify chip)
cmdtransfer, cmdbuf, _ = spi_transfer(cmd, readlen=0)
#build a 1 byte read transfer (reply from the chip)
valtransfer, _, rbuf = spi_transfer(None, readlen=1)
# actually do the transfer
s.do_transfers([cmdtransfer, valtransfer])
assert rbuf.raw == ';', "device not connected?"

cmd = write(0x20, chr(0b0100 << 4 | 0b0111))  # control register, power on
cmdtransfer, cmdbuf, _ = spi_transfer(cmd, readlen=0)
s.do_transfers([cmdtransfer])

cmd = write(0x21, chr(0b0001 << 4 | 0b0000))  # highpass
cmdtransfer, cmdbuf, _ = spi_transfer(cmd, readlen=0)
s.do_transfers([cmdtransfer])

cmdx = read(0x29)  # read x axis command
# prepare transfer
cmdxt, cmdbufx, _ = spi_transfer(cmdx, readlen=0)

cmdy = read(0x2b)  # read y axis
cmdyt, cmdbufy, _ = spi_transfer(cmdy, readlen=0)

cmdz = read(0x2d)  # read z axis
cmdzt, cmdbufz, _ = spi_transfer(cmdz, readlen=0)

cmdstatus = read(0x27)
cmdstatust, cmdbufstat, _ = spi_transfer(cmdstatus, readlen=0)

valtransfer, _, rbuf = spi_transfer(None, readlen=1)
while True:
    s.do_transfers([cmdstatust, valtransfer])
    ready = ord(rbuf.raw[0]) & 1 << 3
    if not ready:
        continue
    s.do_transfers([cmdxt, valtransfer])
    x = struct.unpack("b", rbuf.raw)[0]
    s.do_transfers([cmdyt, valtransfer])
    y = struct.unpack("b", rbuf.raw)[0]
    s.do_transfers([cmdzt, valtransfer])
    z = struct.unpack("b", rbuf.raw)[0]
    v = int((x ** 2 + y ** 2 + z ** 2) ** (0.5))
    print "x:{0:4} y:{1:4} z:{2:4}, v:{3:4}".format(x, y, z, v)

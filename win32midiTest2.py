# Copyright 2004-2023 Soon Wah Chua
from win32midi2 import *
import time
stout = midiStreamOpen(0, 0, 0)
print(midiOutGetErrorTextA(stout[0]))
midiStreamRestart(stout[1])
b = chr(0x90) + chr(0x3C) + chr(0x40)
hdr = MIDIHDR()
hdr.lpData = b
hdr.dwBufferLength = 3
hdr.dwRecordedLength = 0
hdr.dwFlags = 0
midiOutPrepareHeader(stout[1], hdr)
print('Sending long stream message')
print(midiStreamOut(stout[1], hdr))
print(midiOutUnprepareHeader(stout[1], hdr))
time.sleep(2)
result = midiStreamClose(stout[1])
print(midiOutGetErrorTextA(result))

from win32midi2 import *
import time
print 'Num of Input/Output Devices',midiInGetNumDevs(),'/',midiOutGetNumDevs()
r,h=midiOutOpen(0,0,0,0)
midiOutReset(h)
print 'Output Volume', hex(midiOutGetVolume(h)[1])
midiOutSetVolume(h,0xffffffffL)
print 'Output Volume', hex(midiOutGetVolume(h)[1])
midiOutShortMsg(h,0x90|(60<<8)|120<<16)
midiOutShortMsg(h,0x90|(61<<8)|120<<16)
time.sleep(1)
midiOutSetVolume(h,0x77007700L)
print 'Output Volume', hex(midiOutGetVolume(h)[1])
midiOutShortMsg(h,0x90|(62<<8)|120<<16)
midiOutShortMsg(h,0x90|(63<<8)|120<<16)
time.sleep(2)
cap = MIDIOUTCAPSA()
midiOutGetDevCapsA(0,cap)

print 'Output Device capabilities'
print cap.wMid, cap.wPid, cap.vDriverVersion, cap.szPname
print cap.wTechnology, cap.wVoices, cap.wNotes, cap.wChannelMask, cap.dwSupport

print 'Input Device capabilities'
icap = MIDIINCAPSA()
midiInGetDevCapsA(0,icap)
print icap.wMid, icap.wPid, icap.vDriverVersion, icap.szPname, icap.dwSupport
hdr = MIDIHDR()
b = chr(0x90)+chr(0x3C)+chr(0x40)
hdr.lpData = b
hdr.dwBufferLength = 3
hdr.dwRecordedLength = 0
hdr.dwFlags = 0
midiOutPrepareHeader(h,hdr)
print 'Sending long message'
midiOutLongMsg(h,hdr)
midiOutUnprepareHeader(h,hdr)
time.sleep(2)
print midiOutClose(h),'Closed'
#for i in range(10):
#  print midiOutGetErrorTextA(i), midiInGetErrorTextA(i)
stout = midiStreamOpen(0,0,0)
print midiOutGetErrorTextA(stout[0])
midiStreamRestart(stout[1])
hdr = MIDIHDR()
hdr.lpData = b
hdr.dwBufferLength = 3
hdr.dwRecordedLength = 0
hdr.dwFlags = 0
midiOutPrepareHeader(Stream2MIDI(stout[1]),hdr)
print 'Sending long stream message'
print midiStreamOut(stout[1],hdr)
print midiOutUnprepareHeader(Stream2MIDI(stout[1]),hdr)
time.sleep(2)
result = midiStreamClose(stout[1])
print midiOutGetErrorTextA(result)

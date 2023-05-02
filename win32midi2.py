import ctypes
from ctypes import byref
from ctypes.wintypes import *

_wm = ctypes.WinDLL('winmm')


def midiOutOpen(dev=0, a=0, b=0, c=0):
    h = HANDLE()
    r = _wm.midiOutOpen(byref(h), dev, 0, 0, 0)
    return r, h


def midiOutClose(h):
    return _wm.midiOutClose(h)


def midiOutShortMsg(h, dwMsg):
    return _wm.midiOutShortMsg(h, dwMsg)


def midiOutSetVolume(h, dwVol):
    return _wm.midiOutSetVolume(h, dwVol)


def midiOutGetVolume(h):
    dwVol = ctypes.c_long()
    r = _wm.midiOutGetVolume(h, byref(dwVol))
    return r, dwVol.value


midiOutGetNumDevs = _wm.midiOutGetNumDevs
midiInGetNumDevs = _wm.midiInGetNumDevs
midiOutReset = _wm.midiOutReset


CHAR = ctypes.c_char
UINT = ctypes.c_uint

# ctypes.create_string_buffer(127)
# CHARBUF = ctypes.create_string_buffer()


class MIDIOUTCAPSA(ctypes.Structure):
    _fields_ = [("wMid", WORD),
                ("wPid", WORD),
                ("vDriverVersion", UINT),
                # ("szPname", CHAR*32),
                ("_szPname", ctypes.c_byte * 32),
                ("wTechnology", WORD),
                ("wVoices", WORD),
                ("wNotes", WORD),
                ("wChannelMask", WORD),
                ("dwSupport", DWORD),
                ]

    def __getattr__(self, name):
        if name == 'szPname':
            for i in range(32):
                if self._szPname[i] == 0:
                    EOStr = i
                    break
            return ''.join(map(chr, self._szPname[:EOStr]))
        else:
            return ctypes.Structure.name


def midiOutGetDevCapsA(uDeviceID, lpMidiOutCaps):
    return _wm.midiOutGetDevCapsA(uDeviceID, byref(lpMidiOutCaps),
                                  ctypes.sizeof(lpMidiOutCaps))


class MIDIINCAPSA(ctypes.Structure):
    _fields_ = [("wMid", WORD),
                ("wPid", WORD),
                ("vDriverVersion", UINT),
                ("_szPname", ctypes.c_byte * 32),
                ("dwSupport", DWORD),
                ]

    def __getattr__(self, name):
        if name == 'szPname':
            for i in range(32):
                if self._szPname[i] == 0:
                    EOStr = i
                    break
            return ''.join(map(chr, self._szPname[:EOStr]))
        else:
            return ctypes.Structure.name


def midiInGetDevCapsA(uDeviceID, lpMidiOutCaps):
    return _wm.midiInGetDevCapsA(uDeviceID, byref(lpMidiOutCaps),
                                 ctypes.sizeof(lpMidiOutCaps))


DWORD_PTR = ctypes.POINTER(DWORD)


class MIDIHDR(ctypes.Structure):
    pass


MIDIHDR._fields_ = [("lpData", LPSTR),
                    ("dwBufferLength", DWORD),
                    ("dwBytesRecorded", DWORD),
                    ("dwUser", DWORD_PTR),
                    ("lpNext", ctypes.POINTER(MIDIHDR)),
                    ("dwFlags", DWORD),
                    ("reserved", DWORD),
                    ("dwOffset", DWORD),
                    ("dwReserved", DWORD_PTR * 4),
                    ]


def midiOutPrepareHeader(hmo, lpMidiOutHdr):
    return _wm.midiOutPrepareHeader(hmo, byref(lpMidiOutHdr),
                                    ctypes.sizeof(lpMidiOutHdr))


def midiOutLongMsg(hmo, lpMidiOutHdr):
    return _wm.midiOutLongMsg(hmo, byref(lpMidiOutHdr),
                              ctypes.sizeof(lpMidiOutHdr))


def midiOutUnprepareHeader(hmo, lpMidiOutHdr):
    return _wm.midiOutUnprepareHeader(hmo, byref(lpMidiOutHdr),
                                      ctypes.sizeof(lpMidiOutHdr))


class MIDISTRMBUFFER(ctypes.Structure):
    _fields_ = [("dwVersion", DWORD),
                ("dwMid", DWORD),
                ("dwOEMVersion", DWORD),
                ]


LPHMIDISTRM = ctypes.POINTER(MIDISTRMBUFFER)


def midiStreamOpen(puDeviceID, cMidi, dwCallback, dwInstance=0, fdwOpen=0):
    lphStream = LPHMIDISTRM()
    return _wm.midiStreamOpen(lphStream, puDeviceID, cMidi, dwCallback,
                              dwInstance, fdwOpen), lphStream


def midiOutGetErrorTextA(mmrError):
    lpText = ctypes.create_string_buffer(64)
    return _wm.midiOutGetErrorTextA(mmrError, lpText, 64)


midiStreamRestart = _wm.midiStreamRestart


def midiStreamOut(hMidiStream, lpMidiHdr):
    return _wm.midiStreamOut(hMidiStream, byref(lpMidiHdr),
                             ctypes.sizeof(lpMidiHdr))


midiStreamClose = _wm.midiStreamClose

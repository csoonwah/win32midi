from ctypes import *


class _U(Structure):
    _fields_ = [('HighPart', c_long),
                ('LowPart', c_long)
                ]


class LARGE_INTEGER(Union):
    _fields_ = [('QuadPart', c_longlong),
                ('u', _U)
                ]
    _anonymous_ = ('u',)


kdll = windll.kernel32

li = LARGE_INTEGER()

kdll.QueryPerformanceFrequency(pointer(li))
FREQ = li.QuadPart


def waitTime(t):
    kdll.QueryPerformanceCounter(pointer(li))
    s = li.QuadPart
    while (li.QuadPart - s) < (t * FREQ):
        kdll.QueryPerformanceCounter(pointer(li))

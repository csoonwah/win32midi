# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _win32midi

def _swig_setattr(self,class_type,name,value):
    if (name == "this"):
        if isinstance(value, class_type):
            self.__dict__[name] = value.this
            if hasattr(value,"thisown"): self.__dict__["thisown"] = value.thisown
            del value.thisown
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    self.__dict__[name] = value

def _swig_getattr(self,class_type,name):
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError,name

import types
try:
    _object = types.ObjectType
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0
del types


WINVER = _win32midi.WINVER

Stream2MIDI = _win32midi.Stream2MIDI

Event2String = _win32midi.Event2String
MAXPNAMELEN = _win32midi.MAXPNAMELEN
MAXERRORLENGTH = _win32midi.MAXERRORLENGTH
MAX_JOYSTICKOEMVXDNAME = _win32midi.MAX_JOYSTICKOEMVXDNAME
MMSYSERR_BASE = _win32midi.MMSYSERR_BASE
WAVERR_BASE = _win32midi.WAVERR_BASE
MIDIERR_BASE = _win32midi.MIDIERR_BASE
TIMERR_BASE = _win32midi.TIMERR_BASE
JOYERR_BASE = _win32midi.JOYERR_BASE
MCIERR_BASE = _win32midi.MCIERR_BASE
MIXERR_BASE = _win32midi.MIXERR_BASE
MCI_STRING_OFFSET = _win32midi.MCI_STRING_OFFSET
MCI_VD_OFFSET = _win32midi.MCI_VD_OFFSET
MCI_CD_OFFSET = _win32midi.MCI_CD_OFFSET
MCI_WAVE_OFFSET = _win32midi.MCI_WAVE_OFFSET
MCI_SEQ_OFFSET = _win32midi.MCI_SEQ_OFFSET
MMSYSERR_NOERROR = _win32midi.MMSYSERR_NOERROR
MMSYSERR_ERROR = _win32midi.MMSYSERR_ERROR
MMSYSERR_BADDEVICEID = _win32midi.MMSYSERR_BADDEVICEID
MMSYSERR_NOTENABLED = _win32midi.MMSYSERR_NOTENABLED
MMSYSERR_ALLOCATED = _win32midi.MMSYSERR_ALLOCATED
MMSYSERR_INVALHANDLE = _win32midi.MMSYSERR_INVALHANDLE
MMSYSERR_NODRIVER = _win32midi.MMSYSERR_NODRIVER
MMSYSERR_NOMEM = _win32midi.MMSYSERR_NOMEM
MMSYSERR_NOTSUPPORTED = _win32midi.MMSYSERR_NOTSUPPORTED
MMSYSERR_BADERRNUM = _win32midi.MMSYSERR_BADERRNUM
MMSYSERR_INVALFLAG = _win32midi.MMSYSERR_INVALFLAG
MMSYSERR_INVALPARAM = _win32midi.MMSYSERR_INVALPARAM
MMSYSERR_HANDLEBUSY = _win32midi.MMSYSERR_HANDLEBUSY
MMSYSERR_INVALIDALIAS = _win32midi.MMSYSERR_INVALIDALIAS
MMSYSERR_BADDB = _win32midi.MMSYSERR_BADDB
MMSYSERR_KEYNOTFOUND = _win32midi.MMSYSERR_KEYNOTFOUND
MMSYSERR_READERROR = _win32midi.MMSYSERR_READERROR
MMSYSERR_WRITEERROR = _win32midi.MMSYSERR_WRITEERROR
MMSYSERR_DELETEERROR = _win32midi.MMSYSERR_DELETEERROR
MMSYSERR_VALNOTFOUND = _win32midi.MMSYSERR_VALNOTFOUND
MMSYSERR_NODRIVERCB = _win32midi.MMSYSERR_NODRIVERCB
MMSYSERR_MOREDATA = _win32midi.MMSYSERR_MOREDATA
MMSYSERR_LASTERROR = _win32midi.MMSYSERR_LASTERROR
class HDRVR__(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, HDRVR__, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, HDRVR__, name)
    def __repr__(self):
        return "<C HDRVR__ instance at %s>" % (self.this,)
    __swig_setmethods__["unused"] = _win32midi.HDRVR___unused_set
    __swig_getmethods__["unused"] = _win32midi.HDRVR___unused_get
    if _newclass:unused = property(_win32midi.HDRVR___unused_get, _win32midi.HDRVR___unused_set)
    def __init__(self, *args):
        _swig_setattr(self, HDRVR__, 'this', _win32midi.new_HDRVR__(*args))
        _swig_setattr(self, HDRVR__, 'thisown', 1)
    def __del__(self, destroy=_win32midi.delete_HDRVR__):
        try:
            if self.thisown: destroy(self)
        except: pass

class HDRVR__Ptr(HDRVR__):
    def __init__(self, this):
        _swig_setattr(self, HDRVR__, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, HDRVR__, 'thisown', 0)
        _swig_setattr(self, HDRVR__,self.__class__,HDRVR__)
_win32midi.HDRVR___swigregister(HDRVR__Ptr)

MIDIERR_UNPREPARED = _win32midi.MIDIERR_UNPREPARED
MIDIERR_STILLPLAYING = _win32midi.MIDIERR_STILLPLAYING
MIDIERR_NOMAP = _win32midi.MIDIERR_NOMAP
MIDIERR_NOTREADY = _win32midi.MIDIERR_NOTREADY
MIDIERR_NODEVICE = _win32midi.MIDIERR_NODEVICE
MIDIERR_INVALIDSETUP = _win32midi.MIDIERR_INVALIDSETUP
MIDIERR_BADOPENMODE = _win32midi.MIDIERR_BADOPENMODE
MIDIERR_DONT_CONTINUE = _win32midi.MIDIERR_DONT_CONTINUE
MIDIERR_LASTERROR = _win32midi.MIDIERR_LASTERROR
class HMIDI__(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, HMIDI__, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, HMIDI__, name)
    def __repr__(self):
        return "<C HMIDI__ instance at %s>" % (self.this,)
    __swig_setmethods__["unused"] = _win32midi.HMIDI___unused_set
    __swig_getmethods__["unused"] = _win32midi.HMIDI___unused_get
    if _newclass:unused = property(_win32midi.HMIDI___unused_get, _win32midi.HMIDI___unused_set)
    def __init__(self, *args):
        _swig_setattr(self, HMIDI__, 'this', _win32midi.new_HMIDI__(*args))
        _swig_setattr(self, HMIDI__, 'thisown', 1)
    def __del__(self, destroy=_win32midi.delete_HMIDI__):
        try:
            if self.thisown: destroy(self)
        except: pass

class HMIDI__Ptr(HMIDI__):
    def __init__(self, this):
        _swig_setattr(self, HMIDI__, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, HMIDI__, 'thisown', 0)
        _swig_setattr(self, HMIDI__,self.__class__,HMIDI__)
_win32midi.HMIDI___swigregister(HMIDI__Ptr)

class HMIDIIN__(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, HMIDIIN__, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, HMIDIIN__, name)
    def __repr__(self):
        return "<C HMIDIIN__ instance at %s>" % (self.this,)
    __swig_setmethods__["unused"] = _win32midi.HMIDIIN___unused_set
    __swig_getmethods__["unused"] = _win32midi.HMIDIIN___unused_get
    if _newclass:unused = property(_win32midi.HMIDIIN___unused_get, _win32midi.HMIDIIN___unused_set)
    def __init__(self, *args):
        _swig_setattr(self, HMIDIIN__, 'this', _win32midi.new_HMIDIIN__(*args))
        _swig_setattr(self, HMIDIIN__, 'thisown', 1)
    def __del__(self, destroy=_win32midi.delete_HMIDIIN__):
        try:
            if self.thisown: destroy(self)
        except: pass

class HMIDIIN__Ptr(HMIDIIN__):
    def __init__(self, this):
        _swig_setattr(self, HMIDIIN__, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, HMIDIIN__, 'thisown', 0)
        _swig_setattr(self, HMIDIIN__,self.__class__,HMIDIIN__)
_win32midi.HMIDIIN___swigregister(HMIDIIN__Ptr)

class HMIDIOUT__(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, HMIDIOUT__, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, HMIDIOUT__, name)
    def __repr__(self):
        return "<C HMIDIOUT__ instance at %s>" % (self.this,)
    __swig_setmethods__["unused"] = _win32midi.HMIDIOUT___unused_set
    __swig_getmethods__["unused"] = _win32midi.HMIDIOUT___unused_get
    if _newclass:unused = property(_win32midi.HMIDIOUT___unused_get, _win32midi.HMIDIOUT___unused_set)
    def __init__(self, *args):
        _swig_setattr(self, HMIDIOUT__, 'this', _win32midi.new_HMIDIOUT__(*args))
        _swig_setattr(self, HMIDIOUT__, 'thisown', 1)
    def __del__(self, destroy=_win32midi.delete_HMIDIOUT__):
        try:
            if self.thisown: destroy(self)
        except: pass

class HMIDIOUT__Ptr(HMIDIOUT__):
    def __init__(self, this):
        _swig_setattr(self, HMIDIOUT__, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, HMIDIOUT__, 'thisown', 0)
        _swig_setattr(self, HMIDIOUT__,self.__class__,HMIDIOUT__)
_win32midi.HMIDIOUT___swigregister(HMIDIOUT__Ptr)

class HMIDISTRM__(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, HMIDISTRM__, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, HMIDISTRM__, name)
    def __repr__(self):
        return "<C HMIDISTRM__ instance at %s>" % (self.this,)
    __swig_setmethods__["unused"] = _win32midi.HMIDISTRM___unused_set
    __swig_getmethods__["unused"] = _win32midi.HMIDISTRM___unused_get
    if _newclass:unused = property(_win32midi.HMIDISTRM___unused_get, _win32midi.HMIDISTRM___unused_set)
    def __init__(self, *args):
        _swig_setattr(self, HMIDISTRM__, 'this', _win32midi.new_HMIDISTRM__(*args))
        _swig_setattr(self, HMIDISTRM__, 'thisown', 1)
    def __del__(self, destroy=_win32midi.delete_HMIDISTRM__):
        try:
            if self.thisown: destroy(self)
        except: pass

class HMIDISTRM__Ptr(HMIDISTRM__):
    def __init__(self, this):
        _swig_setattr(self, HMIDISTRM__, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, HMIDISTRM__, 'thisown', 0)
        _swig_setattr(self, HMIDISTRM__,self.__class__,HMIDISTRM__)
_win32midi.HMIDISTRM___swigregister(HMIDISTRM__Ptr)

MIDIPATCHSIZE = _win32midi.MIDIPATCHSIZE
MIDI_IO_STATUS = _win32midi.MIDI_IO_STATUS
MIDI_CACHE_ALL = _win32midi.MIDI_CACHE_ALL
MIDI_CACHE_BESTFIT = _win32midi.MIDI_CACHE_BESTFIT
MIDI_CACHE_QUERY = _win32midi.MIDI_CACHE_QUERY
MIDI_UNCACHE = _win32midi.MIDI_UNCACHE
class MIDIOUTCAPSA(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, MIDIOUTCAPSA, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, MIDIOUTCAPSA, name)
    def __repr__(self):
        return "<C MIDIOUTCAPSA instance at %s>" % (self.this,)
    __swig_setmethods__["wMid"] = _win32midi.MIDIOUTCAPSA_wMid_set
    __swig_getmethods__["wMid"] = _win32midi.MIDIOUTCAPSA_wMid_get
    if _newclass:wMid = property(_win32midi.MIDIOUTCAPSA_wMid_get, _win32midi.MIDIOUTCAPSA_wMid_set)
    __swig_setmethods__["wPid"] = _win32midi.MIDIOUTCAPSA_wPid_set
    __swig_getmethods__["wPid"] = _win32midi.MIDIOUTCAPSA_wPid_get
    if _newclass:wPid = property(_win32midi.MIDIOUTCAPSA_wPid_get, _win32midi.MIDIOUTCAPSA_wPid_set)
    __swig_setmethods__["vDriverVersion"] = _win32midi.MIDIOUTCAPSA_vDriverVersion_set
    __swig_getmethods__["vDriverVersion"] = _win32midi.MIDIOUTCAPSA_vDriverVersion_get
    if _newclass:vDriverVersion = property(_win32midi.MIDIOUTCAPSA_vDriverVersion_get, _win32midi.MIDIOUTCAPSA_vDriverVersion_set)
    __swig_setmethods__["szPname"] = _win32midi.MIDIOUTCAPSA_szPname_set
    __swig_getmethods__["szPname"] = _win32midi.MIDIOUTCAPSA_szPname_get
    if _newclass:szPname = property(_win32midi.MIDIOUTCAPSA_szPname_get, _win32midi.MIDIOUTCAPSA_szPname_set)
    __swig_setmethods__["wTechnology"] = _win32midi.MIDIOUTCAPSA_wTechnology_set
    __swig_getmethods__["wTechnology"] = _win32midi.MIDIOUTCAPSA_wTechnology_get
    if _newclass:wTechnology = property(_win32midi.MIDIOUTCAPSA_wTechnology_get, _win32midi.MIDIOUTCAPSA_wTechnology_set)
    __swig_setmethods__["wVoices"] = _win32midi.MIDIOUTCAPSA_wVoices_set
    __swig_getmethods__["wVoices"] = _win32midi.MIDIOUTCAPSA_wVoices_get
    if _newclass:wVoices = property(_win32midi.MIDIOUTCAPSA_wVoices_get, _win32midi.MIDIOUTCAPSA_wVoices_set)
    __swig_setmethods__["wNotes"] = _win32midi.MIDIOUTCAPSA_wNotes_set
    __swig_getmethods__["wNotes"] = _win32midi.MIDIOUTCAPSA_wNotes_get
    if _newclass:wNotes = property(_win32midi.MIDIOUTCAPSA_wNotes_get, _win32midi.MIDIOUTCAPSA_wNotes_set)
    __swig_setmethods__["wChannelMask"] = _win32midi.MIDIOUTCAPSA_wChannelMask_set
    __swig_getmethods__["wChannelMask"] = _win32midi.MIDIOUTCAPSA_wChannelMask_get
    if _newclass:wChannelMask = property(_win32midi.MIDIOUTCAPSA_wChannelMask_get, _win32midi.MIDIOUTCAPSA_wChannelMask_set)
    __swig_setmethods__["dwSupport"] = _win32midi.MIDIOUTCAPSA_dwSupport_set
    __swig_getmethods__["dwSupport"] = _win32midi.MIDIOUTCAPSA_dwSupport_get
    if _newclass:dwSupport = property(_win32midi.MIDIOUTCAPSA_dwSupport_get, _win32midi.MIDIOUTCAPSA_dwSupport_set)
    def __init__(self, *args):
        _swig_setattr(self, MIDIOUTCAPSA, 'this', _win32midi.new_MIDIOUTCAPSA(*args))
        _swig_setattr(self, MIDIOUTCAPSA, 'thisown', 1)
    def __del__(self, destroy=_win32midi.delete_MIDIOUTCAPSA):
        try:
            if self.thisown: destroy(self)
        except: pass

class MIDIOUTCAPSAPtr(MIDIOUTCAPSA):
    def __init__(self, this):
        _swig_setattr(self, MIDIOUTCAPSA, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, MIDIOUTCAPSA, 'thisown', 0)
        _swig_setattr(self, MIDIOUTCAPSA,self.__class__,MIDIOUTCAPSA)
_win32midi.MIDIOUTCAPSA_swigregister(MIDIOUTCAPSAPtr)

class MIDIOUTCAPSW(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, MIDIOUTCAPSW, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, MIDIOUTCAPSW, name)
    def __repr__(self):
        return "<C MIDIOUTCAPSW instance at %s>" % (self.this,)
    __swig_setmethods__["wMid"] = _win32midi.MIDIOUTCAPSW_wMid_set
    __swig_getmethods__["wMid"] = _win32midi.MIDIOUTCAPSW_wMid_get
    if _newclass:wMid = property(_win32midi.MIDIOUTCAPSW_wMid_get, _win32midi.MIDIOUTCAPSW_wMid_set)
    __swig_setmethods__["wPid"] = _win32midi.MIDIOUTCAPSW_wPid_set
    __swig_getmethods__["wPid"] = _win32midi.MIDIOUTCAPSW_wPid_get
    if _newclass:wPid = property(_win32midi.MIDIOUTCAPSW_wPid_get, _win32midi.MIDIOUTCAPSW_wPid_set)
    __swig_setmethods__["vDriverVersion"] = _win32midi.MIDIOUTCAPSW_vDriverVersion_set
    __swig_getmethods__["vDriverVersion"] = _win32midi.MIDIOUTCAPSW_vDriverVersion_get
    if _newclass:vDriverVersion = property(_win32midi.MIDIOUTCAPSW_vDriverVersion_get, _win32midi.MIDIOUTCAPSW_vDriverVersion_set)
    __swig_setmethods__["szPname"] = _win32midi.MIDIOUTCAPSW_szPname_set
    __swig_getmethods__["szPname"] = _win32midi.MIDIOUTCAPSW_szPname_get
    if _newclass:szPname = property(_win32midi.MIDIOUTCAPSW_szPname_get, _win32midi.MIDIOUTCAPSW_szPname_set)
    __swig_setmethods__["wTechnology"] = _win32midi.MIDIOUTCAPSW_wTechnology_set
    __swig_getmethods__["wTechnology"] = _win32midi.MIDIOUTCAPSW_wTechnology_get
    if _newclass:wTechnology = property(_win32midi.MIDIOUTCAPSW_wTechnology_get, _win32midi.MIDIOUTCAPSW_wTechnology_set)
    __swig_setmethods__["wVoices"] = _win32midi.MIDIOUTCAPSW_wVoices_set
    __swig_getmethods__["wVoices"] = _win32midi.MIDIOUTCAPSW_wVoices_get
    if _newclass:wVoices = property(_win32midi.MIDIOUTCAPSW_wVoices_get, _win32midi.MIDIOUTCAPSW_wVoices_set)
    __swig_setmethods__["wNotes"] = _win32midi.MIDIOUTCAPSW_wNotes_set
    __swig_getmethods__["wNotes"] = _win32midi.MIDIOUTCAPSW_wNotes_get
    if _newclass:wNotes = property(_win32midi.MIDIOUTCAPSW_wNotes_get, _win32midi.MIDIOUTCAPSW_wNotes_set)
    __swig_setmethods__["wChannelMask"] = _win32midi.MIDIOUTCAPSW_wChannelMask_set
    __swig_getmethods__["wChannelMask"] = _win32midi.MIDIOUTCAPSW_wChannelMask_get
    if _newclass:wChannelMask = property(_win32midi.MIDIOUTCAPSW_wChannelMask_get, _win32midi.MIDIOUTCAPSW_wChannelMask_set)
    __swig_setmethods__["dwSupport"] = _win32midi.MIDIOUTCAPSW_dwSupport_set
    __swig_getmethods__["dwSupport"] = _win32midi.MIDIOUTCAPSW_dwSupport_get
    if _newclass:dwSupport = property(_win32midi.MIDIOUTCAPSW_dwSupport_get, _win32midi.MIDIOUTCAPSW_dwSupport_set)
    def __init__(self, *args):
        _swig_setattr(self, MIDIOUTCAPSW, 'this', _win32midi.new_MIDIOUTCAPSW(*args))
        _swig_setattr(self, MIDIOUTCAPSW, 'thisown', 1)
    def __del__(self, destroy=_win32midi.delete_MIDIOUTCAPSW):
        try:
            if self.thisown: destroy(self)
        except: pass

class MIDIOUTCAPSWPtr(MIDIOUTCAPSW):
    def __init__(self, this):
        _swig_setattr(self, MIDIOUTCAPSW, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, MIDIOUTCAPSW, 'thisown', 0)
        _swig_setattr(self, MIDIOUTCAPSW,self.__class__,MIDIOUTCAPSW)
_win32midi.MIDIOUTCAPSW_swigregister(MIDIOUTCAPSWPtr)

class MIDIOUTCAPS2A(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, MIDIOUTCAPS2A, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, MIDIOUTCAPS2A, name)
    def __repr__(self):
        return "<C MIDIOUTCAPS2A instance at %s>" % (self.this,)
    __swig_setmethods__["wMid"] = _win32midi.MIDIOUTCAPS2A_wMid_set
    __swig_getmethods__["wMid"] = _win32midi.MIDIOUTCAPS2A_wMid_get
    if _newclass:wMid = property(_win32midi.MIDIOUTCAPS2A_wMid_get, _win32midi.MIDIOUTCAPS2A_wMid_set)
    __swig_setmethods__["wPid"] = _win32midi.MIDIOUTCAPS2A_wPid_set
    __swig_getmethods__["wPid"] = _win32midi.MIDIOUTCAPS2A_wPid_get
    if _newclass:wPid = property(_win32midi.MIDIOUTCAPS2A_wPid_get, _win32midi.MIDIOUTCAPS2A_wPid_set)
    __swig_setmethods__["vDriverVersion"] = _win32midi.MIDIOUTCAPS2A_vDriverVersion_set
    __swig_getmethods__["vDriverVersion"] = _win32midi.MIDIOUTCAPS2A_vDriverVersion_get
    if _newclass:vDriverVersion = property(_win32midi.MIDIOUTCAPS2A_vDriverVersion_get, _win32midi.MIDIOUTCAPS2A_vDriverVersion_set)
    __swig_setmethods__["szPname"] = _win32midi.MIDIOUTCAPS2A_szPname_set
    __swig_getmethods__["szPname"] = _win32midi.MIDIOUTCAPS2A_szPname_get
    if _newclass:szPname = property(_win32midi.MIDIOUTCAPS2A_szPname_get, _win32midi.MIDIOUTCAPS2A_szPname_set)
    __swig_setmethods__["wTechnology"] = _win32midi.MIDIOUTCAPS2A_wTechnology_set
    __swig_getmethods__["wTechnology"] = _win32midi.MIDIOUTCAPS2A_wTechnology_get
    if _newclass:wTechnology = property(_win32midi.MIDIOUTCAPS2A_wTechnology_get, _win32midi.MIDIOUTCAPS2A_wTechnology_set)
    __swig_setmethods__["wVoices"] = _win32midi.MIDIOUTCAPS2A_wVoices_set
    __swig_getmethods__["wVoices"] = _win32midi.MIDIOUTCAPS2A_wVoices_get
    if _newclass:wVoices = property(_win32midi.MIDIOUTCAPS2A_wVoices_get, _win32midi.MIDIOUTCAPS2A_wVoices_set)
    __swig_setmethods__["wNotes"] = _win32midi.MIDIOUTCAPS2A_wNotes_set
    __swig_getmethods__["wNotes"] = _win32midi.MIDIOUTCAPS2A_wNotes_get
    if _newclass:wNotes = property(_win32midi.MIDIOUTCAPS2A_wNotes_get, _win32midi.MIDIOUTCAPS2A_wNotes_set)
    __swig_setmethods__["wChannelMask"] = _win32midi.MIDIOUTCAPS2A_wChannelMask_set
    __swig_getmethods__["wChannelMask"] = _win32midi.MIDIOUTCAPS2A_wChannelMask_get
    if _newclass:wChannelMask = property(_win32midi.MIDIOUTCAPS2A_wChannelMask_get, _win32midi.MIDIOUTCAPS2A_wChannelMask_set)
    __swig_setmethods__["dwSupport"] = _win32midi.MIDIOUTCAPS2A_dwSupport_set
    __swig_getmethods__["dwSupport"] = _win32midi.MIDIOUTCAPS2A_dwSupport_get
    if _newclass:dwSupport = property(_win32midi.MIDIOUTCAPS2A_dwSupport_get, _win32midi.MIDIOUTCAPS2A_dwSupport_set)
    __swig_setmethods__["ManufacturerGuid"] = _win32midi.MIDIOUTCAPS2A_ManufacturerGuid_set
    __swig_getmethods__["ManufacturerGuid"] = _win32midi.MIDIOUTCAPS2A_ManufacturerGuid_get
    if _newclass:ManufacturerGuid = property(_win32midi.MIDIOUTCAPS2A_ManufacturerGuid_get, _win32midi.MIDIOUTCAPS2A_ManufacturerGuid_set)
    __swig_setmethods__["ProductGuid"] = _win32midi.MIDIOUTCAPS2A_ProductGuid_set
    __swig_getmethods__["ProductGuid"] = _win32midi.MIDIOUTCAPS2A_ProductGuid_get
    if _newclass:ProductGuid = property(_win32midi.MIDIOUTCAPS2A_ProductGuid_get, _win32midi.MIDIOUTCAPS2A_ProductGuid_set)
    __swig_setmethods__["NameGuid"] = _win32midi.MIDIOUTCAPS2A_NameGuid_set
    __swig_getmethods__["NameGuid"] = _win32midi.MIDIOUTCAPS2A_NameGuid_get
    if _newclass:NameGuid = property(_win32midi.MIDIOUTCAPS2A_NameGuid_get, _win32midi.MIDIOUTCAPS2A_NameGuid_set)
    def __init__(self, *args):
        _swig_setattr(self, MIDIOUTCAPS2A, 'this', _win32midi.new_MIDIOUTCAPS2A(*args))
        _swig_setattr(self, MIDIOUTCAPS2A, 'thisown', 1)
    def __del__(self, destroy=_win32midi.delete_MIDIOUTCAPS2A):
        try:
            if self.thisown: destroy(self)
        except: pass

class MIDIOUTCAPS2APtr(MIDIOUTCAPS2A):
    def __init__(self, this):
        _swig_setattr(self, MIDIOUTCAPS2A, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, MIDIOUTCAPS2A, 'thisown', 0)
        _swig_setattr(self, MIDIOUTCAPS2A,self.__class__,MIDIOUTCAPS2A)
_win32midi.MIDIOUTCAPS2A_swigregister(MIDIOUTCAPS2APtr)

class MIDIOUTCAPS2W(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, MIDIOUTCAPS2W, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, MIDIOUTCAPS2W, name)
    def __repr__(self):
        return "<C MIDIOUTCAPS2W instance at %s>" % (self.this,)
    __swig_setmethods__["wMid"] = _win32midi.MIDIOUTCAPS2W_wMid_set
    __swig_getmethods__["wMid"] = _win32midi.MIDIOUTCAPS2W_wMid_get
    if _newclass:wMid = property(_win32midi.MIDIOUTCAPS2W_wMid_get, _win32midi.MIDIOUTCAPS2W_wMid_set)
    __swig_setmethods__["wPid"] = _win32midi.MIDIOUTCAPS2W_wPid_set
    __swig_getmethods__["wPid"] = _win32midi.MIDIOUTCAPS2W_wPid_get
    if _newclass:wPid = property(_win32midi.MIDIOUTCAPS2W_wPid_get, _win32midi.MIDIOUTCAPS2W_wPid_set)
    __swig_setmethods__["vDriverVersion"] = _win32midi.MIDIOUTCAPS2W_vDriverVersion_set
    __swig_getmethods__["vDriverVersion"] = _win32midi.MIDIOUTCAPS2W_vDriverVersion_get
    if _newclass:vDriverVersion = property(_win32midi.MIDIOUTCAPS2W_vDriverVersion_get, _win32midi.MIDIOUTCAPS2W_vDriverVersion_set)
    __swig_setmethods__["szPname"] = _win32midi.MIDIOUTCAPS2W_szPname_set
    __swig_getmethods__["szPname"] = _win32midi.MIDIOUTCAPS2W_szPname_get
    if _newclass:szPname = property(_win32midi.MIDIOUTCAPS2W_szPname_get, _win32midi.MIDIOUTCAPS2W_szPname_set)
    __swig_setmethods__["wTechnology"] = _win32midi.MIDIOUTCAPS2W_wTechnology_set
    __swig_getmethods__["wTechnology"] = _win32midi.MIDIOUTCAPS2W_wTechnology_get
    if _newclass:wTechnology = property(_win32midi.MIDIOUTCAPS2W_wTechnology_get, _win32midi.MIDIOUTCAPS2W_wTechnology_set)
    __swig_setmethods__["wVoices"] = _win32midi.MIDIOUTCAPS2W_wVoices_set
    __swig_getmethods__["wVoices"] = _win32midi.MIDIOUTCAPS2W_wVoices_get
    if _newclass:wVoices = property(_win32midi.MIDIOUTCAPS2W_wVoices_get, _win32midi.MIDIOUTCAPS2W_wVoices_set)
    __swig_setmethods__["wNotes"] = _win32midi.MIDIOUTCAPS2W_wNotes_set
    __swig_getmethods__["wNotes"] = _win32midi.MIDIOUTCAPS2W_wNotes_get
    if _newclass:wNotes = property(_win32midi.MIDIOUTCAPS2W_wNotes_get, _win32midi.MIDIOUTCAPS2W_wNotes_set)
    __swig_setmethods__["wChannelMask"] = _win32midi.MIDIOUTCAPS2W_wChannelMask_set
    __swig_getmethods__["wChannelMask"] = _win32midi.MIDIOUTCAPS2W_wChannelMask_get
    if _newclass:wChannelMask = property(_win32midi.MIDIOUTCAPS2W_wChannelMask_get, _win32midi.MIDIOUTCAPS2W_wChannelMask_set)
    __swig_setmethods__["dwSupport"] = _win32midi.MIDIOUTCAPS2W_dwSupport_set
    __swig_getmethods__["dwSupport"] = _win32midi.MIDIOUTCAPS2W_dwSupport_get
    if _newclass:dwSupport = property(_win32midi.MIDIOUTCAPS2W_dwSupport_get, _win32midi.MIDIOUTCAPS2W_dwSupport_set)
    __swig_setmethods__["ManufacturerGuid"] = _win32midi.MIDIOUTCAPS2W_ManufacturerGuid_set
    __swig_getmethods__["ManufacturerGuid"] = _win32midi.MIDIOUTCAPS2W_ManufacturerGuid_get
    if _newclass:ManufacturerGuid = property(_win32midi.MIDIOUTCAPS2W_ManufacturerGuid_get, _win32midi.MIDIOUTCAPS2W_ManufacturerGuid_set)
    __swig_setmethods__["ProductGuid"] = _win32midi.MIDIOUTCAPS2W_ProductGuid_set
    __swig_getmethods__["ProductGuid"] = _win32midi.MIDIOUTCAPS2W_ProductGuid_get
    if _newclass:ProductGuid = property(_win32midi.MIDIOUTCAPS2W_ProductGuid_get, _win32midi.MIDIOUTCAPS2W_ProductGuid_set)
    __swig_setmethods__["NameGuid"] = _win32midi.MIDIOUTCAPS2W_NameGuid_set
    __swig_getmethods__["NameGuid"] = _win32midi.MIDIOUTCAPS2W_NameGuid_get
    if _newclass:NameGuid = property(_win32midi.MIDIOUTCAPS2W_NameGuid_get, _win32midi.MIDIOUTCAPS2W_NameGuid_set)
    def __init__(self, *args):
        _swig_setattr(self, MIDIOUTCAPS2W, 'this', _win32midi.new_MIDIOUTCAPS2W(*args))
        _swig_setattr(self, MIDIOUTCAPS2W, 'thisown', 1)
    def __del__(self, destroy=_win32midi.delete_MIDIOUTCAPS2W):
        try:
            if self.thisown: destroy(self)
        except: pass

class MIDIOUTCAPS2WPtr(MIDIOUTCAPS2W):
    def __init__(self, this):
        _swig_setattr(self, MIDIOUTCAPS2W, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, MIDIOUTCAPS2W, 'thisown', 0)
        _swig_setattr(self, MIDIOUTCAPS2W,self.__class__,MIDIOUTCAPS2W)
_win32midi.MIDIOUTCAPS2W_swigregister(MIDIOUTCAPS2WPtr)

MOD_MIDIPORT = _win32midi.MOD_MIDIPORT
MOD_SYNTH = _win32midi.MOD_SYNTH
MOD_SQSYNTH = _win32midi.MOD_SQSYNTH
MOD_FMSYNTH = _win32midi.MOD_FMSYNTH
MOD_MAPPER = _win32midi.MOD_MAPPER
MOD_WAVETABLE = _win32midi.MOD_WAVETABLE
MOD_SWSYNTH = _win32midi.MOD_SWSYNTH
MIDICAPS_VOLUME = _win32midi.MIDICAPS_VOLUME
MIDICAPS_LRVOLUME = _win32midi.MIDICAPS_LRVOLUME
MIDICAPS_CACHE = _win32midi.MIDICAPS_CACHE
MIDICAPS_STREAM = _win32midi.MIDICAPS_STREAM
class MIDIINCAPSA(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, MIDIINCAPSA, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, MIDIINCAPSA, name)
    def __repr__(self):
        return "<C MIDIINCAPSA instance at %s>" % (self.this,)
    __swig_setmethods__["wMid"] = _win32midi.MIDIINCAPSA_wMid_set
    __swig_getmethods__["wMid"] = _win32midi.MIDIINCAPSA_wMid_get
    if _newclass:wMid = property(_win32midi.MIDIINCAPSA_wMid_get, _win32midi.MIDIINCAPSA_wMid_set)
    __swig_setmethods__["wPid"] = _win32midi.MIDIINCAPSA_wPid_set
    __swig_getmethods__["wPid"] = _win32midi.MIDIINCAPSA_wPid_get
    if _newclass:wPid = property(_win32midi.MIDIINCAPSA_wPid_get, _win32midi.MIDIINCAPSA_wPid_set)
    __swig_setmethods__["vDriverVersion"] = _win32midi.MIDIINCAPSA_vDriverVersion_set
    __swig_getmethods__["vDriverVersion"] = _win32midi.MIDIINCAPSA_vDriverVersion_get
    if _newclass:vDriverVersion = property(_win32midi.MIDIINCAPSA_vDriverVersion_get, _win32midi.MIDIINCAPSA_vDriverVersion_set)
    __swig_setmethods__["szPname"] = _win32midi.MIDIINCAPSA_szPname_set
    __swig_getmethods__["szPname"] = _win32midi.MIDIINCAPSA_szPname_get
    if _newclass:szPname = property(_win32midi.MIDIINCAPSA_szPname_get, _win32midi.MIDIINCAPSA_szPname_set)
    __swig_setmethods__["dwSupport"] = _win32midi.MIDIINCAPSA_dwSupport_set
    __swig_getmethods__["dwSupport"] = _win32midi.MIDIINCAPSA_dwSupport_get
    if _newclass:dwSupport = property(_win32midi.MIDIINCAPSA_dwSupport_get, _win32midi.MIDIINCAPSA_dwSupport_set)
    def __init__(self, *args):
        _swig_setattr(self, MIDIINCAPSA, 'this', _win32midi.new_MIDIINCAPSA(*args))
        _swig_setattr(self, MIDIINCAPSA, 'thisown', 1)
    def __del__(self, destroy=_win32midi.delete_MIDIINCAPSA):
        try:
            if self.thisown: destroy(self)
        except: pass

class MIDIINCAPSAPtr(MIDIINCAPSA):
    def __init__(self, this):
        _swig_setattr(self, MIDIINCAPSA, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, MIDIINCAPSA, 'thisown', 0)
        _swig_setattr(self, MIDIINCAPSA,self.__class__,MIDIINCAPSA)
_win32midi.MIDIINCAPSA_swigregister(MIDIINCAPSAPtr)

class MIDIINCAPSW(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, MIDIINCAPSW, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, MIDIINCAPSW, name)
    def __repr__(self):
        return "<C MIDIINCAPSW instance at %s>" % (self.this,)
    __swig_setmethods__["wMid"] = _win32midi.MIDIINCAPSW_wMid_set
    __swig_getmethods__["wMid"] = _win32midi.MIDIINCAPSW_wMid_get
    if _newclass:wMid = property(_win32midi.MIDIINCAPSW_wMid_get, _win32midi.MIDIINCAPSW_wMid_set)
    __swig_setmethods__["wPid"] = _win32midi.MIDIINCAPSW_wPid_set
    __swig_getmethods__["wPid"] = _win32midi.MIDIINCAPSW_wPid_get
    if _newclass:wPid = property(_win32midi.MIDIINCAPSW_wPid_get, _win32midi.MIDIINCAPSW_wPid_set)
    __swig_setmethods__["vDriverVersion"] = _win32midi.MIDIINCAPSW_vDriverVersion_set
    __swig_getmethods__["vDriverVersion"] = _win32midi.MIDIINCAPSW_vDriverVersion_get
    if _newclass:vDriverVersion = property(_win32midi.MIDIINCAPSW_vDriverVersion_get, _win32midi.MIDIINCAPSW_vDriverVersion_set)
    __swig_setmethods__["szPname"] = _win32midi.MIDIINCAPSW_szPname_set
    __swig_getmethods__["szPname"] = _win32midi.MIDIINCAPSW_szPname_get
    if _newclass:szPname = property(_win32midi.MIDIINCAPSW_szPname_get, _win32midi.MIDIINCAPSW_szPname_set)
    __swig_setmethods__["dwSupport"] = _win32midi.MIDIINCAPSW_dwSupport_set
    __swig_getmethods__["dwSupport"] = _win32midi.MIDIINCAPSW_dwSupport_get
    if _newclass:dwSupport = property(_win32midi.MIDIINCAPSW_dwSupport_get, _win32midi.MIDIINCAPSW_dwSupport_set)
    def __init__(self, *args):
        _swig_setattr(self, MIDIINCAPSW, 'this', _win32midi.new_MIDIINCAPSW(*args))
        _swig_setattr(self, MIDIINCAPSW, 'thisown', 1)
    def __del__(self, destroy=_win32midi.delete_MIDIINCAPSW):
        try:
            if self.thisown: destroy(self)
        except: pass

class MIDIINCAPSWPtr(MIDIINCAPSW):
    def __init__(self, this):
        _swig_setattr(self, MIDIINCAPSW, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, MIDIINCAPSW, 'thisown', 0)
        _swig_setattr(self, MIDIINCAPSW,self.__class__,MIDIINCAPSW)
_win32midi.MIDIINCAPSW_swigregister(MIDIINCAPSWPtr)

class MIDIINCAPS2A(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, MIDIINCAPS2A, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, MIDIINCAPS2A, name)
    def __repr__(self):
        return "<C MIDIINCAPS2A instance at %s>" % (self.this,)
    __swig_setmethods__["wMid"] = _win32midi.MIDIINCAPS2A_wMid_set
    __swig_getmethods__["wMid"] = _win32midi.MIDIINCAPS2A_wMid_get
    if _newclass:wMid = property(_win32midi.MIDIINCAPS2A_wMid_get, _win32midi.MIDIINCAPS2A_wMid_set)
    __swig_setmethods__["wPid"] = _win32midi.MIDIINCAPS2A_wPid_set
    __swig_getmethods__["wPid"] = _win32midi.MIDIINCAPS2A_wPid_get
    if _newclass:wPid = property(_win32midi.MIDIINCAPS2A_wPid_get, _win32midi.MIDIINCAPS2A_wPid_set)
    __swig_setmethods__["vDriverVersion"] = _win32midi.MIDIINCAPS2A_vDriverVersion_set
    __swig_getmethods__["vDriverVersion"] = _win32midi.MIDIINCAPS2A_vDriverVersion_get
    if _newclass:vDriverVersion = property(_win32midi.MIDIINCAPS2A_vDriverVersion_get, _win32midi.MIDIINCAPS2A_vDriverVersion_set)
    __swig_setmethods__["szPname"] = _win32midi.MIDIINCAPS2A_szPname_set
    __swig_getmethods__["szPname"] = _win32midi.MIDIINCAPS2A_szPname_get
    if _newclass:szPname = property(_win32midi.MIDIINCAPS2A_szPname_get, _win32midi.MIDIINCAPS2A_szPname_set)
    __swig_setmethods__["dwSupport"] = _win32midi.MIDIINCAPS2A_dwSupport_set
    __swig_getmethods__["dwSupport"] = _win32midi.MIDIINCAPS2A_dwSupport_get
    if _newclass:dwSupport = property(_win32midi.MIDIINCAPS2A_dwSupport_get, _win32midi.MIDIINCAPS2A_dwSupport_set)
    __swig_setmethods__["ManufacturerGuid"] = _win32midi.MIDIINCAPS2A_ManufacturerGuid_set
    __swig_getmethods__["ManufacturerGuid"] = _win32midi.MIDIINCAPS2A_ManufacturerGuid_get
    if _newclass:ManufacturerGuid = property(_win32midi.MIDIINCAPS2A_ManufacturerGuid_get, _win32midi.MIDIINCAPS2A_ManufacturerGuid_set)
    __swig_setmethods__["ProductGuid"] = _win32midi.MIDIINCAPS2A_ProductGuid_set
    __swig_getmethods__["ProductGuid"] = _win32midi.MIDIINCAPS2A_ProductGuid_get
    if _newclass:ProductGuid = property(_win32midi.MIDIINCAPS2A_ProductGuid_get, _win32midi.MIDIINCAPS2A_ProductGuid_set)
    __swig_setmethods__["NameGuid"] = _win32midi.MIDIINCAPS2A_NameGuid_set
    __swig_getmethods__["NameGuid"] = _win32midi.MIDIINCAPS2A_NameGuid_get
    if _newclass:NameGuid = property(_win32midi.MIDIINCAPS2A_NameGuid_get, _win32midi.MIDIINCAPS2A_NameGuid_set)
    def __init__(self, *args):
        _swig_setattr(self, MIDIINCAPS2A, 'this', _win32midi.new_MIDIINCAPS2A(*args))
        _swig_setattr(self, MIDIINCAPS2A, 'thisown', 1)
    def __del__(self, destroy=_win32midi.delete_MIDIINCAPS2A):
        try:
            if self.thisown: destroy(self)
        except: pass

class MIDIINCAPS2APtr(MIDIINCAPS2A):
    def __init__(self, this):
        _swig_setattr(self, MIDIINCAPS2A, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, MIDIINCAPS2A, 'thisown', 0)
        _swig_setattr(self, MIDIINCAPS2A,self.__class__,MIDIINCAPS2A)
_win32midi.MIDIINCAPS2A_swigregister(MIDIINCAPS2APtr)

class MIDIINCAPS2W(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, MIDIINCAPS2W, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, MIDIINCAPS2W, name)
    def __repr__(self):
        return "<C MIDIINCAPS2W instance at %s>" % (self.this,)
    __swig_setmethods__["wMid"] = _win32midi.MIDIINCAPS2W_wMid_set
    __swig_getmethods__["wMid"] = _win32midi.MIDIINCAPS2W_wMid_get
    if _newclass:wMid = property(_win32midi.MIDIINCAPS2W_wMid_get, _win32midi.MIDIINCAPS2W_wMid_set)
    __swig_setmethods__["wPid"] = _win32midi.MIDIINCAPS2W_wPid_set
    __swig_getmethods__["wPid"] = _win32midi.MIDIINCAPS2W_wPid_get
    if _newclass:wPid = property(_win32midi.MIDIINCAPS2W_wPid_get, _win32midi.MIDIINCAPS2W_wPid_set)
    __swig_setmethods__["vDriverVersion"] = _win32midi.MIDIINCAPS2W_vDriverVersion_set
    __swig_getmethods__["vDriverVersion"] = _win32midi.MIDIINCAPS2W_vDriverVersion_get
    if _newclass:vDriverVersion = property(_win32midi.MIDIINCAPS2W_vDriverVersion_get, _win32midi.MIDIINCAPS2W_vDriverVersion_set)
    __swig_setmethods__["szPname"] = _win32midi.MIDIINCAPS2W_szPname_set
    __swig_getmethods__["szPname"] = _win32midi.MIDIINCAPS2W_szPname_get
    if _newclass:szPname = property(_win32midi.MIDIINCAPS2W_szPname_get, _win32midi.MIDIINCAPS2W_szPname_set)
    __swig_setmethods__["dwSupport"] = _win32midi.MIDIINCAPS2W_dwSupport_set
    __swig_getmethods__["dwSupport"] = _win32midi.MIDIINCAPS2W_dwSupport_get
    if _newclass:dwSupport = property(_win32midi.MIDIINCAPS2W_dwSupport_get, _win32midi.MIDIINCAPS2W_dwSupport_set)
    __swig_setmethods__["ManufacturerGuid"] = _win32midi.MIDIINCAPS2W_ManufacturerGuid_set
    __swig_getmethods__["ManufacturerGuid"] = _win32midi.MIDIINCAPS2W_ManufacturerGuid_get
    if _newclass:ManufacturerGuid = property(_win32midi.MIDIINCAPS2W_ManufacturerGuid_get, _win32midi.MIDIINCAPS2W_ManufacturerGuid_set)
    __swig_setmethods__["ProductGuid"] = _win32midi.MIDIINCAPS2W_ProductGuid_set
    __swig_getmethods__["ProductGuid"] = _win32midi.MIDIINCAPS2W_ProductGuid_get
    if _newclass:ProductGuid = property(_win32midi.MIDIINCAPS2W_ProductGuid_get, _win32midi.MIDIINCAPS2W_ProductGuid_set)
    __swig_setmethods__["NameGuid"] = _win32midi.MIDIINCAPS2W_NameGuid_set
    __swig_getmethods__["NameGuid"] = _win32midi.MIDIINCAPS2W_NameGuid_get
    if _newclass:NameGuid = property(_win32midi.MIDIINCAPS2W_NameGuid_get, _win32midi.MIDIINCAPS2W_NameGuid_set)
    def __init__(self, *args):
        _swig_setattr(self, MIDIINCAPS2W, 'this', _win32midi.new_MIDIINCAPS2W(*args))
        _swig_setattr(self, MIDIINCAPS2W, 'thisown', 1)
    def __del__(self, destroy=_win32midi.delete_MIDIINCAPS2W):
        try:
            if self.thisown: destroy(self)
        except: pass

class MIDIINCAPS2WPtr(MIDIINCAPS2W):
    def __init__(self, this):
        _swig_setattr(self, MIDIINCAPS2W, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, MIDIINCAPS2W, 'thisown', 0)
        _swig_setattr(self, MIDIINCAPS2W,self.__class__,MIDIINCAPS2W)
_win32midi.MIDIINCAPS2W_swigregister(MIDIINCAPS2WPtr)

class MIDIHDR(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, MIDIHDR, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, MIDIHDR, name)
    def __repr__(self):
        return "<C MIDIHDR instance at %s>" % (self.this,)
    __swig_setmethods__["lpData"] = _win32midi.MIDIHDR_lpData_set
    __swig_getmethods__["lpData"] = _win32midi.MIDIHDR_lpData_get
    if _newclass:lpData = property(_win32midi.MIDIHDR_lpData_get, _win32midi.MIDIHDR_lpData_set)
    __swig_setmethods__["dwBufferLength"] = _win32midi.MIDIHDR_dwBufferLength_set
    __swig_getmethods__["dwBufferLength"] = _win32midi.MIDIHDR_dwBufferLength_get
    if _newclass:dwBufferLength = property(_win32midi.MIDIHDR_dwBufferLength_get, _win32midi.MIDIHDR_dwBufferLength_set)
    __swig_setmethods__["dwBytesRecorded"] = _win32midi.MIDIHDR_dwBytesRecorded_set
    __swig_getmethods__["dwBytesRecorded"] = _win32midi.MIDIHDR_dwBytesRecorded_get
    if _newclass:dwBytesRecorded = property(_win32midi.MIDIHDR_dwBytesRecorded_get, _win32midi.MIDIHDR_dwBytesRecorded_set)
    __swig_setmethods__["dwUser"] = _win32midi.MIDIHDR_dwUser_set
    __swig_getmethods__["dwUser"] = _win32midi.MIDIHDR_dwUser_get
    if _newclass:dwUser = property(_win32midi.MIDIHDR_dwUser_get, _win32midi.MIDIHDR_dwUser_set)
    __swig_setmethods__["dwFlags"] = _win32midi.MIDIHDR_dwFlags_set
    __swig_getmethods__["dwFlags"] = _win32midi.MIDIHDR_dwFlags_get
    if _newclass:dwFlags = property(_win32midi.MIDIHDR_dwFlags_get, _win32midi.MIDIHDR_dwFlags_set)
    __swig_setmethods__["lpNext"] = _win32midi.MIDIHDR_lpNext_set
    __swig_getmethods__["lpNext"] = _win32midi.MIDIHDR_lpNext_get
    if _newclass:lpNext = property(_win32midi.MIDIHDR_lpNext_get, _win32midi.MIDIHDR_lpNext_set)
    __swig_setmethods__["reserved"] = _win32midi.MIDIHDR_reserved_set
    __swig_getmethods__["reserved"] = _win32midi.MIDIHDR_reserved_get
    if _newclass:reserved = property(_win32midi.MIDIHDR_reserved_get, _win32midi.MIDIHDR_reserved_set)
    __swig_setmethods__["dwOffset"] = _win32midi.MIDIHDR_dwOffset_set
    __swig_getmethods__["dwOffset"] = _win32midi.MIDIHDR_dwOffset_get
    if _newclass:dwOffset = property(_win32midi.MIDIHDR_dwOffset_get, _win32midi.MIDIHDR_dwOffset_set)
    __swig_setmethods__["dwReserved"] = _win32midi.MIDIHDR_dwReserved_set
    __swig_getmethods__["dwReserved"] = _win32midi.MIDIHDR_dwReserved_get
    if _newclass:dwReserved = property(_win32midi.MIDIHDR_dwReserved_get, _win32midi.MIDIHDR_dwReserved_set)
    def __init__(self, *args):
        _swig_setattr(self, MIDIHDR, 'this', _win32midi.new_MIDIHDR(*args))
        _swig_setattr(self, MIDIHDR, 'thisown', 1)
    def __del__(self, destroy=_win32midi.delete_MIDIHDR):
        try:
            if self.thisown: destroy(self)
        except: pass

class MIDIHDRPtr(MIDIHDR):
    def __init__(self, this):
        _swig_setattr(self, MIDIHDR, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, MIDIHDR, 'thisown', 0)
        _swig_setattr(self, MIDIHDR,self.__class__,MIDIHDR)
_win32midi.MIDIHDR_swigregister(MIDIHDRPtr)

class MIDIEVENT(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, MIDIEVENT, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, MIDIEVENT, name)
    def __repr__(self):
        return "<C MIDIEVENT instance at %s>" % (self.this,)
    __swig_setmethods__["dwDeltaTime"] = _win32midi.MIDIEVENT_dwDeltaTime_set
    __swig_getmethods__["dwDeltaTime"] = _win32midi.MIDIEVENT_dwDeltaTime_get
    if _newclass:dwDeltaTime = property(_win32midi.MIDIEVENT_dwDeltaTime_get, _win32midi.MIDIEVENT_dwDeltaTime_set)
    __swig_setmethods__["dwStreamID"] = _win32midi.MIDIEVENT_dwStreamID_set
    __swig_getmethods__["dwStreamID"] = _win32midi.MIDIEVENT_dwStreamID_get
    if _newclass:dwStreamID = property(_win32midi.MIDIEVENT_dwStreamID_get, _win32midi.MIDIEVENT_dwStreamID_set)
    __swig_setmethods__["dwEvent"] = _win32midi.MIDIEVENT_dwEvent_set
    __swig_getmethods__["dwEvent"] = _win32midi.MIDIEVENT_dwEvent_get
    if _newclass:dwEvent = property(_win32midi.MIDIEVENT_dwEvent_get, _win32midi.MIDIEVENT_dwEvent_set)
    __swig_setmethods__["dwParms"] = _win32midi.MIDIEVENT_dwParms_set
    __swig_getmethods__["dwParms"] = _win32midi.MIDIEVENT_dwParms_get
    if _newclass:dwParms = property(_win32midi.MIDIEVENT_dwParms_get, _win32midi.MIDIEVENT_dwParms_set)
    def __init__(self, *args):
        _swig_setattr(self, MIDIEVENT, 'this', _win32midi.new_MIDIEVENT(*args))
        _swig_setattr(self, MIDIEVENT, 'thisown', 1)
    def __del__(self, destroy=_win32midi.delete_MIDIEVENT):
        try:
            if self.thisown: destroy(self)
        except: pass

class MIDIEVENTPtr(MIDIEVENT):
    def __init__(self, this):
        _swig_setattr(self, MIDIEVENT, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, MIDIEVENT, 'thisown', 0)
        _swig_setattr(self, MIDIEVENT,self.__class__,MIDIEVENT)
_win32midi.MIDIEVENT_swigregister(MIDIEVENTPtr)

class MIDISTRMBUFFVER(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, MIDISTRMBUFFVER, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, MIDISTRMBUFFVER, name)
    def __repr__(self):
        return "<C MIDISTRMBUFFVER instance at %s>" % (self.this,)
    __swig_setmethods__["dwVersion"] = _win32midi.MIDISTRMBUFFVER_dwVersion_set
    __swig_getmethods__["dwVersion"] = _win32midi.MIDISTRMBUFFVER_dwVersion_get
    if _newclass:dwVersion = property(_win32midi.MIDISTRMBUFFVER_dwVersion_get, _win32midi.MIDISTRMBUFFVER_dwVersion_set)
    __swig_setmethods__["dwMid"] = _win32midi.MIDISTRMBUFFVER_dwMid_set
    __swig_getmethods__["dwMid"] = _win32midi.MIDISTRMBUFFVER_dwMid_get
    if _newclass:dwMid = property(_win32midi.MIDISTRMBUFFVER_dwMid_get, _win32midi.MIDISTRMBUFFVER_dwMid_set)
    __swig_setmethods__["dwOEMVersion"] = _win32midi.MIDISTRMBUFFVER_dwOEMVersion_set
    __swig_getmethods__["dwOEMVersion"] = _win32midi.MIDISTRMBUFFVER_dwOEMVersion_get
    if _newclass:dwOEMVersion = property(_win32midi.MIDISTRMBUFFVER_dwOEMVersion_get, _win32midi.MIDISTRMBUFFVER_dwOEMVersion_set)
    def __init__(self, *args):
        _swig_setattr(self, MIDISTRMBUFFVER, 'this', _win32midi.new_MIDISTRMBUFFVER(*args))
        _swig_setattr(self, MIDISTRMBUFFVER, 'thisown', 1)
    def __del__(self, destroy=_win32midi.delete_MIDISTRMBUFFVER):
        try:
            if self.thisown: destroy(self)
        except: pass

class MIDISTRMBUFFVERPtr(MIDISTRMBUFFVER):
    def __init__(self, this):
        _swig_setattr(self, MIDISTRMBUFFVER, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, MIDISTRMBUFFVER, 'thisown', 0)
        _swig_setattr(self, MIDISTRMBUFFVER,self.__class__,MIDISTRMBUFFVER)
_win32midi.MIDISTRMBUFFVER_swigregister(MIDISTRMBUFFVERPtr)

MHDR_DONE = _win32midi.MHDR_DONE
MHDR_PREPARED = _win32midi.MHDR_PREPARED
MHDR_INQUEUE = _win32midi.MHDR_INQUEUE
MHDR_ISSTRM = _win32midi.MHDR_ISSTRM
MEVT_F_SHORT = _win32midi.MEVT_F_SHORT
MEVT_F_LONG = _win32midi.MEVT_F_LONG
MEVT_F_CALLBACK = _win32midi.MEVT_F_CALLBACK
MIDISTRM_ERROR = _win32midi.MIDISTRM_ERROR
MIDIPROP_SET = _win32midi.MIDIPROP_SET
MIDIPROP_GET = _win32midi.MIDIPROP_GET
MIDIPROP_TIMEDIV = _win32midi.MIDIPROP_TIMEDIV
MIDIPROP_TEMPO = _win32midi.MIDIPROP_TEMPO
class MIDIPROPTIMEDIV(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, MIDIPROPTIMEDIV, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, MIDIPROPTIMEDIV, name)
    def __repr__(self):
        return "<C MIDIPROPTIMEDIV instance at %s>" % (self.this,)
    __swig_setmethods__["cbStruct"] = _win32midi.MIDIPROPTIMEDIV_cbStruct_set
    __swig_getmethods__["cbStruct"] = _win32midi.MIDIPROPTIMEDIV_cbStruct_get
    if _newclass:cbStruct = property(_win32midi.MIDIPROPTIMEDIV_cbStruct_get, _win32midi.MIDIPROPTIMEDIV_cbStruct_set)
    __swig_setmethods__["dwTimeDiv"] = _win32midi.MIDIPROPTIMEDIV_dwTimeDiv_set
    __swig_getmethods__["dwTimeDiv"] = _win32midi.MIDIPROPTIMEDIV_dwTimeDiv_get
    if _newclass:dwTimeDiv = property(_win32midi.MIDIPROPTIMEDIV_dwTimeDiv_get, _win32midi.MIDIPROPTIMEDIV_dwTimeDiv_set)
    def __init__(self, *args):
        _swig_setattr(self, MIDIPROPTIMEDIV, 'this', _win32midi.new_MIDIPROPTIMEDIV(*args))
        _swig_setattr(self, MIDIPROPTIMEDIV, 'thisown', 1)
    def __del__(self, destroy=_win32midi.delete_MIDIPROPTIMEDIV):
        try:
            if self.thisown: destroy(self)
        except: pass

class MIDIPROPTIMEDIVPtr(MIDIPROPTIMEDIV):
    def __init__(self, this):
        _swig_setattr(self, MIDIPROPTIMEDIV, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, MIDIPROPTIMEDIV, 'thisown', 0)
        _swig_setattr(self, MIDIPROPTIMEDIV,self.__class__,MIDIPROPTIMEDIV)
_win32midi.MIDIPROPTIMEDIV_swigregister(MIDIPROPTIMEDIVPtr)

class MIDIPROPTEMPO(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, MIDIPROPTEMPO, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, MIDIPROPTEMPO, name)
    def __repr__(self):
        return "<C MIDIPROPTEMPO instance at %s>" % (self.this,)
    __swig_setmethods__["cbStruct"] = _win32midi.MIDIPROPTEMPO_cbStruct_set
    __swig_getmethods__["cbStruct"] = _win32midi.MIDIPROPTEMPO_cbStruct_get
    if _newclass:cbStruct = property(_win32midi.MIDIPROPTEMPO_cbStruct_get, _win32midi.MIDIPROPTEMPO_cbStruct_set)
    __swig_setmethods__["dwTempo"] = _win32midi.MIDIPROPTEMPO_dwTempo_set
    __swig_getmethods__["dwTempo"] = _win32midi.MIDIPROPTEMPO_dwTempo_get
    if _newclass:dwTempo = property(_win32midi.MIDIPROPTEMPO_dwTempo_get, _win32midi.MIDIPROPTEMPO_dwTempo_set)
    def __init__(self, *args):
        _swig_setattr(self, MIDIPROPTEMPO, 'this', _win32midi.new_MIDIPROPTEMPO(*args))
        _swig_setattr(self, MIDIPROPTEMPO, 'thisown', 1)
    def __del__(self, destroy=_win32midi.delete_MIDIPROPTEMPO):
        try:
            if self.thisown: destroy(self)
        except: pass

class MIDIPROPTEMPOPtr(MIDIPROPTEMPO):
    def __init__(self, this):
        _swig_setattr(self, MIDIPROPTEMPO, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, MIDIPROPTEMPO, 'thisown', 0)
        _swig_setattr(self, MIDIPROPTEMPO,self.__class__,MIDIPROPTEMPO)
_win32midi.MIDIPROPTEMPO_swigregister(MIDIPROPTEMPOPtr)


midiOutGetNumDevs = _win32midi.midiOutGetNumDevs

midiStreamOpen = _win32midi.midiStreamOpen

midiStreamClose = _win32midi.midiStreamClose

midiStreamProperty = _win32midi.midiStreamProperty

midiStreamPosition = _win32midi.midiStreamPosition

midiStreamOut = _win32midi.midiStreamOut

midiStreamPause = _win32midi.midiStreamPause

midiStreamRestart = _win32midi.midiStreamRestart

midiStreamStop = _win32midi.midiStreamStop

midiConnect = _win32midi.midiConnect

midiDisconnect = _win32midi.midiDisconnect

midiOutGetDevCapsA = _win32midi.midiOutGetDevCapsA

midiOutGetDevCapsW = _win32midi.midiOutGetDevCapsW

midiOutGetVolume = _win32midi.midiOutGetVolume

midiOutSetVolume = _win32midi.midiOutSetVolume

midiOutGetErrorTextA = _win32midi.midiOutGetErrorTextA

midiOutGetErrorTextW = _win32midi.midiOutGetErrorTextW

midiOutOpen = _win32midi.midiOutOpen

midiOutClose = _win32midi.midiOutClose

midiOutPrepareHeader = _win32midi.midiOutPrepareHeader

midiOutUnprepareHeader = _win32midi.midiOutUnprepareHeader

midiOutShortMsg = _win32midi.midiOutShortMsg

midiOutLongMsg = _win32midi.midiOutLongMsg

midiOutReset = _win32midi.midiOutReset

midiOutCachePatches = _win32midi.midiOutCachePatches

midiOutCacheDrumPatches = _win32midi.midiOutCacheDrumPatches

midiOutGetID = _win32midi.midiOutGetID

midiOutMessage = _win32midi.midiOutMessage

midiInGetNumDevs = _win32midi.midiInGetNumDevs

midiInGetDevCapsA = _win32midi.midiInGetDevCapsA

midiInGetDevCapsW = _win32midi.midiInGetDevCapsW

midiInGetErrorTextA = _win32midi.midiInGetErrorTextA

midiInGetErrorTextW = _win32midi.midiInGetErrorTextW

midiInOpen = _win32midi.midiInOpen

midiInClose = _win32midi.midiInClose

midiInPrepareHeader = _win32midi.midiInPrepareHeader

midiInUnprepareHeader = _win32midi.midiInUnprepareHeader

midiInAddBuffer = _win32midi.midiInAddBuffer

midiInStart = _win32midi.midiInStart

midiInStop = _win32midi.midiInStop

midiInReset = _win32midi.midiInReset

midiInGetID = _win32midi.midiInGetID

midiInMessage = _win32midi.midiInMessage


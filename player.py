# A simple Python class to provide some high level MIDI APIs to play MIDI
# $Id: player.py 30 2007-01-28 17:12:07Z csw $
# Copyright 2004 Soon Wah Chua

import sys
from timing import waitTime
if sys.winver >= '2.7':
    from win32midi2 import *
else:
    from win32midi import *
import time,thread
import cPickle

global COUNTS
COUNTS=0
_patches = cPickle.load(open('patches.dat','rb'))

def buildScale(chord=0):
    scale = {}
    base = [1,1.5,2,2.5,3,4,4.5,5,5.5,6,6.5,7]
    k = []
    for i in range(-5+chord,0):
        k += map(lambda x: i*10-x,base)
    k += base
    for i in range(1,5+chord):
        k += map(lambda x: i*10+x,base)
    val = range(0,120)
    full = dict(zip(k,val))
    return full

def buildChord():
    return buildScale(1)

CMajor=buildScale()
CMajor_chord=buildChord()

class MIDIError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class Player:
    """
    This is a class to provide simple interfaces for playing musical notes on the PC synthesizer
    """
    
    def __init__(self,dev=0):
        ret, self.h = midiOutOpen(dev,0,0,0)
        if not(ret==0):
            raise MIDIError('Device open operation failed')
        self.setTempo(120)
        
    def __del__(self):
        midiOutClose(self.h)

    def setInstrument(self, instrument=0, chan=0):
        """Select the instrument for playing
        """
        if type(instrument)==type('s'):
            num = _patches[instrument]
        else:
            num = instrument
        midiOutShortMsg(self.h,0xc0|chan|(num<<8))

    def setChordInstrument(self, instrument=0, startChan=1, maxNotes=3):
        """Select the instrument for playing
        """
        if type(instrument)==type('s'):
            num = _patches[instrument]
        else:
            num = instrument

        for i in range(maxNotes):
            midiOutShortMsg(self.h,0xc0|startChan+i|(num<<8))

    def listInstruments(self):
        import pprint
        return pprint.pprint(_patches)

    def playNote(self, num, vel=120, len=0, chan=0):
        """
        Play a note
        The note is represented by a number in the range from 0 to 127 where 60 is the Middle C
        """
        # Check the note and volume are in range
        if(num > 127 or num < 0):
            raise MIDIError('Note out of range')
        if(vel > 127 or vel < 0):
            raise MIDIError('Velocity out of range')
        # Setup the MIDI packet
        midiOutShortMsg(self.h,0x90|chan|(num<<8)|vel<<16)

    def playChord(self, chord, vel=100, len=0, chan=0):
        """
        Play a chord
        The chord is represented by a list of numbers in the range from 0 to 127 where 60 is the Middle C
        """
        for num in chord:
            # Check the note and volume are in range
            if(num > 127 or num < 0):
                raise MIDIError('Note out of range')
            if(vel > 127 or vel < 0):
                raise MIDIError('Velocity out of range')
        # Setup the MIDI packet
        for num in chord:
            midiOutShortMsg(self.h,0x90|chan|(num<<8)|vel<<16)

    def setVolume(self, left, right):
        """Set the left and right volume of the Synthesizer
        The volume setting can range from 0 to 65535 for each channel"""
        return midiOutSetVolume(self.h,(left<<16)|right)

    def getVolume(self):
        """Return the left and right volume of the Synthesizer"""
        r, v = midiOutGetVolume(self.h)
        return (v>>16)&0xFFFF, v & 0xFFFF

    def outShortMsg(self, status, first, second):
        """Send a MIDI short message to the synthesizer"""
        midiOutShortMsg(self.h,status|(first<<8)|second<<16)

    def setTempo(self,val):
        """Set the Tempo to val"""
        self.beat = val
        self.tpb  = 60./val*4
        _noteLen = [1,2,4,8,12,16,32,64]
        self._noteTimings = dict(zip(_noteLen, map(lambda x: self.tpb/x , _noteLen)))
        _noteLen = [1.1,2.1,4.1,8.1,16.1,32.1,64.1]
        for n in _noteLen:
            self._noteTimings[n] = self.tpb/int(n)
            self._noteTimings[n] *= 1.5

    def playAllChord(self,chord,chord_t,octave=1):
        """Play all the chords in chord with timing according to chord_t"""
        global COUNTS
        COUNTS+=1
        curScale=buildScale(octave)
        for i in range(len(chord)):
            if (type(chord[i])==type([])):
                if not (chord[i][0] == 99):
                    self.playChord(map(lambda j:curScale[j],chord[i]))
            else:
                if not (chord[i] == 99):
                    self.playChord(map(lambda j:curScale[j],[chord[i]]))

            #time.sleep(self._noteTimings[chord_t[i]])
            waitTime(self._noteTimings[chord_t[i]])
        COUNTS-=1

    def playAllNotes(self,notes,notes_t):
        """Play all the chords in notes with timing according to notes_t"""
        for i in range(len(notes)):
            if not (notes[i] == 99):
                self.playNote(CMajor[notes[i]])
            #time.sleep(self._noteTimings[notes_t[i]])
            waitTime(self._noteTimings[notes_t[i]])

    def playPiece(self,notesStruct,chordStruct):
        """Play a piece of music composed of notesStruct and chordStruct.
        noteStruct is a tuple, (notes, notes_t) where notes is the list of notes and
            notes_t is the list of timings for notes
        chordStruct is a tuple, (chords, chords_t) where notes is the list of chords and
            chords_t is the list of timings for chords
        """
        thread.start_new(self.playAllChord,chordStruct)
        apply(self.playAllNotes,notesStruct)
        
    def playPiece2(self,chordStructs):
        """Play a piece of music composed of chordStructs.
        each chordStruct is a tuple, (chords, chords_t) where notes is the list of chords and
            chords_t is the list of timings for chords
        """
        global COUNTS
        thread.start_new(self.playAllChord,chordStructs[0]+(0,))
        for i in range(1,len(chordStructs)):
            thread.start_new(self.playAllChord,chordStructs[i])
        time.sleep(1)
        while (COUNTS>0):
            time.sleep(10)

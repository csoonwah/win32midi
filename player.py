# A simple Python class to provide some high level MIDI APIs to play MIDI
# Copyright 2004-2023 Soon Wah Chua

import sys
import os
import time
import _thread
if os.name == 'java':
    import pickle
    from javax.sound.midi import *

    def getSyn(x):
        s = MidiSystem.getSynthesizer()
        r = s.open()
        return r, s

    def closeSyn(x):
        x.close()
        x = None

    playMidiNote = lambda s, chan, num, vel: s.channels[chan].noteOn(num, vel)

    def setMidiVol(s, left, right):
        s.channels[0].controlChange(7, (left + right) >> 8)
        # s.channels[0].controlChange(7 + 32, (left + right) % 256)
        s.channels[0].controlChange(10, (right - left) >> 8)
        # s.channels[0].controlChange(10 + 32,(right - left)%256)
        return 0
    progChange = lambda s, c, n: s.channels[c].programChange(n)
    threadStart = _thread.start_new_thread
    waitTime = time.sleep

    def getMidiVol(s):
        vh = s.channels[0].getController(7)
        dh = s.channels[0].getController(7 + 32)
        # vl = s.channels[0].getController(10)
        # dl = s.channels[0].getController(10 + 32)
        # v = vh << 7 + vl
        # d = dh<<7 + dl
        l_ = (float(64 - dh) / 64) * vh
        l_ = int(l_) if l_ > 0 else 0
        r = vh * float(dh + 64) / 64
        r = int(r) if r > 0 else 0
        return 0, (l_ << 24) + (r << 8)

    def outShortMidiMsg(syn, cmd, first, second):
        """Send a MIDI short message to the synthesizer"""
        # midiOutShortMsg(s.syn, status|(first<<8)|second<<16)
        synRcvr = syn.getReceiver()
        synRcvr.send(ShortMessage(cmd, 0, first, second), -1)
else:
    import pickle as pickle
    from timing import waitTime

    if sys.winver >= '2.7':
        from win32midi2 import *
        getSyn = lambda x: midiOutOpen(x, 0, 0, 0)
        closeSyn = lambda x: midiOutClose(x)
        playMidiNote = lambda s, chan, num, vel: \
            midiOutShortMsg(s, 0x90 | chan | (num << 8) | vel << 16)
        setMidiVol = lambda s, left, right: \
            midiOutSetVolume(s, (left << 16) | right)
        progChange = lambda s, c, n: midiOutShortMsg(s, 0xc0 | c | (n << 8))
        threadStart = _thread.start_new
        getMidiVol = lambda s: midiOutGetVolume(s)

        def outShortMidiMsg(syn, cmd, first, second):
            """Send a MIDI short message to the synthesizer"""
            midiOutShortMsg(syn, cmd | (first << 8) | second << 16)
    else:
        print("Python version not supported")
        exit(1)

global COUNTS
COUNTS = 0
_patches = pickle.load(open('patches.dat', 'rb'))


def buildScale(chord=0):
    # scale = {}
    base = [1, 1.5, 2, 2.5, 3, 4, 4.5, 5, 5.5, 6, 6.5, 7]
    k = []
    for i in range(-5 + chord, 0):
        k += [i * 10 - x for x in base]
    k += base
    for i in range(1, 5 + chord):
        k += [i * 10 + x for x in base]
    val = list(range(0, 120))
    full = dict(list(zip(k, val)))
    return full


def buildChord():
    return buildScale(1)


CMajor = buildScale()
CMajor_chord = buildChord()


class MIDIError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class Player:
    """
    This is a class to provide simple interfaces for playing musical notes on
    the PC synthesizer
    """

    def __init__(self, dev=0):
        ret, self.syn = getSyn(dev)
        # if not(ret==0):
        #    raise MIDIError('Device open operation failed')
        self.setTempo(120)

    def __del__(self):
        closeSyn(self.syn)

    def setInstrument(self, instrument=0, chan=0):
        """Select the instrument for playing
        """
        if isinstance(instrument, str):
            num = _patches[instrument]
        else:
            num = instrument
        progChange(self.syn, chan, num)

    def setChordInstrument(self, instrument=0, startChan=1, maxNotes=3):
        """Select the instrument for playing
        """
        if isinstance(instrument, str):
            num = _patches[instrument]
        else:
            num = instrument

        for i in range(maxNotes):
            progChange(self.syn, startChan + i, num)

    def listInstruments(self):
        import pprint
        return pprint.pprint(_patches)

    def playNote(self, num, vel=120, len=0, chan=0):
        """
        Play a note
        The note is represented by a number in the range from 0 to 127
        where 60 is the Middle C
        """
        # Check the note and volume are in range
        if(num > 127 or num < 0):
            raise MIDIError('Note out of range')
        if(vel > 127 or vel < 0):
            raise MIDIError('Velocity out of range')
        # Setup the MIDI packet
        playMidiNote(self.syn, chan, num, vel)

    def playChord(self, chord, vel=100, len=0, chan=0):
        """
        Play a chord
        The chord is represented by a list of numbers in the range from
        0 to 127 where 60 is the Middle C
        """
        for num in chord:
            # Check the note and volume are in range
            if(num > 127 or num < 0):
                raise MIDIError('Note out of range')
            if(vel > 127 or vel < 0):
                raise MIDIError('Velocity out of range')
        # Setup the MIDI packet
        for num in chord:
            playMidiNote(self.syn, chan, num, vel)

    def setVolume(self, left, right):
        """Set the left and right volume of the Synthesizer
        The volume setting can range from 0 to 65535 for each channel"""
        return setMidiVol(self.syn, left, right)

    def getVolume(self):
        """Return the left and right volume of the Synthesizer"""
        r, v = getMidiVol(self.syn)
        return (v >> 16) & 0xFFFF, v & 0xFFFF

    def outShortMsg(self, status, first, second):
        """Send a MIDI short message to the synthesizer"""
        if first < 128 and second < 128:
            outShortMidiMsg(self.syn, status, first, second)

    def setTempo(self, val):
        """Set the Tempo to val"""
        self.beat = val
        self.tpb = 60. / val * 4
        _noteLen = [1, 2, 4, 8, 12, 16, 32, 64]
        self._noteTimings = dict(list(zip(_noteLen, [self.tpb / x for x in _noteLen])))
        _noteLen = [1.1, 2.1, 4.1, 8.1, 16.1, 32.1, 64.1]
        for n in _noteLen:
            self._noteTimings[n] = self.tpb / int(n)
            self._noteTimings[n] *= 1.5

    def playAllChord(self, chord, chord_t, octave=1):
        """Play all the chords in chord with timing according to chord_t"""
        global COUNTS
        COUNTS += 1
        curScale = buildScale(octave)
        for i in range(len(chord)):
            if isinstance(chord[i], list):
                if not (chord[i][0] == 99):
                    self.playChord([curScale[j] for j in chord[i]])
            else:
                if not (chord[i] == 99):
                    self.playChord([curScale[j] for j in [chord[i]]])
            waitTime(self._noteTimings[chord_t[i]])
        COUNTS -= 1

    def playAllNotes(self, notes, notes_t):
        """Play all the chords in notes with timing according to notes_t"""
        for i in range(len(notes)):
            if not (notes[i] == 99):
                self.playNote(CMajor[notes[i]])
            waitTime(self._noteTimings[notes_t[i]])

    def playPiece(self, notesStruct, chordStruct):
        """Play a piece of music composed of notesStruct and chordStruct.
        noteStruct is a tuple, (notes, notes_t) where notes is the list of
        notes and notes_t is the list of timings for notes
        chordStruct is a tuple, (chords, chords_t) where notes is the list of
        chords and chords_t is the list of timings for chords
        """
        threadStart(self.playAllChord, chordStruct)
        self.playAllNotes(*notesStruct)

    def playPiece2(self, chordStructs):
        """Play a piece of music composed of chordStructs.
        each chordStruct is a tuple, (chords, chords_t) where
        notes is the list of chords and chords_t is the list of
        timings for chords
        """
        global COUNTS
        threadStart(self.playAllChord, chordStructs[0] + (0,))
        for i in range(1, len(chordStructs)):
            threadStart(self.playAllChord, chordStructs[i])
        time.sleep(1)
        while (COUNTS > 0):
            time.sleep(2)

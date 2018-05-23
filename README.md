# A Python extension to call the MIDI APIs in Windows for playing synthesizer music
 
## Introduction
Most computers these days come installed with a soundcard or integrated sound device onboard that can play sound. Some of these cards have builtin synthesizer to play MIDI notes. Those that do not have builtin synthesizer are also likely come with a software synthesizer that can play MIDI notes. Installing the latest DirectX SDK will also likely to install the Microsoft Software Synthesizer that comes with the DirectMusic APIs. Thus the quality of the sound produced from MIDI has improved a lot over the years and it will be a lot of fun if we can write program to play music.

This package provides a Python extension to call the MIDI APIs in Windows. Several of the Win32 MIDI APIs are available. A simple high level player module is provided. Please read the sample files to understand its usage. More documentation will be available some time later. Enjoy!

## System Requirements
* Windows Operating system (tested on Windows 10)
* Sound card or integrated sound device on motherboard, with hardware/software MIDI synthesizer
* Python 2.7

## Example
Check out the file win32midiTest.py to find out how the module could be used. Double-clicking the same file should play some sample notes. A playertest.py play notes with the higher level API module, player. Check it out to play simple music. It also demonstrate how to play with more than one instrument together, as well as adding chords to your music. Some scripts are included to show the playing of music through the player module.

## Features
The win32midi module provides wrappers to call Win32 MIDI APIs. The following APIs are currently available.
- midiOutClose
- midiOutGetDevCapsA
- midiOutGetErrorTextA
- midiOutGetID
- midiOutGetNumDevs
- midiOutGetVolume
- midiOutLongMsg
- midiOutOpen
- midiOutPrepareHeader
- midiOutReset
- midiOutSetVolume
- midiOutShortMsg
- midiOutUnprepareHeader
- midiStreamOpen
- midiStreamOut
- midiStreamRestart
- midiStreamClose
- midiInGetDevCapsA
- midiInGetNumDevs

As the documentation is still being written, please refer to the test programs to get a glimpse of how to use the module.

Copyright S. W. Chua, 2004-2018, All rights reserved

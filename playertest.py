# A simple MIDI player demo
# Copyright 2004-2018 Soon Wah Chua
import player
import time,os
mr = player.Player() # Instantiate a Midi object
# Set the musical instrument, 0 is for Acoustic Grand Piano
# Check the General MIDI Specification for instrument number
mr.setInstrument(0)
mr.setVolume(32000,32000)
# Play all the possible white keys in MIDI specification
notes = (0,2,4,5,7,9,11) # For notes C,D,E,F,G,A,B respectively in an octave
for octave in range(11):
  for n in notes:
    time.sleep(0.1)
    mr.outShortMsg(0x91,octave*12+n,120) # Send note ON message to Channel 1

# Let's play the Twinkle Little Star
mr.setInstrument(10) # Choose the Musical Box sound
star = [1,1,5,5,6,6,5,4,4,3,3,2,2,1]
tick = [1,1,1,1,1,1,2,1,1,1,1,1,1,2]
star +=[5,5,4,4,3,3,2,5,5,4,4,3,3,2]
tick += [1,1,1,1,1,1,2,1,1,1,1,1,1,2]
star +=[1,1,5,5,6,6,5,4,4,3,3,2,2,1]
tick += [1,1,1,1,1,1,2,1,1,1,1,1,1,2]

ticksPerMin = 120
timePerTick = 60./ticksPerMin
print 'Volume', mr.getVolume()	
l,r = mr.getVolume()
for n in range(len(star)):
	s = star[n]
	sn = 5*12+notes[s-1]
	# mr.outShortMsg(0x91,sn,120) # Can use outShortMsg or playNote
	mr.playNote(sn,120,0)
	mr.setVolume(int(l*1.01**n),int(r*1.01**n))
#	print 'Volume', mr.getVolume()
	time.sleep(timePerTick*tick[n])
print 'Volume', mr.getVolume()
# Playing percussion instruments
print 'Playing with percussion instruments'
for v in range(1,127):
	mr.outShortMsg(0x99,54,v) # Choosing Tambourine
	#print 'Vel: %d' % v
	time.sleep(0.1)
	
# Playing a note with different velocities,v, will produce different volume for the same note
print 'Start varying velocities, or volume for different notes'
mr.setInstrument(0)
for v in range(1,127):
	mr.playNote(60,v,0)
	#print 'Vel: %d' % v
	time.sleep(0.1)

# For playing two different instrument together, we can set the second instrument to be on a different channel, which
# if not specified is channel 0. Musical notes can be played with the second instrument by directing to the same channel
print 'Playing different instruments together'
mr.setInstrument(123,1) # Choosing bird tweet on channel #1
for n in range(len(star)):
	s = star[n]
	sn = 5*12+notes[s-1]
	mr.playNote(sn,120,0,0)
	mr.playNote(sn,50,0,1)
	time.sleep(timePerTick*tick[n])

# Using different channels, we can play chords
# Set the instrument to play the chord to be piano and the max number of notes in the chord to be 4
# The starting channel for the chord is 1, leaving channel 0 for main melody
print 'Playing with chords'
mr.setChordInstrument(0,1,4)
mr.playChord([53,57,60],120,0,1) # 1 is the starting channel, playing F chord
time.sleep(0.5)
mr.playChord([48,52,55],120,0,1) # 1 is the starting channel, playing C chord
time.sleep(1)
if os.name=='java':
    import sys
    sys.exit()

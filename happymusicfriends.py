# $Id: lullaby.py 26 2005-02-01 02:58:02Z csw $
# Copyright 2004-2018 Soon Wah Chua
import os
if os.name == 'java':
    import jplayer 
    player =  jplayer
else:
    import player

mr = player.Player()
#mr.setInstrument('Acoustic grand piano') #or mr.setInstrument(0)
mr.setInstrument(0)

print 'Let\'s play the Happy Music Friends'

notes   = (6,6,6,6,4,5,6,5,5,2,99,5,5,5,5,3,4,5,4,4,1,99,99,2,3,4,3,2,1,1,6,6,6,6,5,5,6,5,11,99,99,14,14,11,11,12,12,6,6,6.5,6.5,4,4,5,5,2,2,99,11,11,12,12,11,3,4,99)
notes_t = (4,8,8,4.1,8,8,8,8,8,4,4,4,8,8,4.1,8,8,8,8,8,4,4,8,4,8,4,8,8,4,8,8,2,8,8,8,8,4,4,4,4,2,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,4,8,4.1,8,4,4,4,4)

notes = notes * 3
notes_t = notes_t*3

notes += (3,3,3,2.5,3,4,5,5,99,4,4,4,3,4,5,6,6,99,6.5,6.5,11,6.5,6,6,12,12,99,2,2,3,4,5,6,4,4,99,99)
notes_t+=(8,8,8,8,4,8,8,2.1,4,8,8,8,8,4,8,8,2.1,4,4,4,4,4,4,8,8,2,8,4,8,4,4,2,2,1,4,4,2)

chord   = ()
chord_t = ()

mr.setTempo(150)
mr.playPiece((notes,notes_t),(chord,chord_t))

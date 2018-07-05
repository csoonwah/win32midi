# $Id: lullaby.py 30 2007-01-28 17:12:07Z csw $
# Copyright 2004-2018 Soon Wah Chua
    
import os
if os.name == 'java':
    import jplayer 
    player =  jplayer
else:
    import player

mr = player.Player()
mr.setInstrument('Acoustic grand piano') #or mr.setInstrument(0)

print 'Let\'s play the lullaby'

notes   = (3,3,5,3,3,5,3,5,11,7,   6,6,5,2,3,4,2,2,3,4,2,4,7,6,5,7,11,1,1,11,6,4,5,3,1,4,5,6,5,1,1,11,6,4,5,3,1,4,3,2,1)
notes_t = (8,8,2,8,8,2,8,8,4,4.1,8,4,4,8,8,4,4,8,8,2,8,8,8,8,4,4,2,8,8,2,8,8,2,8,8,4,4,4,2,8,8,2,8,8,2,8,8,4,4,4,2.1)

chord   = ([99],[1,3,5],[1,3,5],[1,3,5],[-15,-17,2,4],[-15,-17,2,4],[-15,-17,2,4],[-15,-17,2,4],[1,3,5],[4,6,11],[1,3,5],[-15,-17,2,4],[1,3,5],[4,6,11],[1,3,5],[-15,-17,2,4],[1,3,5])
chord_t = (4,2.1,2.1,2.1,2.1,2.1,2.1,2.1,2.1,2.1,2.1,2.1,2.1,2.1,2.1,2.1,2.1)

mr.setTempo(120)
#mr.playPiece((notes,notes_t),(chord,chord_t))
mr.playPiece2([(notes,notes_t),(chord,chord_t)])



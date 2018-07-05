# $Id: aura_lee.py 30 2007-01-28 17:12:07Z csw $
# Copyright 2004-2018 Soon Wah Chua

import os
if os.name == 'java':
    import jplayer 
    player =  jplayer
else:
    import player

mr = player.Player()
mr.setInstrument('Bright acoustic piano') #or mr.setInstrument(1)

print 'Let\'s play the Aura Lee'

notes   = (5,11,7,11,12,6,12,11,7,6,7,11,99,5,11,7,11,12,6,12,11,7,6,7,11   ,99,13,13,13,13,13,13,13,12,11,12,13,99)
notes_t = (4,4,4,4,4,4,2,4,4,4,4,2.1,4 ,4,4,4,4,4,4,2,4,4,4,4,2.1,4 , 4, 4, 2, 4, 4, 2, 4,4,4,4,2.1,4)
notes   += (13,13,14,13,12,6,12,11,7,13,12,11,99)
notes_t += (4,4,4,4,4,4,2,4,4,4,4,2.1,4)

chord   = ([1,5],[2,6],[-15,2],[1,5],[1,5],[2,6],[-15,2],[1,5],[1,5],[1,5],[-16,3],[-16,3],[-14,1],[-15,2],[1,5])
chord_t = (1    ,1    ,1     ,1    ,1    ,1    ,1     ,1    ,2    ,2    ,2     ,2     ,2     ,2     ,1    )
chord   += ([1,5],[-16,3],[2,6],[-15,2],[1,5],[99])
chord_t += (2,2,1,1,2.1,4)

mr.setTempo(144)
mr.playPiece((notes,notes_t),(chord,chord_t))

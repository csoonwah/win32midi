# Copyright 2004-2018 Soon Wah Chua
import os
if os.name == 'java':
    import jplayer 
    player =  jplayer
else:
    import player


mr = player.Player()
mr.setInstrument('Koto') #or mr.setInstrument(107)
mr.setChordInstrument('Koto') #or mr.setInstrument(107)

print 'Let\'s play the cai_shen_dao'
print 'A Chinese New Year song that means the arrival of God of Fortune'

notes   = (5,5,11,99,5,5,11,99,5,5,11,11,11,5,5,1,99,99,6,6,12,6,6,12,6,6,6,12,6,6,5,5,11,99,99)
notes_t = (4,4,2,1,4,4,2,1,4,4,4,8,8,4,4,2,1,1,4,4,2,4,4,4.1,8,4,4,4,8,8,4,4,2,1,1)

notes   += (3,3,5,11,5,6,  5,6,5,6,6,6,11,12,6,11,5,12 ,11,12 ,12,13,12,11,7,6,11,6,11,11,12,11,6,5,5,2,2,3,5,3,11,5,6,13,12,13,13,12,13,12,12,11,6,5,6,12,11,11,99,99)
notes_t += (4,8,8,4 ,4,4.1,8,8,8,4,4,8,8 ,4 ,8,8 ,1,4.1,8 ,4.1,8 ,8,8,8,8,2,4.1,8,4.1,8,8,8,8,8,2,4,8,8,4,4,4.1,8,2,4.1,8,2,4.1,8,2,4,8,8,4,4,2,2,1,1,1,1)

C=[1,3,5]
Dm=[2,4,6]
Am=[-16,1,3]
G7=[-15,-17,2,2.5]
F=[4,6,11]

chord = (C,)*8
chord_t = (1,)*8
chord += (Dm,)*3 + (C,)*4 +(Am,) + (Dm,) +(G7,) + (Dm,)
chord_t+= (1,)*11
chord += (Am,) + (F,) +(G7,) +(Dm,) +(Am,)+(C,)*2 + (Dm,) + (F,) +(G7,) +(C,)*4
chord_t += (1,)*8 + (2,)*2 + (1,)*4

mr.setTempo(180)
mr.playPiece2([(notes,notes_t),(chord,chord_t)])

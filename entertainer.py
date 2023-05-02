# Copyright 2004-2018 Soon Wah Chua
import player

mr = player.Player()
# mr.setInstrument('Piano')
# or mr.setInstrument(107)
# mr.setChordInstrument('Piano')
mr.setChordInstrument(1)

print('Let\'s play the Entertainer')

notes = (12, 13, 11, 6, 6, 7, 5, 12, 13, 11, 6, 6, 7, 5)
notes_t = (8, 8, 8, 8, 8, 8, 4, 8, 8, 8, 8, 8, 8, 4)

notes += (2, 3, 1, -16, -16, -17, 99, 99, [-17, 4, 5], 2, 2.5)
notes_t += (8, 8, 8, 8, 8, 8, 4, 2, 4, 8, 8)

notesA = (3, 11, 3, 11, 3, 11, 11, 11, 11, 12, 12.5, 13, 11, 12, 13, 13, 7, 12)
notes_tA = (8, 4, 8, 4, 8, 8, 2, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 4)

notesA += (11, 2, 2.5, 3, 11, 3, 11, 3, 11, 11, 6, 5)
notes_tA += (2.1, 8, 8, 8, 4, 8, 4, 8, 8, 2.1, 8, 8)

notesA += (4.5, 6, 11, 13, 13, 12, 11, 6, [4, 12], 2, 2.5, 3, 11, 3, 11, 3, 11)
notes_tA += (8, 8, 8, 8, 8, 8, 8, 8, 2.1, 8, 8, 8, 4, 8, 4, 8, 8)

notesA += (11, 11, 11, 12, 12.5, 13, 11, 12, 13, 13, 7, 12, 11, 11, 12)
notes_tA += (2, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 4, 2.1, 8, 8)

notesA += (13, 11, 12, 13, 13, 11, 12, 11, 13, 11, 12, 13, 13, 11, 12, 11)
notes_tA += (8,) * 16

notesA += (13, 11, 12, 13, 13, 7, 12)
notes_tA += (8, 8, 8, 8, 8, 8, 4)

notes1 = (11, 2, 2.5)
notes_t1 = (2.1, 8, 8)

notes2 = (11, 99)
notes_t2 = (2.1, 4)

notes += notesA + notes1
notes_t += notes_tA + notes_t1

notes += notesA + notes2
notes_t += notes_tA + notes_t2

chord = (99, 99)
chord_t = (1, 1)
chord += (99, 99, 6, 5.5, 5, 99, -15, 99)
chord_t += (2, 4, 8, 8, 4, 4, 4, 4)

chordA = (1, [3, 5], 1, [3, 6.5], 1, [4, 6], [3, 5], 99, [1, 3, 5], 99,
          [-17, 4, 5], 99)
chord_tA = (4,) * 12
chordA += (1, [3, 5], [3, 5], 99, 1, [3, 5], 1, [3, 6.5], 1, [4, 6],
           [3, 5], 99)
chord_tA += (4,) * 12
chordA += (2, [4.5, 6], 2, [4.5, 6], 5, -15, -14, -13, 1, [3, 5], 1, [3, 6.5])
chord_tA += (4,) * 12
chordA += (1, [4, 6], [3, 5], 99, [1, 3, 5], 99, [-17, 4, 5], 99, 1, [3, 5],
           [3, 5], 99)
chord_tA += (4,) * 12
chordA += (11, [6.5, 11], [6, 11], [5.5, 11])
chord_tA += (2,) * 4
chordA += ([5, 11], 99, [-17, 4, 5], 99)
chord_tA += (4,) * 4

chord1 = ([1, 3, 5], -15, -16, -17)
chord_t1 = (4,) * 4

chord2 = ([1, 3, 5], -15, -21, 99)
chord_t2 = (4,) * 4

chord += chordA + chord1
chord_t += chord_tA + chord_t1
chord += chordA + chord2
chord_t += chord_tA + chord_t2

mr.setTempo(180)
# mr.playPiece((notes,notes_t),(chord,chord_t))
mr.playPiece2([(notes, notes_t), (chord, chord_t)])

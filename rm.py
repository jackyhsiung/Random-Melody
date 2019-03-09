from pyknon.genmidi import Midi
from pyknon.music import NoteSeq, Note
#a = NoteSeq("C3 D5 E5 F5")

root = input('Enter the root of the chord: ')
chord = input('What kind of chord:(Maj7/m7) ')
# Set Interval Relationships in Appregio Notes 
half_steps = []
notes_5th = []
if chord == 'Maj7':
	half_steps = [0, 4, 7 ,11]
	notes_5th = [7, 7, 7, 6]
elif chord == 'm7':
	half_steps = [0, 3, 7, 10]
	notes_5th = [7, 7, 7, 7]
sequence = []
for a, b in zip(half_steps, notes_5th):
	sequence.append(Note(a))
	sequence.append(Note(a).transposition(b))

notes3 = NoteSeq(sequence)
midi = Midi(number_tracks=1, tempo=90)
midi.seq_notes(notes3, track=0)
midi.write("demo3.mid")

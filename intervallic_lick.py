from pyknon.genmidi import Midi
from pyknon.music import NoteSeq, Note
#a = NoteSeq("C3 D5 E5 F5")

#Let User Input the Chord
def user_input():
	root = input('Enter the root of the chord: ')
	chord = input('What kind of chord:(maj7/m7) ')
	if root == 'C':
		root = 0
	elif root == 'C#' or root == 'Db':
		root = 1
	elif root == 'D':
		root = 2
	elif root == 'D#' or root == 'Eb':
		root = 3
	elif root == 'E':
		root = 4
	elif root == 'F':
		root = 5
	elif root == 'F#' or root == 'Gb':
		root = 6
	elif root == 'G':
		root = 7
	elif root == 'G#' or root == 'Ab':
		root = 8
	elif root == 'A':
		root = 9
	elif root == 'A#' or root == 'Bb':
		root = 10 
	elif root == 'B':
		root = 11
	# Set Interval Relationships in Appregio Notes 
	appregio_notes = []
	notes_5th = []
	if chord == 'maj7':
		appregio_notes = [root, root+4, root+7 ,root+11]
		notes_5th = [7, 7, 7, 6]
	elif chord == 'm7':
		appregio_notes = [root, root+3, root+7, root+10]
		notes_5th = [7, 7, 7, 7]
	elif chord == '7':
		appregio_notes = [root, root+4, root+7, root+10]
	elif chord == 'm7-5':
		appregio_notes = [root, root+3, root+6, root+10]
	notes_and_5th = [appregio_notes, notes_5th]
	return notes_and_5th 
	
def form_seq(appregio_notes, notes_5th):
	sequence = []
	for a, b in zip(appregio_notes, notes_5th):
		sequence.append(Note(a).stretch_dur(0.5))
		sequence.append(Note(a).stretch_dur(0.5).transposition(b))
	notes = NoteSeq(sequence)
	return notes

def gen_midi(notes, filename):
	midi = Midi(number_tracks=1, tempo=90)
	midi.seq_notes(notes, track=0)
	midi.write(filename)

def main():
	notes_and_5th = user_input()
	appregio_notes = notes_and_5th[0]
	notes_5th = notes_and_5th[1]
	notes = form_seq(appregio_notes, notes_5th)
	gen_midi(notes, 'Gmaj7_5th_8.mid')

main()

from pyknon.genmidi import Midi
from pyknon.music import NoteSeq, Note
import random

#Let User Input the Chord
def user_input():
	root = input('Enter the root of the chord: ')
	# chord = input('What kind of chord:(maj7/m7) ')
	if root == 'C':
		root_i = 0
	elif root == 'C#' or root == 'Db':
		root_i = 1
	elif root == 'D':
		root_i = 2
	elif root == 'D#' or root == 'Eb':
		root_i = 3
	elif root == 'E':
		root_i = 4
	elif root == 'F':
		root_i = 5
	elif root == 'F#' or root == 'Gb':
		root_i = 6
	elif root == 'G':
		root_i = 7
	elif root == 'G#' or root == 'Ab':
		root_i = 8
	elif root == 'A':
		root_i = 9
	elif root == 'A#' or root == 'Bb':
		root_i = 10 
	elif root == 'B':
		root_i = 11
	return root, root_i

def extended_notes(root):
	# chord = input('What kind of chord:(maj7/m7) ')
	major_scale = [root, root+2, root+4, root+5, root+7, root+9, root+11]
	index = [0, 2, 4, 6] #1 3 5 7
	extended_index = [4, 5] #3 5 6
	combined_index = []
	for i in index:
		r = random.choice(extended_index)
		combined_index.append(i)
		combined_index.append((i+r)%7)
	print(combined_index)
	appregio_notes = []
	for i in combined_index:
		appregio_notes.append(major_scale[i])
	print(appregio_notes)
	return appregio_notes

def form_seq(appregio_notes):
	sequence = []
	# for a, b in zip(appregio_notes, notes_5th):
	# 	sequence.append(Note(a).stretch_dur(0.5))
	# 	sequence.append(Note(a).stretch_dur(0.5).transposition(b))
	for i in appregio_notes:
		sequence.append(Note(i, 5, 0.125/2, 100))
	notes = NoteSeq(sequence)
	print(notes)
	return notes

def gen_midi(notes, filename):
	midi = Midi(number_tracks=1, tempo=90)
	midi.seq_notes(notes, track=0)
	midi.write(filename)

def main():
	root, root_i = user_input()
	appregio_notes = extended_notes(root_i)
	notes = form_seq(appregio_notes)
	gen_midi(notes, '{}maj7extended.mid'.format(root))

main()






from pyknon.genmidi import Midi
from pyknon.music import NoteSeq, Note
import random

def random_melody(note_list, octave_low, octave_high, dur_list):
	rm = NoteSeq() #[]
	melody_len = 0
	while melody_len < 8: # while True if break bug
		pitch = random.choice(note_list) #refactor by root +2 +4 ...
		octave = random.randint(octave_low, octave_high)
		dur = random.choice(dur_list)
		vol = random.randrange(80, 125, 5) #refactor
		print([pitch, octave, dur, vol])
		rm.append(Note(pitch, octave, dur, vol))
		melody_len += dur
	print(melody_len)
	print(rm)
	return rm

def gen_midi(rm, filename):
	midi = Midi(number_tracks=1, tempo=120)
	midi.seq_notes(rm, track=0) # no more than 0
	midi.write(filename)

def main():
	note_list = [0, 2, 4, 5, 7, 9, 11] #refactor by root +2 +4 ...
	octave_low = 5
	octave_high = 6
	dur_list = [0.125, 0.25, 0.5]
	rm = random_melody(note_list, octave_low, octave_high, dur_list)
	print(rm)
	gen_midi(rm, 'random_melody_in_C.mid')

main()

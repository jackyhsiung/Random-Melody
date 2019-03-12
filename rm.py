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

def chord_prog(chords_note):
	cprog6251 = NoteSeq()
	count = 0
	while count < 2: # while true if break
		for i in chords_note:
			cprog6251.append(Note(i, 4, 1, 100))
		count += 1
	return cprog6251

def gen_midi(rm, cprogr, cprog3, filename):
	midi = Midi(number_tracks=3, tempo=120)
	midi.seq_notes(rm, track=0) 
	midi.seq_notes(cprogr, track=1) 
	midi.seq_notes(cprog3, track=2) 
	midi.write(filename)

def main():
	note_list = [0, 2, 4, 5, 7, 9, 11] #refactor by root +2 +4 ...
	octave_low = 5
	octave_high = 6
	dur_list = [0.125, 0.25, 0.5]
	rm = random_melody(note_list, octave_low, octave_high, dur_list)
	print(rm)
	cprog6251r = chord_prog([9, 2, 7, 0])
	cprog62513 = chord_prog([0, 5, 11, 4])
	gen_midi(rm, cprog6251r, cprog62513, 'random_melody_in_C_2.mid')

main()

# c = Note(0)
# print(c)
# print(NoteSeq([c]))
# c_major_scale = NoteSeq('C D E F G A B')
# cmaj = Note(0).harmonize(c_major_scale)
# print(cmaj)
# print(cmaj[1])

# #chord progression
# cprog6251 = NoteSeq()
# for i in [9, 2 , 7, 0]:
# 	cprog6251.append(Note(i, 4, 1, 100))
# print(cprog6251)




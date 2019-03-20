from pyknon.genmidi import Midi
from pyknon.music import NoteSeq, Note, Rest
import random

def random_melody(note_list, octave_low, octave_high, dur_list):
	rm_seq = NoteSeq() #[]
	rm_data = []
	melody_len = 0
	while melody_len < 8: # while True if break bug
		pitch = random.choice(note_list) #refactor by root +2 +4 ...
		octave = random.randint(octave_low, octave_high)
		dur = random.choice(dur_list)
		vol = random.randrange(80, 125, 5) #refactor
		print([pitch, octave, dur, vol])
		rm_seq.append(Note(pitch, octave, dur, vol)) #refactor
		rm_data.append([pitch, octave, dur, vol])
		melody_len += dur
	print(melody_len)
	rm = [rm_seq, rm_data]
	return rm

def chord_prog(chords_note):
	cprog6251 = NoteSeq()
	count = 0
	while count < 2: # while true if break
		for i in chords_note:
			cprog6251.append(Note(i, 4, 1, 100))
		count += 1
	return cprog6251

def fusion_prog(rm_data, root, seventh, nine):
	# def append_note(seq_name, p, r, note):
	# 	seqname.append(Note(p[0] - r + note, 4, 1, 100))
	# note indicates which note in the chord you want to put in the seq
	fsprogr = NoteSeq()
	fsprog7 = NoteSeq()
	fsprog9 = NoteSeq()
	fsprog = [fsprogr,fsprog7, fsprog9]
	# the note of melody could be the 1, b3, 3, 5, b7, 7th of the chord 
	pitch_in_chord = [0, 3, 4, 7, 10, 11]
	melody_len = 0
	r = random.choice(pitch_in_chord)
	#print(r)
	ro = random.choice(root)
	se = random.choice(seventh)
	fsprogr.append(Note(rm_data[0][0] - r + ro, 4, 1, 100))
	fsprog7.append(Note(rm_data[0][0] - r + se, 4, 1, 100))
	fsprog9.append(Note(rm_data[0][0] - r + 14, 4, 1, 100))
	for p in rm_data:
		melody_len += p[2]
		#print(melody_len)
		r = random.choice(pitch_in_chord)
		se = random.choice(seventh)
		#print(r)
		for i in range(1, 8):
			if p[2] == 0.125:
				if melody_len - 0.125 == i:
					fsprogr.append(Note(p[0] - r, 4, 1, 100))
					fsprog7.append(Note(p[0] - r + se, 4, 1, 100))
					fsprog9.append(Note(p[0] - r + 14, 4, 1, 100))
			if p[2] == 0.25:
				if melody_len - 0.25 == i:
					fsprogr.append(Note(p[0] - r, 4, 1, 100))
					fsprog7.append(Note(p[0] - r + se, 4, 1, 100))
					fsprog9.append(Note(p[0] - r + 14, 4, 1, 100))
				if melody_len - 0.25 == i - 0.125:
					fsprogr.append(Note(p[0] - r, 4, 1, 100))
					fsprog7.append(Note(p[0] - r + se, 4, 1, 100))
					fsprog9.append(Note(p[0] - r + 14, 4, 1, 100))
			if p[2] == 0.5:
				if melody_len - 0.5 == i:
					fsprogr.append(Note(p[0] - r, 4, 1, 100))
					fsprog7.append(Note(p[0] - r + se, 4, 1, 100))
					fsprog9.append(Note(p[0] - r + 14, 4, 1, 100))
				if melody_len - 0.5 == i - 0.125:
					fsprogr.append(Note(p[0] - r, 4, 1, 100))
					fsprog7.append(Note(p[0] - r + se, 4, 1, 100))
					fsprog9.append(Note(p[0] - r + 14, 4, 1, 100))
				if melody_len - 0.5 == i - 0.25:
					fsprogr.append(Note(p[0] - r, 4, 1, 100))
					fsprog7.append(Note(p[0] - r + se, 4, 1, 100))
					fsprog9.append(Note(p[0] - r + 14, 4, 1, 100))
				if melody_len - 0.5 == i - 0.375:
					fsprogr.append(Note(p[0] - r, 4, 1, 100))
					fsprog7.append(Note(p[0] - r + se, 4, 1, 100)) 
					fsprog9.append(Note(p[0] - r + 14, 4, 1, 100))
	return fsprog

def fusion_prog_rym(rm_data, root, seventh, nine):
	# note indicates which note in the chord you want to put in the seq
	fsprogr = NoteSeq()
	fsprog7 = NoteSeq()
	fsprog9 = NoteSeq()
	fsprog = [fsprogr,fsprog7, fsprog9]
	# the note of melody could be the 1, b3, 3, 5, b7, 7th of the chord 
	pitch_in_chord = [0, 3, 4, 7, 10, 11]
	melody_len = 0
	for p in rm_data:
		melody_len += p[2]
		r = random.choice(pitch_in_chord)
		se = random.choice(seventh)
		if p[2] == 0.25:
			fsprogr.append(Note(p[0] - r, 4, p[2], 100))
			fsprog7.append(Note(p[0] - r + se, 4, p[2], 100))
			fsprog9.append(Note(p[0] - r + 14, 4, p[2], 100))
		elif p[2] == 0.5:
			fsprogr.append(Note(p[0] - r, 4, p[2], 100))
			fsprog7.append(Note(p[0] - r + se, 4, p[2], 100))
			fsprog9.append(Note(p[0] - r + 14, 4, p[2], 100))
		elif p[2] == 0.125:
			fsprogr.append(Rest(p[2]))
			fsprog7.append(Rest(p[2]))
			fsprog9.append(Rest(p[2]))			
	return fsprog

def store_rm(rm_data, filename):
	with open(filename, 'w') as f:
		f.write('pitch,octave,dur,vol\n')
		for p in rm_data:
			f.write(str(p[0]) + ',' + str(p[1])\
			+ ',' + str(p[2]) + ',' + str(p[3]) + '\n')

def open_rm(filename):
	rm_data = []
	with open(filename, 'r') as f:
		for line in f:
			if 'pitch,octave,dur,vol' in line:
				continue
			pitch, octave, dur, vol = line.strip().split(',')
			rm_data.append([int(pitch), int(octave), float(dur), int(vol)])
	return rm_data

def gen_midi(rm_seq, cprogr, cprog3, cprog9, filename):
	midi = Midi(number_tracks=4, tempo=120)
	midi.seq_notes(rm_seq, track=0) 
	midi.seq_notes(cprogr, track=1) 
	midi.seq_notes(cprog3, track=2) 
	midi.seq_notes(cprog9, track=3)
	midi.write(filename)

def main():
	new = input('Do you want to creat a new random melody? ')
	if new == 'y':	
		note_list = [0, 2, 4, 6, 7, 9, 11] #refactor by root +2 +4 ...
		octave_low = 5
		octave_high = 6
		dur_list = [0.125, 0.25, 0.5]
		rm = random_melody(note_list, octave_low, octave_high, dur_list)
		rm_seq, rm_data = rm
		print(rm_seq)
		store_rm(rm_data, 'random_melody_in_G_1_data.csv')
	elif new == 'n':
		rm_data = open_rm('random_melody_in_C_3_data.csv')
		rm_seq = NoteSeq() #rm_seq = NoteSeq([Note(int(p[0])) for p in rm_data])
		for p in rm_data:
			rm_seq.append(Note(p[0], p[1], p[2], p[3]))
		print(rm_seq)
	# cprog6251r = chord_prog([9, 2, 7, 0])
	# cprog62513 = chord_prog([0, 5, 11, 4]) #inversion 9 0 
	# gen_midi(rm_seq, cprog6251r, cprog62513, 'random_melody_in_C_3.mid')
	fsprog = fusion_prog_rym(rm_data, [0], [10, 11], [14])
	fsprogr, fsprog7, fsprog9 = fsprog
	gen_midi(rm_seq, fsprogr, fsprog7, fsprog9, 'random_melody_in_C_3_2.mid')

main()

# c = Note(0)
# print(c)
# print(NoteSeq([c]))
# c_major_scale = NoteSeq('C D E F G A B')
# cmaj = Note(0).harmonize(c_major_scale)
# print(cmaj)
# print(cmaj[1])

#!/usr/bin/env python

from midiutil import MIDIFile
from os import getpid
from mingus.core import chords
from random import choice, seed, random
from sys import argv

NOTES = ['C', 'C#', 'D', 'Eb', 'E', 'F', 'F#', 'G', 'Ab', 'A', 'Bb', 'B']
OCTAVES = list(range(11))
NOTES_IN_OCTAVE = len(NOTES)

def _make_chord_numbers():
    chord_numbers = []

    for chord in ("I", "II", "III", "IV", "V", "VI", "VII"):
        chord_numbers.append(chord)
        chord_numbers.append(chord + "7")

        # sure, these *can* be minor but it doesn't make sense to mingus so...
        if chord not in ('I', 'IV', 'V'):
            chord_numbers.append(chord.lower())
            chord_numbers.append(chord.lower() + "7")

    return chord_numbers

def main(hex_seed):
    seed(hex_seed)

    track    = 0
    channel  = 0
    time     = 0   # In beats
    duration = 4   # In beats
    tempo    = 60  # In BPM
    volume   = 100 # 0-127, as per the MIDI standard
    bass_instrument = 33 # 33 - 40 per General MIDI

    MyMIDI = MIDIFile(2) # One track, defaults to format 1 (tempo track
                         # automatically created)

    MyMIDI.addTempo(track, time, tempo)
    MyMIDI.addProgramChange(track + 1, channel + 1, time, bass_instrument)

    octave = switch_octave()
    chord_numbers = _make_chord_numbers()
    inversions = ["first_inversion", "second_inversion", "third_inversion"]

    key = choice(NOTES)

    for i in range(0, 16):
        chord = call_random_method_kwargs(chords, chord_numbers, key=key)
        bass_note = chord[0]
        print(f'{chord} -> {bass_note}')
        inversion = call_random_method_args(chords, inversions, chord)

        # add chord
        for note in inversion:
            pitch = note_to_number(note, octave)
            duration = choice(range(2, 8))
            MyMIDI.addNote(track, channel, pitch, time, duration, volume)

        # add bass note
        MyMIDI.addNote(track + 1, channel + 1, note_to_number(bass_note, octave-1), time, 4, volume)

        time = time + 4
        key = swap_accidentals(choice(inversion))
        octave = switch_octave(octave)

    with open("atmospheric-chords-" + hex_seed + ".mid", "wb") as output_file:
        MyMIDI.writeFile(output_file)

ACCIDENTALS = {
    "Db": "C#",
    "D#": "Eb",
    "E#": "F",
    "Gb": "F#",
    "G#": "Ab",
    "A#": "Bb",
    "B#": "C",
}

def swap_accidentals(note):
    return ACCIDENTALS.get(note, note)

def note_to_number(note: str, octave: int) -> int:
    note = swap_accidentals(note)
    assert note in NOTES, errors['notes']
    assert octave in OCTAVES, errors['notes']

    note = NOTES.index(note)
    note += (NOTES_IN_OCTAVE * octave)

    assert 0 <= note <= 127, errors['notes']

    return note

def call_random_method_kwargs(obj, source, **kwargs):
    method_name = choice(source)
    method = getattr(obj, method_name)
    return method(**kwargs)

def call_random_method_args(obj, source, *args):
    method_name = choice(source)
    method = getattr(obj, method_name)
    return method(*args)

def switch_octave(octave=0):
    val = random()

    if val < 0.20:
        octave -= 1
    elif val > 0.80:
        octave += 1

    if octave < 2 or octave > 6:
        octave = choice([2, 3, 4])

    return octave

if __name__ == "__main__":
    main(argv[1])


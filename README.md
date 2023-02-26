## GenMIDIPython

This is a small and simple project generating MIDI songs from Python. It may
expand. It may not. But you can use it now.

## Installation

With a relatively recent Python (I used Python 3.10.8). Install
[mingus](https://pypi.org/project/mingus/) and
[MIDIUtil](https://pypi.org/project/MIDIUtil/). Then you should be ready to go.

Alternately, I've created an ActiveState project at
[chromatic/GenMIDIPython](https://platform.activestate.com/chromatic/GenMIDIPython/distributions).
Follow the instructions there. This can be easier for Windows and Mac users who
are not already experienced Python developers.

## Usage

Run `python3 gen_atmospheric_chords.py <seed>` with a seed value. This can be
an integer or hexadecimal value. Python will convert it into a seed for the
random number generator and generate a MIDI file named
`atmospheric-chords-<seed>.mid`. The seed should generate the same value for
every run, at least unless you change the version of Python out from under
things.

Use a MIDI player such as [VLC](https://www.videolan.org/vlc/) or
[FluidSynth](https://www.fluidsynth.org/) to play the file. You can use any
SoundFont 2 pack you like, though I prefer atmospheric synth sounds.

## License

MIT; see `LICENSE`.

## Copyright

Copyright (c) 2023 chromatic. Some rights reserved. See `LICENSE`.

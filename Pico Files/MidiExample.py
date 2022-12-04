#import usb_midi
import adafruit_midi
from adafruit_midi.note_on          import NoteOn
from adafruit_midi.note_off         import NoteOff
from time import sleep

midi = adafruit_midi.MIDI(midi_out=usb_midi.ports[1], out_channel=0)

while True:
    #NoteOn / Off (Note, Velocity)
    midi.send(NoteOn(60, 120))
    sleep(0.5)
    midi.send(NoteOff(60, 120))
    sleep(0.5)
    
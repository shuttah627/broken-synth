import mido
import random

mid = mido.MidiFile("test.mid")

for track in mid.tracks:
    for msg in track:
        if (msg.type == 'program_change'):
            msg.program = random.randint(0,127)

mid.save('ohjesusohfuckwhathaveidone.mid')



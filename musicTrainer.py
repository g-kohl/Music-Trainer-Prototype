import random
import time

mode = input("With which mode do you want to train: notes (1), arpeggios(2), scales(3) or chords(4)?")
repetitions = input("How many repetitions do you want to do?")
interval = int(input("How much time (seconds) do you want between exercises?"))

strings = ["E", "A", "D", "G", "B", "e"]
notes = ["Ab", "A", "A#", "Bb", "B", "C", "C#", "Db", "D", "D#", "Eb", "E", "F", "F#", "Gb", "G", "G#"]
arpeggios = ["Major(M)", "Minor(m)", "Diminished(°)", "Augmented(+)"]
scales = ["Major", "Minor", "Harmonic Minor", "Melodic Minor"]
degrees = ["1st", "2nd", "3rd", "4th", "5th", "6th", "7th"]
chords = ["7", "M7", "m7", "mM7", "7 (5#)", "M7 (5#)", "m7 (b5)", "°"]

for x in range(int(repetitions)):
    if mode == "1":
        print("play a(n)" + notes[random.randrange(0,17)] + " on the " + strings[random.randrange(0, 6)] + " string.")
        time.sleep(interval)
    elif mode == "2":
        print("play a(n) " + notes[random.randrange(0,17)] + " " + arpeggios[random.randrange(0,4)] + " arpeggio starting from the " + strings[random.randrange(0, 6)] + " string.")
        time.sleep(interval)
    elif mode == "3":
        print("play the " + degrees[random.randrange(0,7)] + " degree of the " + notes[random.randrange(0,17)] + " " + scales[random.randrange(0,4)] + " scale starting from the " + strings[random.randrange(0, 6)] + " string.")
        time.sleep(interval)
    elif mode == "4":
        print("play a(n) " + notes[random.randrange(0,17)] + chords[random.randrange(0,8)] + " chord starting from the " + strings[random.randrange(0, 3)] + " string.")
        time.sleep(interval)

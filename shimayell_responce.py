#!/usr/bin/env python3

import csv
import subprocess


with open(r'voices/speakers.csv', 'r') as f:
    reader = next(csv.reader(f))
    speakers = { line[0] : line[1] for line in reader if line }
    print('speakers: ', speakers)

voices = {}
for folderName in set(speakers.values()):
    voices[folderName] = {}
    with open(r'voices/{}/voices.csv'.format(folderName), 'r') as f:
        reader = next(csv.reader(f))
        voices[folderName] = { line[0] : line[1] for line in reader }
    print('voices[', folderName, ']: ', voices[folderName])

speaker = speaker.keys()[0]

def is_end_text(text):
    return text in ['goodbye', 'bye-bye', 'ばいばい', 'バイバイ']


def responce(text):
    if text in talks:
        print('aplay', r'./audios/' + talks[text])
        subprocess.run(['aplay', r'./audios/' + talks[text]])
    else:
        print('sorry not find.')

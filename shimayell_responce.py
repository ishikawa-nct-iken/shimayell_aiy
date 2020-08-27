#!/usr/bin/env python3

import csv
import subprocess


with open(r'voices/speakers.csv', 'r') as f:
    reader = csv.reader(f)
    header = next(reader)
    speakers = { line[0] : line[1] for line in reader if line }
    print('speakers: ', speakers)

voices = {}
for folderName in set(speakers.values()):
    voices[folderName] = {}
    with open(r'voices/{}/voices.csv'.format(folderName), 'r') as f:
        reader = csv.reader(f)
        header = next(reader)
        voices[folderName] = { line[0] : line[1] for line in reader }
    print('voices[', folderName, ']: ', voices[folderName])

speaker = list(speakers.keys())[0]

def is_end_text(text):
    return text in ['goodbye', 'bye-bye', 'ばいばい', 'バイバイ']


def responce(text):
    if text in talks:
        filePath = r'voices/' + speakers[speaker] + r'/' + talks[text]
        print('aplay', filePath)
        subprocess.run(['aplay', filePath])
    else:
        print('not find file.')

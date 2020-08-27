#!/usr/bin/env python3

import csv
import subprocess
import re


with open(r'voices/speakers.csv', 'r') as f:
    reader = csv.reader(f)
    header = next(reader)
    speakers = { line[0] : line[1] for line in reader}
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


with open(r'voices/end_texts.txt', 'r') as f:
    reader = csv.reader(f)
    end_texts = [ end_text for end_text in f ]
    print('end_texts: ', end_texts)

def is_end_text(text):
    return text in end_texts



change_speaker_pattern = r'.+(?=[にへ]変更)'
change_speaker_repatter = re.compile(change_speaker_pattern)

def change_speaker(text):
    result = change_speaker_repatter.match(text)
    if result and result.group() in speakers:
        return True
    
    return False



def responce(text):
    if text in voices[speakers[speaker]]:
        filePath = r'voices/' + speakers[speaker] + r'/' + voices[speakers[speaker]][text]
        print('aplay', filePath)
        subprocess.run(['aplay', filePath])
    else:
        print('not find file.')

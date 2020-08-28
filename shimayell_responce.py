#!/usr/bin/env python3

import os
import csv
import subprocess
import re
import random


with open(r'voices/speakers.csv', 'r') as f:
    reader = csv.reader(f)
    header = next(reader)
    speakers = { line[0] : line[1] for line in reader}
    print('speakers: ', speakers)

speaker = '@default'
print('speaker is', speaker)

voices = {}
for folderName in set(speakers.values()):
    with open(r'voices/{}/voices.csv'.format(folderName), 'r') as f:
        reader = csv.reader(f)
        header = next(reader)
        voices[folderName] = { line[0] : line[1] for line in reader }
    print('voices[', folderName, ']: ', voices[folderName])


with open(r'voices/end_texts.txt', 'r') as f:
    reader = csv.reader(f)
    end_texts = [ end_text for end_text in f.read().splitlines() ]
    print('end_texts: ', end_texts)

def is_end_text(text):
    return text in end_texts



change_speaker_pattern = r'.+(?=[にへ]変更)'
change_speaker_repatter = re.compile(change_speaker_pattern)

def change_speaker(text):
    result = change_speaker_repatter.match(text)
    if result and result.group() in speakers:
        global speaker
        speaker = result.group()
        print('change speaker to', speaker)
        return True
    return False


def responce(text):
    print(speaker)
    print(speakers[speaker])
    print(voices[speakers[speaker]])
    if text in voices[speakers[speaker]]:
        path = r'voices/' + speakers[speaker] + r'/' + voices[speakers[speaker]][text]
        if os.path.isfile(path):
            play_voice(path)
        elif os.path.isdir(path):
            filespath = [os.path.join(path, f) for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
            if len(filespath) == 0:
                print('not find any file in', path, '.')
            else:
                play_voice(filespath)
        else:
            print('not find', path, '.')
    else:
        print('not find talk.')

def play_voice(filepath):
    _, ext = os.path.splitext(filepath)
    if ext == '.wav':
        print('aplay', filepath)
        subprocess.run(['aplay', filepath])
    elif ext == '.mp3':
        print('mpg321', filepath)
        subprocess.run(['mpg321', filepath])

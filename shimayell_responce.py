#!/usr/bin/env python3

from os import path
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
    csvpath = r'voices/{}/voices.csv'.format(folderName)
    if path.isfile(csvpath):
        with open(csvpath, 'r') as f:
            reader = csv.reader(f)
            header = next(reader)
            voices[folderName] = { line[0] : line[1] for line in reader }
        print('voices[', folderName, ']: ', voices[folderName])


with open(r'voices/end_texts.txt', 'r') as f:
    reader = csv.reader(f)
    end_texts = [ end_text for end_text in f.read().splitlines() ]
    print('end_texts: ', end_texts)

start()

def start():
    play('start')

def responce(text):
    print('speaker is', speaker)

    if change_speaker(text):
        return

    if text in voices[speakers[speaker]]:
        voicepath = r'voices/' + speakers[speaker] + r'/' + voices[speakers[speaker]][text]
        play(voicepath)
    else:
        print('not find talk.')

def is_end_text(text):
    return text in end_texts

change_speaker_pattern = r'.+(?=[にへ](変更|変えて))'
change_speaker_repatter = re.compile(change_speaker_pattern)

def change_speaker(text):
    result = change_speaker_repatter.match(text)
    if result and result.group() in speakers:
        global speaker
        if speaker != result.group():
            speaker = result.group()
            print('change speaker to', speaker)
            start()
            return True
    return False


def play(voicepath, put_error = true):
    if path.isfile(voicepath):
        play_voice(voicepath)
    elif path.isdir(voicepath):
        filespath = [path.join(voicepath, f) for f in os.listdir(voicepath) if os.path.isfile(os.path.join(voicepath, f))]
        if len(filespath) == 0:
            if put_error:
                print('not find any file in', voicepath, '.')
        else:
            play_voice(filespath)
    else:
        if put_error:
            print('not find', voicepath, '.')

def play_voice(filepath):
    _, ext = path.splitext(filepath)
    if ext == '.wav':
        print('aplay', filepath)
        subprocess.run(['aplay', filepath])
    elif ext == '.mp3':
        print('mpg321', filepath)
        subprocess.run(['mpg321', filepath])

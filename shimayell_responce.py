#!/usr/bin/env python3

from os import path
import csv
import re
from play_voice import play_voice, start


def init():
    """
    初期化する．
    """
    global speakers
    with open(r'voices/speakers.csv', 'r') as f:
        reader = csv.reader(f)
        header = next(reader)
        speakers = { line[0] : line[1] for line in reader}
        print('speakers:', speakers)

    global speaker
    speaker = '@default'

    global voices
    voices = {}
    for folderName in set(speakers.values()):
        csvpath = path.join('voices',folderName,'voices.csv')
        if path.isfile(csvpath):
            with open(csvpath, 'r') as f:
                reader = csv.reader(f)
                header = next(reader)
                voices[folderName] = { line[0] : line[1] for line in reader }
            print('voices[', folderName, ']:', voices[folderName])

    global end_texts
    with open(r'voices/end_texts.txt', 'r') as f:
        reader = csv.reader(f)
        end_texts = [ end_text for end_text in f.read().splitlines() ]
        print('end_texts:', end_texts)


def change_speaker(text):
    """
    話者を変更する．

    Parameters
    ----------
    text : str
        利用者のボイステキスト．
    """
    result = change_speaker_repatter.match(text)
    if result and result.group() in speakers:
        global speaker
        if speaker != result.group():
            speaker = result.group()
            print('change speaker to', speaker)
            start()
            return True
    return False


change_speaker_pattern = r'.+(?=[にへ](変更|変えて))'
change_speaker_repatter = re.compile(change_speaker_pattern)
def is_end_text(text):
    """
    終了の言葉かどうか．

    Parameters
    ----------
    text : str
        利用者のボイステキスト．

    Returns
    -------
    is_end : bool
        終了の言葉かどうか．
    """
    return text in end_texts


def responce(text):
    """
    返事をする．

    Parameters
    ----------
    text : str
        利用者のボイステキスト．
    """
    print('speaker is', speaker)

    if change_speaker(text):
        return

    if text in voices[speakers[speaker]]:
        play_voice(path.join(speakers[speaker], voices[speakers[speaker]][text]))
    else:
        print('not find talk.')


init()

start()

#!/usr/bin/env python3

from os import path
import csv
import re
from play_voice import play_voice, start, end, end_sleep

homepath = path.dirname(__file__)

def init():
    """
    初期化する．
    """
    global speakers
    with open(path.join(homepath, r'voices/speakers.csv'), 'r', encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader)
        speakers = { line[0] : line[1] for line in reader}
        # print('speakers:', speakers)

    global speaker
    speaker = '@default'

    global voices
    voices = {}
    for folderName in set(speakers.values()):
        # print('folderName: {}'.format(folderName))
        csvpath = path.join(homepath, 'voices', folderName, 'voices.csv')
        if path.isfile(csvpath):
            with open(csvpath, 'r', encoding="utf-8") as f:
                reader = csv.reader(f)
                header = next(reader)
                voices[folderName] = { line[0] : line[1] for line in reader if len(line) == 2 }
            # print('voices[', folderName, ']:', voices[folderName])

    global end_texts
    with open(path.join(homepath, r'voices/end_texts.txt'), 'r', encoding="utf-8") as f:
        reader = csv.reader(f)
        end_texts = [ end_text for end_text in f.read().splitlines() ]
        # print('end_texts:', end_texts)

    global end_sleep_texts
    with open(path.join(homepath, r'voices/sleep_texts.txt'), 'r', encoding="utf-8") as f:
        reader = csv.reader(f)
        end_sleep_texts = [ text for text in f.read().splitlines() ]


change_speaker_pattern = r'.+(?=番[にへ](音声変更|変更|変えて))'
change_speaker_repatter = re.compile(change_speaker_pattern)

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
            start(speakers[speaker])
            return True

    return False

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
    if text in end_texts:
        end(speakers[speaker])
        return True

    if text in end_sleep_texts:
        end_sleep(speakers[speaker])
        return True

    return False


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

    for voice in voices[speakers[speaker]].items():
        if re.search(voice[0], text):
            play_voice(path.join(speakers[speaker], voice[1]))
            break
    else:
        print('not find talk.')


init()

start(speakers[speaker])

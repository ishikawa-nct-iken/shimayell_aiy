#!/usr/bin/env python3

from os import path, listdir
import subprocess
import random
import platform

homepath = path.dirname(__file__)

def play_voice(voicepath, play_error = True, join_path_voices = True):
    """
    指定したパスのファイルもしくはパスのフォルダ中のファイルをランダムに再生する．

    Parameters
    ----------
    voicepath : str
        音楽ファイルもしくはフォルダのパス．
    play_error : bool
        エラー時，それに対応した音声を再生するかどうか．
    """

    if join_path_voices:
        voicepath = path.join(homepath, 'voices', voicepath)

    print('voicepath:', voicepath)

    if path.isfile(voicepath):
        play_file(voicepath)
    elif path.isdir(voicepath):
        filespath = [path.join(voicepath, f) for f in listdir(voicepath) if path.isfile(path.join(voicepath, f))]
        if len(filespath) == 0:
            print('not find any files in', voicepath, '.')
            if play_error:
                play_voice('file_error', False)
        else:
            play_voice(random.choice(filespath), True, False)
    else:
        print('not find', voicepath, '.')
        if play_error:
            play_voice('file_error', False)


def play_file(filepath):
    """
    指定した音楽ファイルを再生する．

    Parameters
    ----------
    filepath : str
        音楽ファイルのパス．
    """
    if platform.system() == 'Windows':
        return

    _, ext = path.splitext(filepath)
    if ext == '.wav':
        print('aplay', filepath)
        subprocess.run(['aplay', filepath])
    elif ext == '.mp3':
        print('mpg321', filepath)
        subprocess.run(['mpg321', filepath])
    elif ext == '.m4a':
        print('mplayer', filepath)
        subprocess.run(['mplayer', filepath])
    else:
        print('cannot play file', filepath)


def start(speakerpath):
    """
    開始時の音声を再生する．
    """
    print('in start():', path.join(speakerpath, '開始時'))
    play_voice(path.join(speakerpath, '開始時'), False)


def end(speakerpath):
    """
    終了時の音声を再生する．
    """
    play_voice(path.join(speakerpath, '終了時'), False)

def end_sleep(speakerpath):
    """
    終了（睡眠）時の音声を再生する．
    """
    play_voice(path.join(speakerpath, '挨拶_おやすみ'), False)

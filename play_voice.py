#!/usr/bin/env python3

from os import path, listdir
import subprocess
import random


def play_voice(voicepath, play_error = True):
    """
    指定したパスのファイルもしくはパスのフォルダ中のファイルをランダムに再生する．

    Parameters
    ----------
    voicepath : str
        音楽ファイルもしくはフォルダのパス．
    play_error : bool
        エラー時，それに対応した音声を再生するかどうか．
    """
    voicepath = path.join('voices', voicepath)
    print('voicepath:', voicepath)
    if path.isfile(voicepath):
        play_file(voicepath)
    elif path.isdir(voicepath):
        filespath = [path.join(voicepath, f) for f in listdir(voicepath) if os.path.isfile(os.path.join(voicepath, f))]
        if len(filespath) == 0:
            print('not find any files in', voicepath, '.')
            if play_error:
                play_voice('file_error', False)
        else:
            play_voice(filespath)
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
    pass
    _, ext = path.splitext(filepath)
    if ext == '.wav':
        print('aplay', filepath)
        subprocess.run(['aplay', filepath])
    elif ext == '.mp3':
        print('mpg321', filepath)
        subprocess.run(['mpg321', filepath])
    else:
        print('cannot play file', filepath)


def start():
    """
    スタート時の音声を再生する．
    """
    play_voice('start', False)

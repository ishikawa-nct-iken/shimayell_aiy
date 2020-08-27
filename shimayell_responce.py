#!/usr/bin/env python3

import csv
import subprocess

talks = {}
with open(r'talks/setting.csv') as f:
    reader = csv.reader(f)
    talks = { line[0] : line[1] for line in reader }


end_texts = ['goodbye', 'bye-bye', 'ばいばい', 'バイバイ']
def is_end_text(text):
    return text in end_texts


def responce(text):
    if text in talks:
        subprocess.run(['aplay', r'./audios/' + talks[text]])

    return 'ごめんさい．分かりませんでした．'

#!/usr/bin/env python3

import csv
import pprint

talks = {}
with open(r'talks/setting.csv') as f:
    reader = csv.reader(f)
    l = [row for row in reader]
    talks[l[0]] = l[1]


end_texts = ['goodbye', 'bye-bye', 'ばいばい', 'バイバイ']
def is_end_text(text):
    return text in end_texts


def responce(text):
    if text == 'こんにちは':
        return 'こんにちは！'

    return 'ごめんさい．分かりませんでした．'

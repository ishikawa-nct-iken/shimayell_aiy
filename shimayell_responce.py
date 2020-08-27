#!/usr/bin/env python3

end_texts = ['goodbye', 'bye-bye', 'ばいばい', 'バイバイ']
def is_end_text(text):
    return text in end_texts

def responce(text):
    if text == 'こんにちは':
        return 'こんにちは！'
    
    return 'ごめんさい．分かりませんでした．'

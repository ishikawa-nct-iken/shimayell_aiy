#!/usr/bin/env python3

import shimayell_responce as sr

def main():
    while True:
        text = input()
        print('You said "', text, '"')

        if text:
            if sr.is_end_text(text):
                print('Bye!')
                break

        sr.responce(text)


if __name__ == '__main__':
    main()

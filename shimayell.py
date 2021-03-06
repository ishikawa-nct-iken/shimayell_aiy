#!/usr/bin/env python3

import logging

import aiy.assistant.grpc
import aiy.audio
import aiy.voicehat

import shimayell_responce as sr

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
)


def main():
    status_ui = aiy.voicehat.get_status_ui()
    status_ui.status('starting')
    assistant = aiy.assistant.grpc.get_assistant()
    # button = aiy.voicehat.get_button()
    with aiy.audio.get_recorder():
        while True:
            # button.wait_for_press()
            status_ui.status('listening')
            print('Listening...')

            text, _ = assistant.recognize()

            print('You said "', text, '"')

            if text:
                text = text.replace(' ', '').replace('　', '')

                if sr.is_end_text(text):
                    status_ui.status('stopping')
                    print('Bye!')
                    break

                sr.responce(text)


if __name__ == '__main__':
    main()

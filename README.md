# shimayell_aiy

## 実行方法

> python3 shimayell.py

## 話者変更方法

1. "テスト君に変更"のように言う

## 話者追加方法

1. voices/speakers.csvを開き，"新しい話者の名前,フォルダ名"のように追加する

## 音声追加方法

1. voices/speakers.csvに書かれたファイルの中に音声ファイルを入れる

2. voices.csvを開き，"利用者の声,音声ファイル名"のように追加する

## TODO

- 開始時や終了時，認識できなかった時に，start.wavやend.wav, not_found.wavなどの特別なファイルを呼び出す
- setting.iniなどで話者の変更を保存する
- 音声をファイルでなくフォルダとして指定した際，フォルダ内のランダムなファイルを再生する
- 音声をzipなどで圧縮し，自動で解凍させる

# shimayell_aiy

## AIY Voice Kitでのダウンロード方法

> git clone https://github.com/ishikawa-nct-iken/shimayell_aiy.git

## アップデート

> git pull

## 実行方法

- 音声入力

> python3 shimayell.py

- テキスト入力

> python3 shimayell_text.py

## 話者変更方法

1. "1番に変更"のように言う

## 話者追加方法

1. voices/speakers.csvを開き，"新しい話者の名前,フォルダ名"のように追加する

## 音声追加方法

1. voices/speakers.csvに書かれたファイルの中に音声ファイルを入れる

2. voices.csvを開き，"利用者の声,音声ファイル名"のように追加する

## 今後

- setting.iniなどで話者の変更を保存する

- 音声を必要に応じてダウンロード・アップデートするようにする

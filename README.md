# CreateMV  (CMV)
オーディオスペクトラムを表示した簡易的なMVが作成できます

# 開発環境
- Windows10
- python3.9.6

# ダウンロード
２通りの方法があります

## 実行ファイルをダウンロードする方法
[こちら](https://github.com/midry3125/CreateMV/releases/latest)から、exeファイルをダウンロードして、そのファイルをダブルクリックすると起動します

起動の際にコマンドプロンプトも表示されます

コマンドプロンプトには音声結合の進捗等が表示されます

## ソースコードをダウンロードする方法
※python3.9以降のインストールが必要です

[こちら](https://github.com/midry3125/CreateMV/releases/latest)から、zip(またはgzip)形式のファイルをダウンロードして展開

その後該当ディレクトリにて下記コマンドを実行したのち、main.pyをダブルクリックすると起動します

```bash
$ pip install --user .
```

# ビルド
開発者向けに以下にビルド手順を示します

(使用環境を汚さない為にも、poetryのインストールを推奨します)

```bash
$ git clone https://github.com/midry3125/CreateMV
$ cd CreateMV
$ poetry install # or: pip install --user .
$ poetry run nuitka --mingw64 --follow-imports --enable-plugin=numpy --onefile -o CreateMV.exe ./createmv/main.py # pipを使用してインストールした場合、先頭のpoetry runは不要です
```

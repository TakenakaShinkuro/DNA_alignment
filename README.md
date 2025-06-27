# DNA_alignment
16ｓのデータを取得し、進化距離のマトリックスを得るためのpythonプログラム。A Python script to retrieve 16S rRNA sequences and calculate an evolutionary distance matrix.

# 16S rRNA 距離マトリックス作成ツール

このPythonプログラムは、16S rRNA配列のFASTAファイルを用いて、MUSCLEによるアライメントを行い、配列間の進化的距離（シーケンスアイデンティティベース）を計算します。出力は距離マトリックスのTSVファイルです。

## 🧠 主な機能

- 16S rRNAのFASTAファイルを読み込み
- MUSCLEを用いた多重配列アライメント
- アライメントに基づく距離マトリックス（シーケンスアイデンティティ）の作成
- 出力はTSV形式

## 🗂️ ファイル構成

├── align_distance.py # 本プログラム
├── LAB_178_16s.fasta # 入力用の16S配列FASTAファイル
├── LAB_178_dist_matrix.tsv # 出力される距離マトリックス
├── README.md # 本ファイル


## 🚀 実行方法

### 1. 必要なライブラリのインストール

- Python 3.8 以上
- 必要なPythonパッケージ

### 2. MUSCLEのインストール
MUSCLE公式ページからダウンロード

実行ファイル (muscle.exe または muscle) をPATHに追加するか、同じフォルダに配置してください

### 3. 実行コマンド
bash
コピーする
編集する
python distance_matrix.py
※ ファイルパスを変更する場合は、スクリプト内の以下の部分を修正してください。

python
コピーする
編集する
input_path = '入力FASTAファイルのパス'
out_path   = '出力ファイルのパス'
📤 出力ファイル
LAB_178_dist_matrix.tsv
→ 種間の距離マトリックスが出力されます。ファイルはタブ区切りのテキストです。


### 🙋‍♂️ 著者
Takenaka Shinkuro (2021)
本ツールは次の論文の解析の一部として開発されました。
Shinkuro Takenaka, Takeshi Kawashima, Masanori Arita, A sugar utilization phenotype contributes to the formation of genetic exchange communities in lactic acid bacteria, FEMS Microbiology Letters, Volume 368, Issue 17, September 2021, fnab117, https://doi.org/10.1093/femsle/fnab117

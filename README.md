# Google-Code-Golf-2025

## ファイル構成

```
google-code-golf-2025
├── XXX（001~400）
│   ├── testcases（テストケースのフォルダ）
│   ├── 0_input.json（入力JSON）
│   ├── 0_gen.py（テストケースの生成方法が書かれたPythonコード）
│   ├── 1_solution.md（問題の考察ポイントや解くための手続きを自然言語で記述）
│   ├── 2_plain_code.py（平易なPythonで記載されたコード）
│   └── 3_submission.py（コードゴルフ用のコード）
├── verify.py（テストケースを実行するためのバリデータ）
├── verify.all（全てのsubをテストした上でスコアを計算）
├── list.py（subが未実装のファイルの一覧を取得）
├── generate_testcases.py（テストケースのテキストファイルを生成するためのスクリプト）
├── generate_submission.py（提出用のフォルダを生成するためのスクリプト）
├── compress_solution.py（zlib圧縮によるコード最適化）
├── optimize_variables.py（ランダム探索による変数名最適化）
└── optimize_and_compress.py（変数名最適化 + 圧縮の統合ツール）
```

## テストケースの色付き表示方法

- generate_testcases.pyを実行すると、testcasesフォルダにテストケースのテキストファイルが生成される
- VSCodeの拡張機能「Color My Text」をインストール
- ワークスペースの設定に以下を追加
- テキストファイルをVSCode上で開くと色がついて表示される

```json
{
    "colorMyText.configurations": [
        { 
            "paths": ["**/testcases/*.txt"],
            "rules": [
                { "patterns": ["0"], "color": "White"},
                { "patterns": ["1"], "color": "BrightBlack"},
                { "patterns": ["2"], "color": "BrightBlue"},
                { "patterns": ["3"], "color": "BrightCyan"},
                { "patterns": ["4"], "color": "BrightGreen"},
                { "patterns": ["5"], "color": "BrightMagenta"},
                { "patterns": ["6"], "color": "BrightRed"},
                { "patterns": ["7"], "color": "Red"},
                { "patterns": ["8"], "color": "BrightYellow"},
                { "patterns": ["9"], "color": "Blue"}
            ]
        }
    ]
}
```

## Docker Composeを使った実行方法

### 環境構築

```bash
# Dockerコンテナをビルド
docker compose build
```

### ワンライナーで実行

```bash
# タスク1のsubmissionコードをテスト
docker compose run --rm code-golf python verify.py 1 sub

# タスク1のplainコードをテスト
docker compose run --rm code-golf python verify.py 1 plain

# 全タスクのテスト
docker compose run --rm code-golf python verify_all.py
```

## 進め方

- 問題を読んで1_solution.mdを頑張って書く
- 2_plain_code.pyをAIに書かせる
- 3_submission.pyをAIに書かせる



## タスクのビジュアライザ

```
cd task-visualizer
```

httpサーバーを起動

```
npm run dev
```

`http://localhost:8080/task-visualizer/` にアクセスすると各タスクの入力がビジュアライズされます

ARC-GEN exampleは展開するときに少し重い時があります。

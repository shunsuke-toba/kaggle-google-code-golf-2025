# Task Visualizer

Google Code Golf 2025のタスクデータを視覚的に表示するツールです。

## 使用方法

### 方法1: サーバーモード（推奨）

```bash
cd task-visualizer
npm run dev
```

ブラウザで http://localhost:8080/task-visualizer/ にアクセスし、ドロップダウンからタスクを選択します。

### 方法2: ファイル直接開く

`index.html`をブラウザで直接開き、「Choose File」ボタンからJSONファイルを選択します。

## 機能

- ARC-AGIタスクのグリッド表示
- Training/Test/ARC-GENの例を視覚化
- Input → Output の流れで確認
- カラーレジェンド表示

## 技術スタック

- React (CDN版)
- Tailwind CSS (CDN版)
- Babel (ブラウザ内トランスパイル)
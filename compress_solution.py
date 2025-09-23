#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Code Golf Solution Compressor

圧縮を使ってコードゴルフソリューションのサイズを最適化するツール
"""

import os
import sys
import zlib
import zopfli.zlib


def compress_solution(solution_code: str) -> tuple[bytes, bool, int, int]:
    """
    ソリューションコードを圧縮して最適なバージョンを返す

    Args:
        solution_code: 圧縮するPythonコード

    Returns:
        tuple: (最終バイト, 圧縮使用フラグ, 元サイズ, 最終サイズ)
    """
    solution_bytes = solution_code.strip().encode("utf-8")
    original_len = len(solution_bytes)

    compressed_data = zopfli.zlib.compress(solution_bytes).replace(b'\\',b'\\\\').replace(b'\0',b'\\0').replace(b'\r',b'\\r').replace(b'\n',b'\\n')

    # 圧縮データをPythonコードとして埋め込み
    quote_count = compressed_data.count(b'"') + compressed_data.count(b"'")

    if quote_count >= 6:
        compressed_data_str = b'"""' + compressed_data + b'"""'
    elif quote_count >= 2:
        if b'"' in compressed_data:
            first_quote_found = False
            new_data = b''
            for i in range(len(compressed_data)):
                if compressed_data[i:i+1] == b'"' and not first_quote_found:
                    first_quote_found = True
                    new_data += b'"'
                elif compressed_data[i:i+1] == b'"':
                    new_data += b'\\"'
                elif compressed_data[i:i+1] == b"'":
                    new_data += b"\\'"
                else:
                    new_data += compressed_data[i:i+1]
            compressed_data = new_data
            compressed_data_str = b"'" + compressed_data + b"'"
        else:
            first_quote_found = False
            new_data = b''
            for i in range(len(compressed_data)):
                if compressed_data[i:i+1] == b"'" and not first_quote_found:
                    first_quote_found = True
                    new_data += b"'"
                elif compressed_data[i:i+1] == b"'":
                    new_data += b"\\'"
                elif compressed_data[i:i+1] == b'"':
                    new_data += b'\\"'
                else:
                    new_data += compressed_data[i:i+1]
            compressed_data = new_data
            compressed_data_str = b'"' + compressed_data + b'"'
    elif b'"' in compressed_data:
        compressed_data_str = b"'" + compressed_data + b"'"
    else:
        compressed_data_str = b'"' + compressed_data + b'"'

    compressed_code = b"import zlib;exec(zlib.decompress(bytes(%s,'L1')))" % compressed_data_str

    # UTF-8でデコードできるかテスト
    try:
        compressed_code.decode("utf-8")
        final_code = compressed_code
    except UnicodeDecodeError:
        # エラーが出る場合はL1エンコーディング指定を追加
        final_code = b"#coding:L1\nimport zlib;exec(zlib.decompress(bytes(%s,'L1')))" % compressed_data_str

    compressed_len = len(final_code)

    # より短い方を選択
    if compressed_len < original_len:
        return final_code, True, original_len, compressed_len
    else:
        return solution_bytes, False, original_len, original_len


def save_compressed_solution(task_id: int, solution_code: str, output_dir: str = "submission"):
    """
    圧縮したソリューションをファイルに保存

    Args:
        task_id: タスク番号
        solution_code: ソリューションコード
        output_dir: 出力ディレクトリ
    """
    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, f"task{task_id:03d}.py")

    final_bytes, used_compression, original_len, final_len = compress_solution(solution_code)

    with open(file_path, "wb") as f:
        f.write(final_bytes)

    # 結果を表示
    if used_compression:
        print(f"✓ Task {task_id}: 圧縮成功! {original_len} → {final_len} bytes (-{original_len - final_len})")
    else:
        print(f"✓ Task {task_id}: 圧縮なし {original_len} bytes (圧縮効果なし)")

    return final_len


def compress_file(input_file: str, output_file: str = None):
    """
    ファイルからソリューションを読み込んで圧縮

    Args:
        input_file: 入力ファイルパス
        output_file: 出力ファイルパス (Noneの場合は入力ファイルを上書き)
    """
    with open(input_file, "r", encoding="utf-8") as f:
        solution_code = f.read()

    final_bytes, used_compression, original_len, final_len = compress_solution(solution_code)

    output_path = output_file or input_file
    with open(output_path, "wb") as f:
        f.write(final_bytes)

    print(f"圧縮結果: {input_file}")
    if used_compression:
        print(f"  圧縮成功! {original_len} → {final_len} bytes (-{original_len - final_len})")
    else:
        print(f"  圧縮なし {original_len} bytes (圧縮効果なし)")

    return final_len


def compress_task(task_num: int, output_dir: str = "submission"):
    """
    タスク番号から3_submission_uncompressed.pyを読み込んで3_submission.pyに圧縮出力

    Args:
        task_num: タスク番号 (例: 118)
        output_dir: 出力ディレクトリ (3_submission_uncompressed.pyがある場合は無視)
    """
    uncompressed_file = f"{task_num:03d}/3_submission_uncompressed.py"
    submission_file = f"{task_num:03d}/3_submission.py"

    if os.path.exists(uncompressed_file):
        print(f"圧縮元: {uncompressed_file} -> 出力先: {submission_file}")

        with open(uncompressed_file, "r", encoding="utf-8") as f:
            solution_code = f.read()

        final_bytes, used_compression, original_len, final_len = compress_solution(solution_code)

        # 同じフォルダの3_submission.pyに出力
        with open(submission_file, "wb") as f:
            f.write(final_bytes)

        if used_compression:
            print(f"✓ Task {task_num}: 圧縮成功! {original_len} → {final_len} bytes (-{original_len - final_len})")
        else:
            print(f"✓ Task {task_num}: 圧縮なし {original_len} bytes (圧縮効果なし)")

        return final_len

    else:
        print(f"エラー: ファイルが見つかりません: {uncompressed_file}")
        return None


def main():
    """コマンドライン実行時のメイン関数"""
    if len(sys.argv) < 2:
        print("使用法:")
        print("  python compress_solution.py <task_number>")
        print("  python compress_solution.py <input_file> [output_file]")
        print("例:")
        print("  python compress_solution.py 118")
        print("  python compress_solution.py 118/3_submission.py")
        sys.exit(1)

    arg = sys.argv[1]

    # 数字だけの場合はタスク番号として処理
    if arg.isdigit():
        task_num = int(arg)
        compress_task(task_num)
    else:
        # ファイルパスとして処理
        input_file = arg
        output_file = sys.argv[2] if len(sys.argv) > 2 else None

        if not os.path.exists(input_file):
            print(f"エラー: ファイルが見つかりません: {input_file}")
            sys.exit(1)

        try:
            compress_file(input_file, output_file)
        except Exception as e:
            print(f"エラー: {e}")
            sys.exit(1)


if __name__ == "__main__":
    main()

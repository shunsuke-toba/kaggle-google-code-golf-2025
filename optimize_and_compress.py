#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Optimize and Compress Workflow

変数名最適化 → 圧縮の一連のフローを実行するツール
"""

import os
import sys

# 既存のモジュールをインポート
from optimize_variables import optimize_variable_names
from compress_solution import compress_solution


def optimize_and_compress_task(
    task_num: int,
    iterations: int = 4000,
    test_subset_ids: list = None,
    skip_optimization: bool = False
):
    """
    タスクの完全な最適化フロー

    1. 3_submission_uncompressed.py を読み込み
    2. 変数名をランダム探索で最適化
    3. zlib圧縮を適用
    4. 3_submission.py に出力

    Args:
        task_num: タスク番号
        iterations: 変数名最適化の反復回数
        test_subset_ids: テストするサンプルIDのリスト
        skip_optimization: True の場合は変数名最適化をスキップ
    """
    uncompressed_file = f"{task_num:03d}/3_submission_uncompressed.py"
    submission_file = f"{task_num:03d}/3_submission.py"
    optimized_file = f"{task_num:03d}/3_submission_optimized.py"

    # ファイル存在チェック
    if not os.path.exists(uncompressed_file):
        print(f"エラー: ファイルが見つかりません: {uncompressed_file}")
        return None

    print("=" * 70)
    print(f"タスク {task_num} の最適化 + 圧縮フロー")
    print("=" * 70)

    # ステップ1: コード読み込みと元のコードの圧縮サイズを計算
    with open(uncompressed_file, "r", encoding="utf-8") as f:
        original_code = f.read().strip()

    original_len = len(original_code.encode("utf-8"))
    print(f"\n[1] 元のコード読み込み: {uncompressed_file}")
    print(f"    サイズ: {original_len} bytes")

    # 元のコードを圧縮してベースラインを計算
    original_compressed_bytes, original_used_compression, _, original_compressed_len = compress_solution(original_code)
    if original_used_compression:
        print(f"    元のコード圧縮後: {original_compressed_len} bytes（ベースライン）")
    else:
        print(f"    元のコードは圧縮効果なし: {original_compressed_len} bytes")

    # ステップ2: 変数名最適化
    if skip_optimization:
        print(f"\n[2] 変数名最適化: スキップ")
        optimized_code = original_code
    else:
        print(f"\n[2] 変数名最適化を実行 (反復: {iterations}回)")
        print("-" * 70)

        optimized_code, _, _ = optimize_variable_names(
            original_code,
            task_num,
            iterations=iterations,
            test_subset_ids=test_subset_ids
        )

        # 最適化版を保存
        with open(optimized_file, "w", encoding="utf-8") as f:
            f.write(optimized_code)

        optimized_len = len(optimized_code.encode("utf-8"))
        saved = original_len - optimized_len
        print(f"\n    最適化後サイズ: {optimized_len} bytes ({saved:+d} bytes)")
        print(f"    保存先: {optimized_file}")

    # ステップ3: zlib圧縮
    print(f"\n[3] zlib圧縮を適用")
    print("-" * 70)

    final_bytes, used_compression, pre_compress_len, final_len = compress_solution(optimized_code)

    # 結果サマリー
    print("\n" + "=" * 70)
    print("最適化完了サマリー")
    print("=" * 70)
    print(f"元のコード:            {original_len} bytes")
    print(f"元のコード圧縮後:      {original_compressed_len} bytes（ベースライン）")

    if not skip_optimization:
        optimized_len = len(optimized_code.encode("utf-8"))
        print(f"変数名最適化後:        {optimized_len} bytes ({original_len - optimized_len:+d})")

    if used_compression:
        print(f"最適化後圧縮:          {final_len} bytes ({pre_compress_len - final_len:+d})")
        compression_improvement = original_compressed_len - final_len
        print(f"\n圧縮での改善:          {compression_improvement:+d} bytes ({original_compressed_len} → {final_len})")
        print(f"合計削減:              {original_len - final_len} bytes ({original_len} → {final_len})")
    else:
        print(f"圧縮:                  効果なし")
        print(f"最終サイズ:            {final_len} bytes")
        compression_improvement = 0

    # 改善があった場合のみファイルを更新
    if compression_improvement > 0:
        print(f"\n✓ 圧縮で改善あり！ 両ファイルを更新します")

        # 3_submission_uncompressed.py を更新
        with open(uncompressed_file, "w", encoding="utf-8") as f:
            f.write(optimized_code)
        print(f"  更新: {uncompressed_file}")

        # 3_submission.py を更新
        with open(submission_file, "wb") as f:
            f.write(final_bytes)
        print(f"  更新: {submission_file}")
    elif compression_improvement == 0:
        print(f"\n→ 圧縮での改善なし。ファイルは更新しません")
    else:
        print(f"\n✗ 圧縮で悪化しました。ファイルは更新しません")
        print(f"  元のサイズを維持: {original_compressed_len} bytes")

    print("=" * 70)

    return final_len


def batch_optimize(task_numbers: list, iterations: int = 4000):
    """
    複数のタスクを一括最適化

    Args:
        task_numbers: タスク番号のリスト
        iterations: 各タスクの反復回数
    """
    results = {}

    print("\n" + "=" * 70)
    print(f"バッチ最適化: {len(task_numbers)} 個のタスク")
    print("=" * 70 + "\n")

    for task_num in task_numbers:
        try:
            final_size = optimize_and_compress_task(task_num, iterations=iterations)
            results[task_num] = final_size
            print()
        except Exception as e:
            print(f"\nエラー (タスク {task_num}): {e}\n")
            results[task_num] = None

    # 最終レポート
    print("\n" + "=" * 70)
    print("バッチ最適化レポート")
    print("=" * 70)

    for task_num in task_numbers:
        size = results.get(task_num)
        if size is not None:
            print(f"  タスク {task_num:03d}: {size} bytes ✓")
        else:
            print(f"  タスク {task_num:03d}: 失敗 ✗")

    print("=" * 70)


def main():
    """コマンドライン実行時のメイン関数"""
    if len(sys.argv) < 2:
        print("使用法:")
        print("  python optimize_and_compress.py <task_number> [iterations] [--skip-opt]")
        print("  python optimize_and_compress.py --batch <task1> <task2> ... [iterations]")
        print("\n例:")
        print("  python optimize_and_compress.py 173")
        print("  python optimize_and_compress.py 173 2000")
        print("  python optimize_and_compress.py 173 --skip-opt  # 変数名最適化をスキップ")
        print("  python optimize_and_compress.py --batch 173 209 118")
        print("\nオプション:")
        print("  task_number: タスク番号")
        print("  iterations: 最適化の反復回数（デフォルト: 4000）")
        print("  --skip-opt: 変数名最適化をスキップして圧縮のみ実行")
        print("  --batch: 複数のタスクを一括処理")
        sys.exit(1)

    # バッチモード
    if sys.argv[1] == "--batch":
        if len(sys.argv) < 3:
            print("エラー: タスク番号を指定してください")
            sys.exit(1)

        task_numbers = []
        iterations = 4000

        for arg in sys.argv[2:]:
            if arg.isdigit():
                num = int(arg)
                if num < 1000:  # タスク番号
                    task_numbers.append(num)
                else:  # 反復回数
                    iterations = num

        batch_optimize(task_numbers, iterations=iterations)
        return

    # 単一タスクモード
    task_num = int(sys.argv[1])
    iterations = 4000
    skip_opt = False

    for arg in sys.argv[2:]:
        if arg == "--skip-opt":
            skip_opt = True
        elif arg.isdigit():
            iterations = int(arg)

    optimize_and_compress_task(
        task_num,
        iterations=iterations,
        skip_optimization=skip_opt
    )


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Variable Name Optimizer for Code Golf

ランダム探索アルゴリズムを使用して変数名を最適化し、
圧縮後のバイト数を最小化するツール
"""

import ast
import copy
import json
import keyword
import os
import random
import re
import sys
import warnings
import zopfli.zlib

# テストケースを読み込む関数
def load_examples(task_num: int) -> dict:
    """
    タスクのテストケースを読み込む

    Args:
        task_num: タスク番号

    Returns:
        dict: {"train": [...], "test": [...], "arc-gen": [...]}
    """
    examples_path = f"{task_num:03d}/0_input.json"
    if not os.path.exists(examples_path):
        print(f"警告: {examples_path} が見つかりません")
        return {}

    with open(examples_path, "r") as f:
        return json.load(f)


# --- コアユーティリティ ---

def create_template_from_function(code_string: str) -> tuple[str, list]:
    """
    コードから変数名を抽出してテンプレート化

    Args:
        code_string: 元のPythonコード

    Returns:
        tuple: (テンプレート文字列, 変数名リスト)
    """
    tree = ast.parse(code_string)

    # 除外する名前（組み込み関数、キーワード、よく使うライブラリ関数）
    excluded_names = {
        'Counter', 'next', 'int', 'chain', 'enumerate', 'combinations',
        'product', 'str', 'abs', 'exec', 'len', 'min', 'max', 'range',
        'set', 'any', 'filter', 'list', 'map', 'sum', 'tuple', 'zip',
        'all', 'sorted', 'bool', 'dict', 'float', 'ord', 'chr', 'reversed',
        'pow', 'round', 'divmod', 'finditer', 'search', 'match', 'sub',
        'permutations', 'groupby', 'accumulate', 'repeat', 'cycle'
    }

    # ASTから変数名を抽出
    variable_names = {
        node.id for node in ast.walk(tree)
        if isinstance(node, ast.Name)
        and node.id not in keyword.kwlist
        and node.id not in excluded_names
    }

    template = code_string
    # 長い変数名から順に置換（部分マッチを避けるため）
    for name in sorted(list(variable_names), key=len, reverse=True):
        template = re.sub(r'\b' + re.escape(name) + r'\b', f'##{name}##', template)

    # 特殊なケースを処理（関数名pとf文字列）
    template = (template
                .replace("def ##p##", "def p")
                .replace("##p##=lambda", "p=lambda")
                .replace("##p## =lambda", "p=lambda")
                .replace("##f##'", "f'")
                .replace('##f##"', 'f"'))

    return template, sorted(list(variable_names))


def get_compressed_size(code: str) -> tuple[int, int] | None:
    """
    コードを圧縮してサイズを計算（検証なし）

    Args:
        code: 評価するコード

    Returns:
        tuple: (圧縮後のバイト数, ペナルティ値) または None（エラー時）
    """
    try:
        # 圧縮
        compressed = zopfli.zlib.compress(code.encode())

        # ペナルティ計算（圧縮に不利な文字）
        penalty = (
            compressed.count(b'\\') +
            compressed.count(b'\0') +
            compressed.count(b'\n') +
            compressed.count(b'\r') +
            min(compressed.count(b"'"), compressed.count(b'"'))
        )

        return len(compressed), penalty
    except Exception:
        return None


def validate_with_examples(code: str, examples_to_check: list) -> bool:
    """
    テストケースでコードを検証（高速版）

    Args:
        code: 検証するコード
        examples_to_check: テストする例のリスト [(id, example), ...]

    Returns:
        bool: 全て成功したらTrue
    """
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=SyntaxWarning)

            # コードを実行してp関数を取得
            solution_namespace = {}
            exec(code, solution_namespace)
            p_func = solution_namespace.get('p')

            # テストケースで検証
            for _, example in examples_to_check:
                result = p_func(copy.deepcopy(example['input']))
                if json.dumps(result) != json.dumps(example['output']):
                    return False

            return True
    except Exception:
        return False


def validate_code(code: str, all_examples: list) -> tuple | None:
    """
    全テストケースに対してコードを検証

    Args:
        code: 検証するコード
        all_examples: 全テストケース [(id, example), ...]

    Returns:
        失敗した場合は (id, example)、成功した場合は None
    """
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=SyntaxWarning)

            solution_namespace = {}
            exec(code, solution_namespace)
            p_func = solution_namespace.get('p')

            for i, example in all_examples:
                result = p_func(copy.deepcopy(example['input']))
                if json.dumps(result) != json.dumps(example['output']):
                    return i, example  # 失敗

            return None  # 成功
    except Exception:
        return all_examples[0] if all_examples else None


# --- 最適化メイン処理 ---

def optimize_variable_names(
    code: str,
    task_num: int,
    iterations: int = 4000,
    rebase_interval: int = 500,
    test_subset_ids: list = None
) -> tuple[str, int, int]:
    """
    ランダム探索で変数名を最適化

    Args:
        code: 最適化する元コード
        task_num: タスク番号
        iterations: 最大試行回数
        rebase_interval: リベース間隔
        test_subset_ids: テストするサンプルIDのリスト（Noneの場合は全て）

    Returns:
        tuple: (最適化されたコード, 圧縮後のバイト数, ペナルティ)
    """
    # テストケースを読み込み
    task_data = load_examples(task_num)
    all_examples = list(enumerate(
        task_data.get('train', []) +
        task_data.get('test', []) +
        task_data.get('arc-gen', [])
    ))

    if not all_examples:
        print(f"警告: タスク{task_num}のテストケースが見つかりません")
        return code, 0, 0

    # テスト用のサブセットを選択
    if test_subset_ids:
        checked_examples = [ex for ex in all_examples if ex[0] in test_subset_ids]
        checked_example_ids = set(test_subset_ids)
    else:
        checked_examples = all_examples
        checked_example_ids = {ex[0] for ex in all_examples}

    print(f"タスク {task_num} の最適化を開始")
    print(f"テストケース: {len(checked_examples)}/{len(all_examples)} 個")

    # テンプレート作成
    FUNCTION_TEMPLATE, original_vars = create_template_from_function(code)
    print(f"検出された変数: {original_vars}\n")

    if not original_vars:
        print("最適化可能な変数が見つかりませんでした")
        return code, 0, 0

    # 候補となる変数名（短い文字を優先）
    candidate_names = list("qwertyuiopasdfghjklzxcvbnm")

    # 初期コード
    initial_code = FUNCTION_TEMPLATE.replace("##", "")
    PAYLOAD_OVERHEAD = 60  # 圧縮ラッパーのオーバーヘッド

    # # 初期検証
    # print("初期コードの検証中...")
    # if validate_code(initial_code, all_examples) is not None:
    #     print("エラー: 初期コードがテストケースを通過しません")
    #     return code, 0, 0
    # print("初期コード: 検証成功\n")

    # 初期サイズを計算
    size_result = get_compressed_size(initial_code)
    if size_result is None:
        print("エラー: 初期コードの圧縮に失敗しました")
        return code, 0, 0

    current_base, current_penalty = size_result
    current_total_size = PAYLOAD_OVERHEAD + current_base + current_penalty

    # グローバルベスト
    global_best_code = initial_code
    global_best_base, global_best_penalty = current_base, current_penalty
    global_best_total_size = current_total_size

    # 最後の正常バージョン
    last_known_good_code = initial_code
    last_known_good_base, last_known_good_penalty = current_base, current_penalty
    last_known_good_total_size = current_total_size

    print(f"初期サイズ: {global_best_total_size} bytes (Base: {current_base}, Penalty: {current_penalty})")
    print(f"コード: {initial_code}\n")
    print("-" * 60)

    # 最適化ループ
    next_rebase = rebase_interval
    current_rebase_interval = rebase_interval

    # 進捗追跡
    attempts = 0  # 試行回数
    improvements = 0  # 改善回数
    skipped_by_size = 0  # サイズで弾かれた回数
    skipped_by_validation = 0  # 検証で弾かれた回数
    last_progress_report = 0  # 最後の進捗表示

    for i in range(iterations):
        # リベースタイミング
        if i > 0 and i >= next_rebase:
            current_rebase_interval = int(current_rebase_interval * 1.3)
            next_rebase += current_rebase_interval

            print(f"\n--- リベース #{i}: 全テストケースで検証中 (Size: {global_best_total_size}) ---")

            failing_example = validate_code(global_best_code, all_examples)

            if failing_example:
                fail_id, _ = failing_example
                print(f"  検証失敗! (例 #{fail_id}) → 前回の正常版に戻します")

                # 巻き戻し
                global_best_code = last_known_good_code
                global_best_base, global_best_penalty = last_known_good_base, last_known_good_penalty
                global_best_total_size = last_known_good_total_size
                print(f"  復元: {global_best_total_size} bytes")

                # 失敗した例をテストセットに追加
                if fail_id not in checked_example_ids:
                    checked_example_ids.add(fail_id)
                    checked_examples = [ex for ex in all_examples if ex[0] in checked_example_ids]
                    print(f"  例 #{fail_id} をテストセットに追加 (計 {len(checked_examples)} 個)")
            else:
                # 正常版を更新
                last_known_good_code = global_best_code
                last_known_good_base, last_known_good_penalty = global_best_base, global_best_penalty
                last_known_good_total_size = global_best_total_size
                print(f"  検証成功! チェックポイント更新")

            # テンプレートを再作成
            FUNCTION_TEMPLATE, original_vars = create_template_from_function(global_best_code)
            size_result = get_compressed_size(global_best_code)
            if size_result:
                current_base, current_penalty = size_result
            print(f"  新しい変数: {original_vars}")

            # 進捗統計をリセット
            print(f"  進捗: 試行 {attempts}, 改善 {improvements}, サイズNG {skipped_by_size}, 検証NG {skipped_by_validation}")
            attempts = 0
            improvements = 0
            skipped_by_size = 0
            skipped_by_validation = 0
            last_progress_report = i
            print("-" * 60)

        if not original_vars:
            continue

        attempts += 1

        # 定期的な進捗表示（1回ごと）
        if attempts > 0 and i - last_progress_report >= 1:
            print(f"進捗 [{i+1}/{iterations}]: 試行 {attempts}, 改善 {improvements}, サイズNG {skipped_by_size}, 検証NG {skipped_by_validation}")
            last_progress_report = i

        # ランダムに変数名を変更
        trial_mapping = {var: var for var in original_vars}
        num_changes = random.randint(1, min(6, len(original_vars)))
        vars_to_change = random.sample(original_vars, k=num_changes)
        new_names = random.sample(candidate_names, k=num_changes)

        for var, new_name in zip(vars_to_change, new_names):
            trial_mapping[var] = new_name

        # テンプレートを適用
        trial_code = FUNCTION_TEMPLATE
        for var in original_vars:
            trial_code = trial_code.replace(f"##{var}##", trial_mapping[var])

        # ステップ1: まず圧縮してサイズをチェック（高速）
        size_result = get_compressed_size(trial_code)
        if size_result is None:
            continue  # 圧縮失敗なのでスキップ

        trial_base, trial_penalty = size_result
        trial_total_size = PAYLOAD_OVERHEAD + trial_base + trial_penalty

        # サイズが改善しない場合はスキップ（検証不要）
        if trial_total_size > global_best_total_size:
            skipped_by_size += 1
            continue

        # ステップ2: サイズが良い場合のみ検証（時間かかる）
        if not validate_with_examples(trial_code, checked_examples):
            skipped_by_validation += 1
            continue  # 検証失敗なのでスキップ

        # 両方パスしたので採用
        global_best_code = trial_code
        global_best_base, global_best_penalty = trial_base, trial_penalty

        if trial_total_size < global_best_total_size:
            improvement = global_best_total_size - trial_total_size
            improvements += 1
            print(f"\n改善! {trial_total_size} bytes (Base:{trial_base}, Penalty:{trial_penalty}) @{i+1} [-{improvement}]")
            print(f"  {trial_code}")
            print(f"  統計: 試行 {attempts}, 改善 {improvements}, サイズNG {skipped_by_size}, 検証NG {skipped_by_validation}")

        global_best_total_size = trial_total_size

    # 最終検証
    print(f"\n" + "=" * 60)
    print("最終検証中...")
    if validate_code(global_best_code, all_examples) is not None:
        print("警告: 最終コードがテストケースを通過しませんでした")
    else:
        print("最終コード: 検証成功")

    print(f"\n最終統計:")
    print(f"  合計試行回数: {attempts}")
    print(f"  改善回数: {improvements}")
    print(f"  サイズでスキップ: {skipped_by_size}")
    print(f"  検証でスキップ: {skipped_by_validation}")
    print(f"  検証実行率: {(skipped_by_validation + improvements) / max(attempts, 1) * 100:.1f}% ({skipped_by_validation + improvements}/{attempts})")

    print(f"\n最終スコア: {global_best_total_size} bytes (Base: {global_best_base}, Penalty: {global_best_penalty})")
    print(f"最適化されたコード:\n{global_best_code}")
    print("=" * 60)

    return global_best_code, global_best_base, global_best_penalty


def optimize_task(
    task_num: int,
    source_file: str = None,
    output_file: str = None,
    iterations: int = 4000,
    test_subset_ids: list = None
):
    """
    タスクの3_submission_uncompressed.pyを最適化

    Args:
        task_num: タスク番号
        source_file: 入力ファイル（指定しない場合は3_submission_uncompressed.py）
        output_file: 出力ファイル（指定しない場合は3_submission_optimized.py）
        iterations: 最適化の反復回数
        test_subset_ids: テストするサンプルIDのリスト
    """
    # デフォルトのファイルパス
    if source_file is None:
        source_file = f"{task_num:03d}/3_submission_uncompressed.py"
    if output_file is None:
        output_file = f"{task_num:03d}/3_submission_optimized.py"

    # ファイル存在チェック
    if not os.path.exists(source_file):
        print(f"エラー: ファイルが見つかりません: {source_file}")
        return

    # コードを読み込み
    with open(source_file, "r", encoding="utf-8") as f:
        code = f.read().strip()

    print(f"入力: {source_file}")
    print(f"出力: {output_file}\n")

    # 最適化実行
    optimized_code, base_size, penalty = optimize_variable_names(
        code,
        task_num,
        iterations=iterations,
        test_subset_ids=test_subset_ids
    )

    # 結果を保存
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(optimized_code)

    print(f"\n✓ 最適化完了: {output_file}")


def main():
    """コマンドライン実行時のメイン関数"""
    if len(sys.argv) < 2:
        print("使用法:")
        print("  python optimize_variables.py <task_number> [iterations] [test_ids...]")
        print("\n例:")
        print("  python optimize_variables.py 173")
        print("  python optimize_variables.py 173 2000")
        print("  python optimize_variables.py 173 4000 0 5 10")
        print("\nオプション:")
        print("  task_number: タスク番号")
        print("  iterations: 最適化の反復回数（デフォルト: 4000）")
        print("  test_ids: テストするサンプルID（指定しない場合は全て）")
        sys.exit(1)

    task_num = int(sys.argv[1])
    iterations = int(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2].isdigit() else 4000

    # テストIDを解析
    test_ids = None
    if len(sys.argv) > 2:
        test_ids = []
        for arg in sys.argv[2:]:
            if arg.isdigit():
                test_ids.append(int(arg))
        if not test_ids:
            test_ids = None

    optimize_task(task_num, iterations=iterations, test_subset_ids=test_ids)


if __name__ == "__main__":
    main()

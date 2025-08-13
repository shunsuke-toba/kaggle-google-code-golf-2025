# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## あなたの目的

- 0_input.jsonを読む。（pattern: ""train"", path: "005/0_input.json", output_mode: "content", head_limit: 5）のようにする。
- testcasesや1_solution.mdを参考にして、2_plain_code.pyを実装する。
    - 日本語のコメントを含むファイルを作成する際は、エンコーディングがUTF-8であることを確認する。(重要)
    - importは使ってはいけない。
- 「python verify.py (問題番号) plain」を実行して、テストケースに対して正しく動作するか確認する。
- その後、2_plain_code.pyを参考にして、3_submission.pyを実装する。
- 3_submission.pyは、2_plain_code.pyの内容をコードゴルフのために最適化したものとする。
- 「python verify.py (問題番号) sub」を実行して、テストケースに対して正しく動作するか確認する。

## Repository Overview

This repository contains solutions for the 2025 Google Code Golf Championship. It implements ARC-AGI (Abstraction and Reasoning Challenge) style puzzles where the goal is to solve grid pattern recognition problems with the shortest possible Python code.

## Common Development Commands

### Testing Solutions
```bash
# Test a submission solution (golf code)
python verify.py 1 sub

# Test a plain code solution (readable version)  
python verify.py 1 plain
```

### Generate Submission Package
```bash
# Creates submission.zip containing all task001.py to task400.py files
python generate_submission.py
```

### Using Code Golf Utilities
```python
# For Kaggle environment development
from code_golf_utils import load_examples, verify_program
examples = load_examples(1)  # Load problem 1
verify_program(1, examples)  # Test solution in /kaggle/working/task.py
```

## Architecture and Development Workflow

### Problem Structure
Each problem (001-400) follows this development pipeline:
1. **Analysis**: Read `0_input.json` for problem specification
2. **Planning**: Document approach in `1_solution.md` (in Japanese)  
3. **Implementation**: Write readable solution in `2_plain_code.py`
4. **Optimization**: Create golf version in `3_submission.py`
5. **Validation**: Test using `verify.py` against test cases

### Solution Requirements
- Function must be named `p()` and accept input grid
- No imports allowed in solution files (libraries auto-injected during testing)
- Available libraries: `collections`, `itertools`, `math`, `operator`, `re`, `string`, `struct`
- Must pass both ARC-AGI (train/test) and ARC-GEN examples
- Byte count optimization is crucial for competition ranking

### Code Golf Example
The repository now contains actual solutions. Example from `001/3_submission.py`:
```python
p=lambda j,A=range(9):[[j[r//3][c//3]and j[r%3][c%3]for c in A]for r in A]
```
This demonstrates the extreme compression techniques used in code golf.

### Test Case Format
Test cases in `testcases/*.txt` use this structure:
```
3 3          # Input dimensions (height width)
077          # Input grid data  
777
077
9 9          # Output dimensions
000077077    # Output grid data
000777777    # (continues for all rows)
...
```

### Verification System
The `verify.py` script:
- Loads problem data from `0_input.json`
- Injects allowed libraries automatically
- Tests against both solution types (plain/submission)
- Reports pass/fail counts and byte length
- Shows submission readiness status

### Submission Pipeline
1. Develop and test individual solutions
2. Run `python generate_submission.py` to create `submission.zip`
3. Submit zip file containing `task001.py` through `task400.py` to Kaggle

## Visual Development Setup

For debugging test cases visually, configure VS Code with "Color My Text" extension:

```json
{
    "colorMyText.configurations": [
        { 
            "paths": ["**/testcases/*.txt"],
            "rules": [
                { "patterns": ["0"], "color": "Blue"},
                { "patterns": ["1"], "color": "BrightBlack"},
                { "patterns": ["2"], "color": "BrightBlue"},
                { "patterns": ["3"], "color": "BrightCyan"},
                { "patterns": ["4"], "color": "BrightGreen"},
                { "patterns": ["5"], "color": "BrightMagenta"},
                { "patterns": ["6"], "color": "BrightRed"},
                { "patterns": ["7"], "color": "BrightWhite"},
                { "patterns": ["8"], "color": "BrightYellow"},
                { "patterns": ["9"], "color": "BrightMagenta"}
            ]
        }
    ]
}
```

## Key Implementation Patterns

### Grid Pattern Recognition
Problems typically involve:
- Identifying rectangular regions or shapes within grids
- Applying transformations (rotation, scaling, projection)
- Pattern completion or extension
- Logical operations between grid regions

### Code Golf Techniques  
Based on existing solutions:
- Lambda functions with minimal variable names
- List comprehensions over nested loops
- Boolean arithmetic for conditional logic
- Range object reuse (`A=range(9)`)
- Operator precedence exploitation for parentheses reduction
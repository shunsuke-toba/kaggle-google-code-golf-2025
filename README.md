# Google Code Golf 2025 - Solution Repository

Below you can find a outline of how to reproduce my solution for the Google Code Golf 2025 competition.
If you run into any trouble with the setup/code or have any questions please contact me at toba0248624@gmail.com.

## ARCHIVE CONTENTS

```
google-code-golf-2025/
├── XXX/ (001-400)              : Individual problem directories
│   ├── testcases/              : Test case files for visualization
│   ├── 0_input.json            : Problem specification and examples
│   ├── 0_gen.py                : Test case generation code
│   ├── 1_solution.md           : Solution approach and analysis (Japanese)
│   ├── 2_plain_code.py         : Readable Python implementation
│   └── 3_submission.py         : Code golf optimized version
├── verify.py                   : Test case validator for individual problems
├── verify_all.py               : Batch tester and score calculator
├── list.py                     : List unimplemented solutions
├── generate_testcases.py       : Generate test case text files
├── generate_submission.py      : Create submission.zip package
├── compress_solution.py        : Code optimization using zlib compression
├── optimize_variables.py       : Variable name optimization via random search
├── optimize_and_compress.py    : Integrated optimization tool
└── task-visualizer/            : Web-based task visualization tool
```

## HARDWARE

This solution can run on standard hardware:

- Ubuntu 20.04 LTS or later (or WSL2 on Windows)

## SOFTWARE

Python packages are detailed in `requirements.txt`:

- Python 3.11

## DATA SETUP

The repository already contains all problem data in JSON format. No additional downloads are required.

## ENVIRONMENT SETUP

### Option 1: Docker

```bash
# Build the Docker container
docker compose build

# Test a single problem
docker compose run --rm code-golf python verify.py 1 sub

# Test all problems
docker compose run --rm code-golf python verify_all.py
```

### Option 2: Local Python Environment

```bash
# Install dependencies
pip install -r requirements.txt

# Test a single problem
python verify.py 1 sub

# Test all problems
python verify_all.py
```

## SOLUTION BUILD

```bash
# Generate submission.zip containing task001.py to task400.py
python generate_submission.py
```

## Compression-based Optimization

```bash
# Variable name optimization via random search
python optimize_variables.py <problem_number>

# Compression-based optimization
python compress_solution.py <problem_number>

# Combined optimization
python optimize_and_compress.py <problem_number>
```

## Web-based Visualizer

```bash
cd task-visualizer
npm install
npm run dev
```

Access `http://localhost:8080/task-visualizer/` to view interactive task visualizations.

Note: ARC-GEN examples may take a moment to expand/load.

## Utility Scripts

```bash
# List problems without submission implementations
python list.py

# Test all submissions and calculate total score
python verify_all.py

# Generate test case text files for visualization
python generate_testcases.py
```

## NeurIPS Presentation

The file `logiclynx_presentation.mp4` contains the presentation video as specified in the "NeurIPS Presentation" section of the email.

## LICENSE

This project is licensed under the Apache License 2.0 - see the LICENSE file for details.

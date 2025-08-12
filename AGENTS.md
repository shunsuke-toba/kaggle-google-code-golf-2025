# Repository Guidelines

## Project Structure & Module Organization
- Root: utility scripts and docs — `verify.py` (local validator), `generate_submission.py` (builds zip), `list_unsolved.py` (quick status), `README.md`, `CLAUDE.md`.
- Tasks: numbered folders `001`–`400`, each containing:
  - `0_input.json`: ARC-AGI/ARC-GEN examples.
  - `1_solution.md`: reasoning and approach notes.
  - `2_plain_code.py`: clear, readable reference solution.
  - `3_submission.py`: code-golfed solution used for submission.
  - `testcases/`: supplemental text fixtures (optional).

## Build, Test, and Development Commands
- Test a task (submission): `python verify.py 7 sub`
  - Loads `007/0_input.json`, evaluates `007/3_submission.py`’s `p()`.
- Test a task (plain): `python verify.py 7 plain`
  - Evaluates `007/2_plain_code.py`’s `p()`.
- Package all tasks: `python generate_submission.py`
  - Produces `submission.zip` with `taskNNN.py` files.
- List incomplete submissions: `python list_unsolved.py`

## Coding Style & Naming Conventions
- Language: Python 3.
- Plain code (`2_plain_code.py`): prioritize clarity; PEP 8 (4-space indents, descriptive names). Optional: format locally before committing.
- Golfed code (`3_submission.py`): minimize bytes; must define `p(input)` and use no imports (validator rejects any `import`). Side effects, I/O, and globals should be avoided.
- File names and layout must match the task pattern above; do not rename.

## Testing Guidelines
- Framework: custom validator `verify.py`; no external test runner.
- Scope: ensure `p()` returns exact output for all train/test and ARC-GEN in `0_input.json`.
- Regressions: keep `2_plain_code.py` functionally equivalent to `3_submission.py`.
- Determinism: no randomness or time-based behavior.

## Commit & Pull Request Guidelines
- Commits: imperative, scoped by task — e.g., `007: optimize transpose; -42 bytes`.
- Include: summary of change, before/after byte count for `3_submission.py`, and verification results.
- PRs: link related issues (if any), describe approach, attach sample `verify.py` output.

## Security & Configuration Tips
- No network, file I/O, or imports in `3_submission.py`.
- Keep solutions pure and self-contained; avoid large constants unless necessary.

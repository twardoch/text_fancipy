# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

### Added
- Jekyll documentation site (`docs/`) with style gallery, CLI reference, and
  Python API pages
- Comprehensive test suite: 11 tests covering exact round-trips, per-style
  `unfancipy`, mixed-style stripping, edge cases, and fancy-name assertions
- `this_file` records in all source and test files per project convention
- `__all__` export list in `__init__.py`; re-exports `fancipy`, `unfancipy`,
  `unfancipy_all` for convenient top-level import

### Changed
- **Build system migrated** from pyscaffold/setuptools-scm to
  **hatchling + hatch-vcs** — `pyproject.toml` is now the single source of
  truth; `setup.cfg` and `setup.py` are superseded
- **CI workflow** updated to GitHub Actions v4/v5 actions, matrix extended to
  Python 3.9–3.12 across Linux/macOS/Windows, `ruff` + `mypy` lint job added,
  publish job uses OIDC trusted publishing
- `fancipy.py` docstrings expanded with Unicode block references, NFD/NFC
  explanation, and per-function parameter tables
- `get_table` falls back to `dflt` identity table for unknown style codes
  instead of returning `None`
- `__init__.py` simplified — drops Python 3.7 `importlib_metadata` shim
  (min Python is 3.9)

## [2.7.6] - 2026-05-17

### Added
- Unicode decomposition and normalization support (NFD before translate, NFC after)
- `unicodedata2` fast-path with stdlib `unicodedata` fallback

## [2.7.5] - 2025

### Added
- Initial comprehensive style set: mono, bold, bdit, sans, snbd, snit, snbi,
  scrb, frak, parn, circ, wide
- CLI via `fire` with per-style subcommands, `undo`, and `show`
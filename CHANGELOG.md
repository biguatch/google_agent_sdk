# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2025-10-30

### Added
- Initial project setup with uv package manager
- Service-based architecture foundation
- Entry point script (`run.py`) for application execution
- Basic project structure and documentation

### Changed
- Package renamed from `google_asdk` to `google_adk`
- Updated all documentation to reflect new package name
- Simplified entry point by removing redundant path manipulation

### Documentation
- Created README.md with project overview and features
- Created QUICKSTART.md for getting started guide
- Created index.md for project structure reference
- Updated all docstrings to reflect `google_adk` naming

## [Unreleased]

### Planned
- Core service implementations
- API integrations with Google services
- Comprehensive test suite
- Additional documentation and examples

---

## Commit History

### [900acd3] - 2025-10-30
**docs: update documentation to reflect package rename**
- Update README.md title and description from ASDK to ADK
- Update package docstring and author in __init__.py
- Update entry point script documentation in run.py

### [d29903b] - 2025-10-30
**refactor: rename package from google_asdk to google_adk**
- Renamed main package directory from google_asdk/ to google_adk/
- Updated project name in pyproject.toml
- Updated all import statements and module references
- Updated documentation (README.md, QUICKSTART.md, index.md)
- Updated run.py entry point script

### [57ce696] - 2025-10-30
**refactor(run): simplify entry point by removing path manipulation**

### [7d58678] - 2025-10-30
**chore: initial project setup with uv and service-based architecture**

### [3d2c219] - 2025-10-30
**first commit**

---

[0.1.0]: https://github.com/yourusername/google_adk/releases/tag/v0.1.0

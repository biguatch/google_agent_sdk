# Google Agents Project Index

## Project Overview

This is a Python project managed with `uv`. It follows service-based organization with domain-driven directory structure as specified in the project guidelines.

## Directory Structure

```
google_adk/
├── google_adk/          # Main package directory
│   ├── __init__.py       # Package initialization
│   ├── main.py           # Main application logic
│   ├── service/          # Service layer - business logic and external integrations
│   ├── models/           # Data models and domain entities
│   └── utils/            # Utility functions and helpers
├── tests/                # Test files (empty, ready for tests)
├── run.py                # Application entry point script
├── pyproject.toml        # Project configuration and dependencies
├── .gitignore            # Git ignore patterns
├── .python-version       # Python version specification
├── uv.lock               # Dependency lock file
├── README.md             # Project README
└── index.md              # This file - project documentation index
```

## Architecture Principles

This project follows these key architectural principles:

1. **One Class Per File** - Each class has its own dedicated source file
2. **Service-Based Organization** - Services are organized in separate folders with related files
3. **Domain-Based Directory Structure** - Files are placed in subdirectories reflecting their domain
4. **Clear Naming Conventions** - Files use snake_case matching their class names

## Services

No services defined yet.

### Service Structure Template

When adding new services, follow this structure:

```
google_adk/service/
└── <service_name>/
    ├── <service_name>_service.py    # Main service class
    ├── <service_name>_config.py     # Configuration class
    └── validators/                   # Related validators (if needed)
        └── <validator_name>.py
```

## Models

No models defined yet.

### Model Structure

Models should be placed in `google_adk/models/` with one model per file:

```
google_adk/models/
├── <model_name>.py
└── <another_model>.py
```

## Utilities

No utilities defined yet.

### Utility Structure

Utility functions should be organized in `google_adk/utils/` by domain:

```
google_adk/utils/
├── <utility_domain>.py
└── <another_utility>.py
```

## Getting Started

### Prerequisites

- Python >= 3.14
- `uv` package manager

### Installation

```bash
# Navigate to project directory
cd google_adk

# Install dependencies (creates virtual environment automatically)
uv sync
```

### Running the Application

```bash
# Run using the entry point script
uv run run.py

# Or run the main module directly
uv run python -m google_adk.main
```

### Development

```bash
# Add a new dependency
uv add package-name

# Add a development dependency
uv add --dev package-name

# Remove a dependency
uv remove package-name

# Update dependencies
uv lock --upgrade
```

### Running Tests

```bash
# Run all tests
uv run pytest

# Run with verbose output
uv run pytest -v

# Run with coverage report
uv run pytest --cov

# Run specific test file
uv run pytest tests/test_main.py
```

## Development Guidelines

### Adding New Classes

1. Create a new file in the appropriate directory (service/, models/, or utils/)
2. Name the file in snake_case matching the class name
3. If creating a service, create a dedicated folder with related files
4. Update this index.md with the new class location

### Commit Messages

Use conventional commits format:

```
<type>(<scope>): <subject>
```

**Types:** feat, fix, docs, style, refactor, perf, test, chore, ci, build

**Examples:**
- `feat(service): add embedding service`
- `fix(models): correct user model validation`
- `docs: update index with new services`
- `test: add tests for utility functions`

### Code Style

- Follow PEP 8 guidelines
- Use type hints where appropriate
- Write docstrings for all public classes and functions
- Keep functions focused and single-purpose

## Project Dependencies

### Production Dependencies

None yet.

### Development Dependencies

- `pytest>=8.4.2` - Testing framework
- `pytest-cov>=7.0.0` - Test coverage reporting

## Testing

All tests should be placed in the `tests/` directory with the naming convention `test_<module_name>.py`.

Current test coverage:
- No tests yet. Add tests as you develop features.

## Maintenance Notes

- Each class should have its own file
- File names should match class names in snake_case
- Update this index when adding new classes or services
- Follow conventional commits for all changes
- Use `uv` for all package management operations
- Never commit directly without proper commit messages

## Troubleshooting

### Module Not Found Errors

If you encounter `ModuleNotFoundError`, ensure the project root is in your Python path. The `run.py` script handles this automatically.

### Virtual Environment Issues

If you need to recreate the virtual environment:

```bash
# Remove existing venv
rm -rf .venv

# Recreate with uv
uv sync
```

---

**Project Version:** 0.1.0
**Last Updated:** Initial Setup
**Python Version:** >= 3.14
**Package Manager:** uv

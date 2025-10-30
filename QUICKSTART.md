# Quick Start Guide

## Initial Setup

```bash
# 1. Install dependencies
uv sync

# 2. Verify installation
uv run run.py
```

## Common Commands

### Running the Application

```bash
# Using entry point script
uv run run.py

# Using module
uv run python -m google_adk.main
```

### Testing

```bash
# Run all tests
uv run pytest

# Run with coverage
uv run pytest --cov

# Run specific test
uv run pytest tests/test_main.py -v
```

### Package Management

```bash
# Add dependency
uv add requests

# Add dev dependency
uv add --dev black

# Remove dependency
uv remove requests

# Update all packages
uv lock --upgrade

# Sync dependencies
uv sync
```

## Creating New Components

### New Service

```bash
# 1. Create service directory
mkdir -p google_adk/service/my_service

# 2. Create service files
touch google_adk/service/my_service/__init__.py
touch google_adk/service/my_service/my_service.py
touch google_adk/service/my_service/my_service_config.py

# 3. Update index.md
```

### New Model

```bash
# 1. Create model file
touch google_adk/models/user.py

# 2. Update index.md
```

### New Utility

```bash
# 1. Create utility file
touch google_adk/utils/helpers.py

# 2. Update index.md
```

## Git Workflow

### Conventional Commits

```bash
# Feature
git commit -m "feat(service): add authentication service"

# Bug fix
git commit -m "fix(models): correct user validation"

# Documentation
git commit -m "docs: update API documentation"

# Refactoring
git commit -m "refactor(utils): simplify helper functions"

# Tests
git commit -m "test: add integration tests for service"
```

### Common Workflow

```bash
# 1. Create feature branch
git checkout -b feature/new-feature

# 2. Make changes and stage
git add .

# 3. Commit with conventional message
git commit -m "feat: add new feature"

# 4. Push to remote
git push origin feature/new-feature
```

## Project Structure Reference

```
google_adk/
├── google_adk/           # Main package
│   ├── __init__.py        # Package init
│   ├── main.py            # Main logic
│   ├── service/           # Services
│   │   └── [service]/     # Each service in own folder
│   │       ├── [service].py
│   │       └── [service]_config.py
│   ├── models/            # Data models
│   │   └── [model].py     # One model per file
│   └── utils/             # Utilities
│       └── [utility].py   # One utility per file
├── tests/                 # Tests
│   └── test_[module].py   # Test files
├── run.py                 # Entry point
├── pyproject.toml         # Dependencies
└── index.md               # Full documentation
```

## Key Principles

1. **One Class Per File** - Each class in its own file
2. **Snake Case** - File names match class names in snake_case
3. **Service Folders** - Related service files grouped together
4. **Update Docs** - Keep index.md current
5. **Conventional Commits** - Use proper commit messages

## Troubleshooting

### Module Not Found

```bash
# The run.py script handles path setup automatically
# If issues persist, check your Python path
uv run run.py
```

### Test Failures

```bash
# Run with verbose output
uv run pytest -vv

# Run specific test
uv run pytest tests/test_main.py::test_main -v
```

### Dependency Issues

```bash
# Remove and recreate environment
rm -rf .venv
uv sync
```

## Resources

- **Full Documentation**: See `index.md`
- **Project Guidelines**: See `~/.claude/CLAUDE.md`
- **uv Documentation**: https://github.com/astral-sh/uv

## Next Steps

1. ✅ Read `index.md` for detailed documentation
2. ✅ Review existing code structure in `google_adk/`
3. ✅ Start building your services!

---

**Quick Reference Card**

| Task | Command |
|------|---------|
| Run app | `uv run run.py` |
| Run tests | `uv run pytest` |
| Add package | `uv add package-name` |
| Add dev package | `uv add --dev package-name` |
| Install deps | `uv sync` |
| Update deps | `uv lock --upgrade` |
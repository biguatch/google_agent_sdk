# Google ASDK

A Python SDK for Google services with a clean, service-based architecture.

## Overview

Google ASDK is a modern Python SDK designed to interact with Google services and APIs. Built with a focus on maintainability and scalability, it follows service-based architectural patterns with clear separation of concerns.

## Features

- 🏗️ **Service-Based Architecture** - Clean separation of business logic into dedicated services
- 📦 **Domain-Driven Structure** - Organized by domain with clear module boundaries
- 🧪 **Comprehensive Testing** - Built-in test suite with pytest
- ⚡ **Fast Package Management** - Uses `uv` for blazing-fast dependency management
- 🔧 **Type-Safe** - Designed with type hints for better IDE support and fewer bugs
- 📚 **Well-Documented** - Extensive documentation and clear code organization

## Prerequisites

- Python >= 3.14
- `uv` package manager

### Installing uv

If you don't have `uv` installed:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd google_adk
```

2. Install dependencies:

```bash
# Install all dependencies and create virtual environment
uv sync
```

## Quick Start

Run the application using the entry point script:

```bash
uv run run.py
```

Or run the main module directly:

```bash
uv run python -m google_adk.main
```

## Project Structure

```
google_adk/
├── google_adk/          # Main package
│   ├── __init__.py       # Package initialization
│   ├── main.py           # Main application logic
│   ├── service/          # Service layer
│   ├── models/           # Data models
│   └── utils/            # Utility functions
├── tests/                # Test suite
├── run.py                # Application entry point
├── pyproject.toml        # Project configuration
├── index.md              # Detailed project index
└── README.md             # This file
```

## Development

### Adding Dependencies

```bash
# Add a production dependency
uv add package-name

# Add a development dependency
uv add --dev package-name

# Remove a dependency
uv remove package-name
```

### Running Tests

```bash
# Run all tests
uv run pytest

# Run with verbose output
uv run pytest -v

# Run with coverage
uv run pytest --cov

# Run specific test file
uv run pytest tests/test_main.py
```

### Code Organization

This project follows strict organizational principles:

1. **One Class Per File** - Each class gets its own file
2. **Service Folders** - Related services are grouped in dedicated folders
3. **Snake Case Naming** - Files use snake_case matching their class names
4. **Domain Directories** - Files are organized by domain (models, services, utils)

### Example: Adding a New Service

```bash
# Create service directory
mkdir -p google_adk/service/my_service

# Create service files
touch google_adk/service/my_service/my_service.py
touch google_adk/service/my_service/my_service_config.py
touch google_adk/service/my_service/__init__.py
```

### Commit Convention

This project uses Conventional Commits:

```
<type>(<scope>): <subject>
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

**Examples:**
```bash
git commit -m "feat(service): add embedding service"
git commit -m "fix(models): correct validation logic"
git commit -m "docs: update README with examples"
```

## Testing

The project includes a comprehensive test suite using pytest:

```bash
# Run all tests
uv run pytest

# Run with coverage report
uv run pytest --cov=google_adk

# Generate HTML coverage report
uv run pytest --cov=google_adk --cov-report=html
```

## Documentation

For detailed information about the project structure, classes, and development guidelines, see:

- [index.md](index.md) - Comprehensive project index and documentation
- [pyproject.toml](pyproject.toml) - Project configuration and dependencies

## Contributing

1. Follow the code organization principles outlined above
2. Write tests for all new functionality
3. Use conventional commit messages
4. Update `index.md` when adding new classes or services
5. Ensure all tests pass before submitting changes

## License

[Add your license information here]

## Contact

[Add contact information here]

## Acknowledgments

This project uses:
- [uv](https://github.com/astral-sh/uv) - Fast Python package manager
- [pytest](https://pytest.org/) - Testing framework
- [pytest-cov](https://pytest-cov.readthedocs.io/) - Coverage plugin

---

**Version:** 0.1.0  
**Python:** >= 3.14  
**Package Manager:** uv
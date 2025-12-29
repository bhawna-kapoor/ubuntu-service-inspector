# Ubuntu Service Inspector

A simple Python utility to inspect and report system services on an Ubuntu machine.

This project is part of my learning journey to understand:
- Linux services
- Python scripting
- Command-line tools
- Writing clean, iterative code

---

## Features

- Lists system services
- Shows their current status
- Designed to be extended with more inspection commands

---

## Project Structure
- `inspector/`: The core package containing logic for service inspection and error handling.
- `usi.py`: A lightweight entry script for running the CLI without installing the package.
- `.gitignore`: Ensures environment-specific files aren't tracked.
- `pyproject.toml`: Defines package metadata and the installed `usi` CLI entry point.

---

## Requirements

- Ubuntu / Linux system
- Python 3.x

---

## Installation (optional)
- For development or local usage:
```bash
pip install -e .
```
  - This installs the `usi` command in editable mode, so code changes take effect immediately.

## Usage
### Using the installed CLI (recommended)
#### List all services
```bash
usi list
```

#### List only failed services
```bash
usi list --failed
```

#### Check status of a specific service
```bash
usi status ghost-service
```

### Running directly (no installation required)
#### List all services
```bash
python3 usi.py list
```

#### List only failed services
```bash
python3 usi.py list --failed
```

#### Check status of a specific service
```bash
python3 usi.py status bluetooth
```
---

## Future Improvements
 - Add unit tests
 - Add JSON output support for automation

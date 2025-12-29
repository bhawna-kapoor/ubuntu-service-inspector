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
- `usi.py`: The main entry point/CLI script.
- `.gitignore`: Ensures environment-specific files aren't tracked.

---

## Requirements

- Ubuntu / Linux system
- Python 3.x

---

## Usage
### List all services
```bash
python3 usi.py list
```

### List only failed services
```bash
python3 usi.py list --failed
```

### Check status of a specific service
```bash
python3 usi.py status bluetooth
```
---

## Future Improvements
 - Improve error handling
 - Add unit tests
 - Better formatted output

# PGR107-Python-Exam

---
## Install Python
 1. https://www.python.org/downloads/
 2. Add Python to PATH
    1. Windows: `Win + x` select "System"
    2. Advanced system settings - Environment variables
    3. Under "System variables" - "Path" select "Edit"
    4. Select New and add to path `C:\Python\Python<version>\Scripts`, where `<version>` is the Python version installed
    5. macOS: Update `./bashrc`, `./bash_profile` or `./zshrc` file path to Python `/usr/local/bin/python3`
 3. Check for Python version `py --version`
---
## Add Virtual Environment to Project
 Install the Python Virtual Environment
 1. Navigate to project directory `cd path/to/project`
 2. Create the virtual environment library folder `py -m venv venv`

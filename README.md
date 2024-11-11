# 0x00. AirBnB clone - The console

![image](https://github.com/user-attachments/assets/0cff691f-5e4a-4cc2-9c94-401e86ef2402)

## Overview
This project is a simple command-line interpreter (shell) for managing instances of various classes, including the BaseModel and User. The interpreter supports running commands to interact with a file-based storage system, and allows users to create, store, and display objects in a structured way. This project is part of a larger set of exercises to build familiarity with object-oriented programming, file handling, and shell programming.

## Project Structure

```plaintext
Airbnb-Clone/
│
├── __init__.py                       # Makes this folder a Python package
│
├── models                            # Contains the model classes and related functionality
│   └── __init__.py                   # Makes this folder a Python package
│   └── base_model.py                 # Base class with common attributes and methods for models
│   └── user.py                       # User class inherits from BaseModel
│   └── engine                        # Contains the engine that handles file storage logic
│       └── __init__.py               # Makes this folder a Python package
│       └── file_storage.py           # Storage for objects (serialization/deserialization)
│
├── console.py                        # Command-line interpreter for interacting with the program
│
├── tests                             # Contains the unit tests
│   └── __init__.py                   # Makes this folder a Python package
│   └── test_console.py               # Unit tests for the command-line interpreter
│   └── test_base_model.py            # Unit tests for BaseModel
│   └── test_file_storage.py          # Unit tests for FileStorage
│
├── .gitignore                        # To ignore unnecessary files
│
├── README.md                         # Project documentation
└── requirements.txt                  # Project dependencies for installation
```


## Project Components

- BaseModel Class (models/base_model.py):
A base class providing common attributes (id) and methods (save(), to_dict()) for models like User.

- FileStorage Class (models/engine/file_storage.py):
Manages file-based storage, handling serialization, deserialization, and listing of objects.

- Command Interpreter (console.py):
A command-line interface that allows users to interact with the program, enabling operations like creating, displaying, and managing objects.

- User Class (models/user.py):
Inherits from BaseModel and represents a user object, extending the basic functionality with user-specific attributes.


## Features

- Create, List, Show, and Destroy objects.
- Store object data in a JSON file for persistence.
- Handle User-specific attributes and operations through inheritance.
- Interactive Mode: Enter commands directly in the terminal.
- Non-Interactive Mode: Provide commands through script input.


## Installation

### Prerequisites
- Python 3.8
- JSON (for file storage)
- Unix/Linux environment for the shell

### Setup Instructions
- Clone the repository
- Make sure you have Python installed on your machine.
- Ensure that all Python files are in the same directory or sub-directories, maintaining the same structure as the repository.


## Usage

### Running the Command Interpreter

- To start the interactive shell, run the following command:
```bash
python3 console.py
```
- This will enter the interactive mode where you can type commands. Below are some example commands:
** Create a new object:
```bash
create <ClassName> <attributes>
```

```bash
create User first_name="Nicholas" last_name="Wilson"
```

** Show an object:
```bash
show <ClassName> <id>
```

** List all objects of a class:
```bash
all <ClassName>
```

** Destroy an object
```bash
destroy User 12345
```

** Quit the interpreter:
```bash
quit
```

### Non-Interactive Mode

You can run commands from a file or script by passing input to the shell:
```bash
python3 console.py < <input-file>
```

Where "<input-file>" contains a list of commands, one per line.


## Contributing
Contributions to this project are welcome. To get started:

- Fork the repository.
- Create a new branch (git checkout -b feature-branch).
- Commit your changes (git commit -am 'Add new feature').
- Push the branch to your fork (git push origin feature-branch).
- Create a new pull request.


## Authors
- sirnicson
- bn-yussuph

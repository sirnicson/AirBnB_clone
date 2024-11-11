# 0x00. AirBnB clone - The console

![image](https://github.com/user-attachments/assets/0cff691f-5e4a-4cc2-9c94-401e86ef2402)

## Overview
This project is a simple command-line interpreter (shell) for managing instances of various classes, including the BaseModel and User. The interpreter supports running commands to interact with a file-based storage system, and allows users to create, store, and display objects in a structured way. This project is part of a larger set of exercises to build familiarity with object-oriented programming, file handling, and shell programming.

## Project Structure

The project is divided into several components:

- BaseModel Class: A base class that is inherited by other objects (e.g., User) and provides common attributes and methods for interacting with the storage system.
- FileStorage Class: Manages file-based storage of objects. It handles serializing, deserializing, and listing objects in memory and the storage file.
- Command Interpreter: A custom shell that allows users to interact with the program via commands. The interpreter can handle commands to manage instances, including creating, displaying, and storing objects.
- User Class: Inherits from BaseModel and represents a specific type of object to be managed by the system.

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


# Custom Shell Implementation

This project involves building a POSIX-compliant shell capable of interpreting shell commands, running external programs, and handling built-in commands like `cd`, `pwd`, `echo`, and more.

## Features

- **Built-in Commands**: `cd`, `pwd`, `echo`, `exit`, `type`
- **External Command Execution**: Executes commands found in the system's PATH
- **Error Handling**: Provides basic error messages for invalid commands and arguments

## Requirements

- Python 3.x

## How to Run

1. **Clone the Repository:**

   ```sh
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Run the Shell:**

   ```sh
   python main.py
   ```

## Usage

- The shell will display a prompt (`$ `) where you can type commands.
- Supported built-in commands:
    - `cd <directory>`: Change the current directory to `<directory>`.
    - `pwd`: Print the current working directory.
    - `echo <text>`: Print `<text>` to the standard output.
    - `exit <code>`: Exit the shell with the given exit code.
    - `type <command>`: Display information about the command (whether it is a built-in or an external command).

## Example

```sh
$ pwd
/home/user
$ cd /tmp
$ pwd
/tmp
$ echo Hello, World!
Hello, World!
$ type cd
cd is a shell builtin
$ type ls
ls is /bin/ls
$ exit 0
```

## Code Explanation

### Overview

The code implements a simple custom shell in Python. It reads user commands, processes built-in commands, and executes external programs found in the system's PATH.

### Key Components

1. **Imports**:
    - `sys`: Provides access to system-specific parameters and functions.
    - `os`: Provides a way of using operating system-dependent functionality like reading or writing to the file system.
    - `subprocess`: Allows you to spawn new processes, connect to their input/output/error pipes, and obtain their return codes.

2. **Built-in Commands**:
    - A list of supported built-in commands: `cd`, `pwd`, `echo`, `exit`, `type`.

3. **Function: `find_executable(command)`**:
    - Searches for the given command in the directories listed in the PATH environment variable.
    - Returns the path to the command if found, otherwise returns `None`.

4. **Function: `main()`**:
    - The main loop of the shell.
    - Continuously prompts the user for input, processes the input, and executes the appropriate command.

### Detailed Explanation

1. **Prompt and Input**:
    - The shell prints a prompt (`$ `) and waits for the user to enter a command.
    - The user input is read and stripped of leading/trailing whitespace.

2. **Command Parsing**:
    - The input command is split into the command name and its arguments.
    - If the input is empty, the loop continues to prompt the user.

3. **Built-in Command Handling**:
    - **`cd <directory>`**: Changes the current directory to `<directory>`.
        - If the argument is `~`, it changes to the user's home directory.
        - If the directory does not exist, it prints an error message.
    - **`pwd`**: Prints the current working directory.
    - **`echo <text>`**: Prints `<text>` to the standard output.
    - **`exit <code>`**: Exits the shell with the given exit code.
        - If the argument is not a number, it prints an error message.
    - **`type <command>`**: Displays information about the command.
        - If the command is a built-in, it prints that it is a shell built-in.
        - If the command is an external program, it prints the path to the executable.
        - If the command is not found, it prints an error message.

4. **External Command Handling**:
    - If the command is not a built-in, the shell searches for the executable in the system's PATH.
    - If found, it uses `subprocess.run` to execute the command with the provided arguments.
    - If the command execution fails, it prints the error message.
    - If the command is not found, it prints an error message.

5. **Main Loop**:
    - The `main()` function runs in an infinite loop, continuously prompting the user for input and processing commands until the user exits the shell.

### Error Handling

- The shell provides basic error messages for invalid commands and arguments.
- For example, if the user tries to change to a non-existent directory, it prints an error message.
- If the user provides an invalid exit code, it prints an error message.

### Conclusion

This custom shell is a simple yet functional implementation that demonstrates how to handle user input, process built-in commands, and execute external programs in Python. It provides a basic framework that can be extended with additional features and commands as needed.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.
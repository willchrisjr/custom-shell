Sure! Let's document the changes in the code and update the `README.md` to reflect the new stage of the project.

### Code Documentation and Explanation

#### Updated `main.py`

```python
import sys

def main():
    while True:
        # Print the shell prompt
        sys.stdout.write("$ ")
        sys.stdout.flush()

        # Read user input
        command = input().strip()

        # Check if the command is recognized
        # For now, we assume all commands are unrecognized
        if command:
            print(f"{command}: command not found")

if __name__ == "__main__":
    main()
```

### Explanation

1. **Importing the `sys` Module:**
   - The `sys` module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter.

2. **Defining the `main` Function:**
   - The `main` function is the entry point of the script. It contains the logic for the shell prompt, handling user input, and the REPL.

3. **Infinite Loop (`while True`):**
   - The loop ensures that the shell keeps running, waiting for user input, evaluating it, printing the result, and then waiting for the next input.

4. **Printing the Shell Prompt:**
   - `sys.stdout.write("$ ")` prints the shell prompt (`$ `) to the console.
   - `sys.stdout.flush()` ensures that the prompt is displayed immediately by flushing the output buffer.

5. **Reading User Input:**
   - `command = input().strip()` reads the user input from the console and removes any leading or trailing whitespace using the `strip()` method.

6. **Handling Unrecognized Commands:**
   - The `if command:` statement checks if the user has entered a command (i.e., the input is not empty).
   - `print(f"{command}: command not found")` prints the error message indicating that the entered command is not recognized. The `f` before the string denotes an f-string, which allows embedding expressions inside string literals using curly braces `{}`.

7. **Loop Back to the Prompt:**
   - The `while True` loop ensures that the shell continuously prints the prompt, reads user input, evaluates it, and prints the result.

### Updated README.md

```markdown
# Build Your Own Shell

Welcome to the Build Your Own Shell challenge! This project involves building a POSIX-compliant shell capable of interpreting shell commands, running external programs, and handling built-in commands like `cd`, `pwd`, `echo`, and more.

## Project Overview

In this project, you'll learn about shell command parsing, REPLs (Read-Eval-Print Loops), built-in commands, and more. The project is divided into multiple stages, each focusing on a specific aspect of shell functionality.

## Stages

### Stage 1: Printing the Shell Prompt

#### Objective

In this stage, you'll implement printing a shell prompt (`$ `) and waiting for user input.

#### Implementation

The implementation is done in the `main.py` file. Here’s the code:

```python
import sys

def main():
    # Uncomment this block to pass the first stage
    sys.stdout.write("$ ")
    sys.stdout.flush()

    # Wait for user input
    input()

if __name__ == "__main__":
    main()
```

#### How to Run

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/your-new-repo.git
   cd your-new-repo
   ```

2. **Make the Shell Script Executable:**

   Ensure that `your_shell.sh` is executable. You can do this by running:

   ```bash
   chmod +x your_shell.sh
   ```

3. **Run the Shell Script:**

   Execute the shell script:

   ```bash
   ./your_shell.sh
   ```

4. **Test the Shell:**

   The shell should print the prompt (`$ `) and wait for user input.

### Stage 2: Handling Missing Commands

#### Objective

In this stage, you'll implement support for handling missing commands in your shell. The shell should print an error message when an unrecognized command is entered.

#### Requirements

- The shell should print a prompt (`$ `) and wait for user input.
- If an unrecognized command is entered, the shell should print `<command_name>: command not found`.
- The command name will be a random string, so the response cannot be hardcoded.
- The shell can exit after printing the error message for this stage. In later stages, we will implement a REPL to keep the shell running continuously.

#### Implementation

The implementation is done in the `main.py` file. Here’s the code:

```python
import sys

def main():
    while True:
        # Print the shell prompt
        sys.stdout.write("$ ")
        sys.stdout.flush()

        # Read user input
        command = input().strip()

        # Check if the command is recognized
        # For now, we assume all commands are unrecognized
        if command:
            print(f"{command}: command not found")

        # Exit after handling the command (for this stage only)
        break

if __name__ == "__main__":
    main()
```

#### How to Run

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/your-new-repo.git
   cd your-new-repo
   ```

2. **Make the Shell Script Executable:**

   Ensure that `your_shell.sh` is executable. You can do this by running:

   ```bash
   chmod +x your_shell.sh
   ```

3. **Run the Shell Script:**

   Execute the shell script:

   ```bash
   ./your_shell.sh
   ```

4. **Test the Shell:**

   Type a command like `nonexistent` and press Enter. The output should be:

   ```
   $ nonexistent
   nonexistent: command not found
   ```

### Stage 3: Implementing a REPL (Read-Eval-Print Loop)

#### Objective

In this stage, you'll implement a REPL (Read-Eval-Print Loop) in your shell. A REPL is an interactive loop that reads user input, evaluates it, prints the result, and then waits for the next input.

#### Requirements

- The shell should continuously print the prompt (`$ `), wait for user input, evaluate the command, print the result, and loop back to the prompt.
- If an unrecognized command is entered, the shell should print `<command_name>: command not found`.
- The exact number of commands sent and the command names will be random.

#### Implementation

The implementation is done in the `main.py` file. Here’s the code:

```python
import sys

def main():
    while True:
        # Print the shell prompt
        sys.stdout.write("$ ")
        sys.stdout.flush()

        # Read user input
        command = input().strip()

        # Check if the command is recognized
        # For now, we assume all commands are unrecognized
        if command:
            print(f"{command}: command not found")

if __name__ == "__main__":
    main()
```

#### How to Run

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/your-new-repo.git
   cd your-new-repo
   ```

2. **Make the Shell Script Executable:**

   Ensure that `your_shell.sh` is executable. You can do this by running:

   ```bash
   chmod +x your_shell.sh
   ```

3. **Run the Shell Script:**

   Execute the shell script:

   ```bash
   ./your_shell.sh
   ```

4. **Test the Shell:**

   Type a series of invalid commands like `invalid_command_1`, `invalid_command_2`, and `invalid_command_3`, pressing Enter after each one. The output should be:

   ```
   $ invalid_command_1
   invalid_command_1: command not found
   $ invalid_command_2
   invalid_command_2: command not found
   $ invalid_command_3
   invalid_command_3: command not found
   $
   ```

### Next Steps

In the next stages, we will:
- Implement support for valid commands like `echo`, `cd`, etc.
- Add more advanced features and error handling.

Stay tuned for more updates!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```

### Summary

This updated `README.md` includes:

1. **Project Overview:** A brief introduction to the project.
2. **Stages:** Separate sections for each stage, detailing the objective, implementation, and how to run and test the shell.
3. **Next Steps:** A brief outline of what will be implemented in future stages.
4. **License:** Information about the project’s license.

By following this structure, you can easily document each new addition to your project, making it clear and organized for anyone who reads your `README.md`.
import sys
import os

def main():
    while True:
        # Print the shell prompt
        sys.stdout.write("$ ")
        sys.stdout.flush()

        # Read user input
        command = input().strip()

        # Split the command into the command name and arguments
        parts = command.split()
        if not parts:
            continue

        cmd_name = parts[0]
        args = parts[1:]

        # Handle built-in commands
        if cmd_name == "cd":
            if len(args) != 1:
                print("cd: expected one argument")
            else:
                try:
                    os.chdir(args[0])
                except FileNotFoundError:
                    print(f"cd: no such file or directory: {args[0]}")
        elif cmd_name == "pwd":
            print(os.getcwd())
        elif cmd_name == "echo":
            print(" ".join(args))
        elif cmd_name == "exit":
            if len(args) != 1:
                print("exit: expected one argument")
            else:
                try:
                    exit_code = int(args[0])
                    sys.exit(exit_code)
                except ValueError:
                    print("exit: numeric argument required")
        else:
            # Handle unrecognized commands
            print(f"{cmd_name}: command not found")

if __name__ == "__main__":
    main()
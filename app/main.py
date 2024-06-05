import sys
import os
import subprocess

# List of shell builtins
builtins = ["cd", "pwd", "echo", "exit", "type"]

def find_executable(command):
    """
    Search for the command in the directories listed in the PATH environment variable.
    Return the path to the command if found, otherwise return None.
    """
    path_dirs = os.environ.get("PATH", "").split(":")
    for directory in path_dirs:
        potential_path = os.path.join(directory, command)
        if os.path.isfile(potential_path) and os.access(potential_path, os.X_OK):
            return potential_path
    return None

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
                target_dir = args[0]
                if target_dir == "~":
                    target_dir = os.environ.get("HOME", "")
                try:
                    os.chdir(target_dir)
                except FileNotFoundError:
                    print(f"cd: {target_dir}: No such file or directory")
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
        elif cmd_name == "type":
            if len(args) != 1:
                print("type: expected one argument")
            else:
                target_cmd = args[0]
                if target_cmd in builtins:
                    print(f"{target_cmd} is a shell builtin")
                else:
                    executable_path = find_executable(target_cmd)
                    if executable_path:
                        print(f"{target_cmd} is {executable_path}")
                    else:
                        print(f"bash: type: {target_cmd}: not found")
        else:
            # Handle external programs
            executable_path = find_executable(cmd_name)
            if executable_path:
                try:
                    result = subprocess.run([executable_path] + args, check=True, text=True, capture_output=True)
                    print(result.stdout, end="")
                except subprocess.CalledProcessError as e:
                    print(e.stderr, end="")
            else:
                # Handle unrecognized commands
                print(f"{cmd_name}: command not found")

if __name__ == "__main__":
    main()
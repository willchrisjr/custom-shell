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
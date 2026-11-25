import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def load_line(directory):
    path = os.path.join(directory, "entry.txt")
    with open(path, "r", encoding="utf-8") as handle:
        text = handle.read()
    return text.rstrip("\r\n")


def main():
    line = load_line(HERE)
    sys.stdout.write(line + "\n")


if __name__ == "__main__":
    main()

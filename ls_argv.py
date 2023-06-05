#!/usr/bin/python3

"""This is a python script that uses sys module to create a CLI app that
replicates the ls command."""

import sys
from pathlib import Path

if (args_count := len(sys.argv)) > 2:
    print(f"We expected one arguement, but you gave {args_count - 1}")
    raise SystemExit(2)
elif args_count < 2:
    print("You have not given us your preffered directory")
    raise SystemExit(2)

target_directory = Path(sys.argv[1])

#the path function in pathlib finds the path of the file stored in the arg

if not target_directory.is_dir():
    print(f"Sorry. The {sys.argv[1]} directory you gave does not exist")
    raise SystemExit(1)

for entry in target_directory.iterdir():
    print(entry.name)

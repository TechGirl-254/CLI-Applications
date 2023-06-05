#!/usr/bin/python3

"""This script uses argparse to replicate the ls command."""

import argparse
from pathlib import Path

#Create an argument parser and store it in a variable

parser = argparse.ArgumentParser()

#Add arguments to the to the arguement parser

parser.add_argument("path")

#Get the namespace of the arguments and store it in a variable

args = parser.parse_args()

target_directory = Path(args.path)

if not target_directory.exists():
    print("The directory you gave does not exist")
    raise SystemExit(1)

for entry in target_directory.iterdir():
    print(entry.name)

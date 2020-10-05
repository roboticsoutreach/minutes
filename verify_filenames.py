#! /usr/bin/env python3

#
# Copyright (c) 2019 Dan Trickey.
# 
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
# 
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

from pathlib import Path
import re

status = True

print("Verifying minutes filenames.")

repo = Path(".")

year_folders = []

for f in repo.iterdir():
    if f.is_dir():
        if f.name[0] == ".":
            print(f"Found folder {f.stem}, ignoring")
        else:
            year_folders.append(f)
    elif f.is_file():
        if f.name not in {"verify_filenames.py", "README.md"}:
            print(f"Found bad file name: {f.name}")
            status = False

folder_regex = re.compile("^20[0-9]{2}$")

filename_regex = re.compile("^20[0-9]{2}-[0-9]{2}-[0-9]{2}((\.md)|(-[a-z0-9-]*\.md))$")

for folder in year_folders:

    # Verify folder name is valid

    result = re.match(folder_regex, folder.name)

    if result is None:
        print(f"Found bad folder name: {folder.name}")
        status = False
    else:
        print(f"Found valid folder name: {folder.name}")

    for f in folder.iterdir():

       # Test if there are any nested folders

       if f.is_dir():
           print(f"\tFound nested directory: {folder.stem}/{f.stem}")
           status = False
       
       # Verify file name
       
       file_result =  re.match(filename_regex, f.name)

       if file_result is None:
           print(f"\tFound bad file name: {f.name}")
           status = False
       else:
           print(f"\tFound valid file name: {f.name}")

if status:
    print("All tests passed.")
else:
    print("Some tests failed.")
    exit(1)

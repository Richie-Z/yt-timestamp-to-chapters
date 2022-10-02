import os

if (os.path.exists("output.txt")):
    os.remove("output.txt")
else:
    open("output.txt", "x")
with open('timestamps.txt') as input:
    for index, line in enumerate(input, 1):
        separator = line.split(" - ")
        with open("output.txt", "a") as out:
            out.write(f"CHAPTER{index}={separator[0]}.000")
            out.write("\n")
            out.write(f"CHAPTER{index}NAME={separator[1]}")

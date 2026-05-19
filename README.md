# BookBot Project

Bookbot is a Python program that analyzes novels and prints a statistical report of the word and character usage found within

## Requirements

- **Python 3.x**: Ensure you have Python 3 installed on your system.
- No additional external libraries or virtual environments are strictly required since this project only relies on Python's built-in modules.

## How to Run

Run the program from your terminal by providing the relative or absolute path to the text file you want to analyze as an argument:

```bash
python3 main.py <path_to_book>
```

**Example:**

```bash
python3 main.py books/frankenstein.txt
```

## Expected Output

When running the project with a text file, you should see output similar to the following:

```text
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 75767 total words
--------- Character Count -------
e: 44538
t: 29493
a: 25894
o: 24494
i: 23927
n: 23643
s: 20360
r: 20079
h: 19176
d: 16318
l: 12306
m: 10206
u: 10111
c: 9011
f: 8451
y: 7756
w: 7450
p: 5952
g: 5795
b: 4868
v: 3737
k: 1661
x: 691
j: 497
q: 325
z: 235
æ: 28
â: 8
ê: 7
ë: 2
ô: 1
============= END ===============
```

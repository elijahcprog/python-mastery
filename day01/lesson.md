# Day 1: Setup, a Git refresher, and how Python stores data

**Today's goal:** get your tools working on Windows, refresh how Git works, and understand variables and types properly.

**Time:** about 30 minutes of reading plus doing. Setup is a one-off, so today may run 15–20 minutes over. That's fine.

---

## Part A: Windows setup (one-off)

Do each step in order. Skip any tool you already have, but still run the "check it worked" line for it.

### A1. Python

1. Go to **python.org → Downloads** and download the latest Python 3 installer for Windows.
2. Run it. On the first screen, **tick "Add python.exe to PATH"** before you click Install.
   - *PATH* is a list of folders Windows searches when you type a command. Adding Python to it lets you type `python` anywhere.
3. Check it worked: open **PowerShell** (Start menu → type "PowerShell") and run:
   ```
   python --version
   ```
   You should see something like `Python 3.13.x`. If you get an error, close PowerShell, reopen it and try again.

### A2. Git

1. Go to **git-scm.com** and download Git for Windows. Install it with the default options.
   - It includes **Git Credential Manager**, which handles signing in to GitHub for you.
2. Check it worked:
   ```
   git --version
   ```
3. Tell Git who you are. Every commit is stamped with this. Use the email address on your GitHub account:
   ```
   git config --global user.name "Elijah Cotterell"
   git config --global user.email "YOUR-GITHUB-EMAIL"
   git config --global init.defaultBranch main
   ```

### A3. VS Code

1. Install VS Code from **code.visualstudio.com**.
2. Open it, click the **Extensions** icon on the left (four squares) and install **Python** (made by Microsoft).
3. Open a terminal inside VS Code with **Ctrl + `** (the key under Esc). This is PowerShell running inside VS Code, and you'll use it every day.

### A4. pytest (the tool that checks your exercises)

```
python -m pip install pytest
```

- `pip` is Python's app store: it downloads packages, which are code other people wrote.
- `python -m pip` means "use the pip that belongs to this Python", which avoids mix-ups.
- On Day 10 you'll learn to keep packages per project, using virtual environments.

---

## Part B: Git refresher 1

### What Git actually is

Git is a **save system with history**. A normal save overwrites your file. A Git save (a **commit**) keeps a snapshot, so you can see or go back to any past version.

**GitHub** is a website that stores a copy of your Git project online. Git is the tool; GitHub is the place.

### The 3 areas (the idea most people never get taught)

Your code passes through three places:

```
 Working folder   --git add-->   Staging area   --git commit-->   Repository (history)
 (files you edit)                (what goes in                     (saved snapshots)
                                  the next snapshot)
```

1. **Working folder**: the files you see and edit in VS Code.
2. **Staging area**: a waiting room. `git add` puts changes here to say "include these in the next snapshot".
3. **Repository**: the history of every commit, stored in a hidden `.git` folder.

Then `git push` sends your new commits up to GitHub.

**Why the waiting room?** So you can choose what goes into each snapshot. If you changed 5 files but only 2 belong together, you add just those 2.

### Create your repo and get it on your PC (one-off)

1. On **github.com**, signed in as `elijahcprog`, click **New repository**.
   - Name: `python-mastery`
   - Public (so it counts as a portfolio) or Private, your choice.
   - **Leave every "Add a README / .gitignore / licence" box unticked.** You'll add your own.
2. In the VS Code terminal, go to where you want the course to live, then **clone** it. Cloning means downloading the repo and linking it to GitHub:
   ```
   cd ~\Documents
   git clone https://github.com/elijahcprog/python-mastery.git
   cd python-mastery
   ```
   - `cd` means "change directory": move into a folder.
   - `~` is shorthand for your user folder (`C:\Users\<you>`).
   - Git may warn "you appear to have cloned an empty repository". That's expected.
3. In VS Code: **File → Open Folder → Documents\python-mastery**.

### Add today's files and push (you'll do this every day)

1. Unzip the files I sent and copy `README.md`, `.gitignore` and the `day01` folder **into** `python-mastery`.
   - `.gitignore` starts with a dot, so Windows may hide it. In File Explorer, go to **View → Show → Hidden items**.
2. See what Git notices:
   ```
   git status
   ```
   The new files show in red as **untracked**: Git sees them but isn't saving them yet.
3. Move them to the staging area:
   ```
   git add .
   ```
   The `.` means "everything in this folder". Run `git status` again and they turn green: staged.
4. Take the snapshot, with a message saying what changed:
   ```
   git commit -m "Day 1: add course files"
   ```
5. Send it to GitHub:
   ```
   git push
   ```
   The first time, a browser window opens asking you to sign in to GitHub. Approve it, and Git remembers you after that.
6. Refresh your repo page on github.com. Your files are there.

At the end of the day, once you've done the exercises, commit again:
```
git add .
git commit -m "Day 1: complete exercises and LeetCode 1108"
git push
```

---

## Part C: How Python runs your code

Python is an **interpreted** language. A program called the **interpreter** reads your `.py` file **top to bottom, one line at a time**, and does each line before moving on.

That's why order matters:

```python
print(greeting)      # Error! Python hasn't seen 'greeting' yet
greeting = "hello"
```

To run a file from the terminal:
```
python day01\playground.py
```

Or open the file in VS Code and press the **▶ Run** button in the top right.

---

## Part D: Variables

A **variable** is a **name tag stuck on a value**.

```python
failed_logins = 5
```

Read it right to left: "make the value `5`, then stick the name `failed_logins` on it." The `=` sign does **not** mean "equals" here. It means **"assign"**: point this name at this value.

You can move the tag to a new value at any time:
```python
failed_logins = 5
failed_logins = failed_logins + 1   # take the old value, add 1, re-stick the tag
print(failed_logins)                 # 6
```

**Naming rules:** use lowercase words joined by underscores (`failed_logins`, not `FailedLogins` or `fl`). This style is called *snake_case*. Names can't start with a number. Good names make code read like English.

---

## Part E: The 4 basic types

Every value has a **type**, which says what kind of thing it is and what you can do with it.

| Type | What it holds | Examples |
|---|---|---|
| `int` | Whole numbers | `5`, `-12`, `443` |
| `float` | Numbers with a decimal point | `3.14`, `0.5`, `2.0` |
| `str` | Text (a "string" of characters) | `"admin"`, `'192.168.0.1'` |
| `bool` | True or false | `True`, `False` |

Check any value's type with `type()`:
```python
print(type(443))       # <class 'int'>
print(type("443"))     # <class 'str'>   ← quotes make it text, not a number!
```

### Maths operators

```python
7 + 2    # 9      add
7 - 2    # 5      subtract
7 * 2    # 14     multiply
7 / 2    # 3.5    divide: ALWAYS gives a float
7 // 2   # 3      floor divide: divide, then throw away the decimal part
7 % 2    # 1      modulo: the remainder after dividing
2 ** 10  # 1024   power
```

`//` and `%` come up constantly. Think of sharing out 7 sweets between 2 people: each gets `7 // 2 = 3`, and `7 % 2 = 1` is left over.

### Converting between types

Text that *looks* like a number is still text:
```python
"5" + "3"            # "53"  ← joins the text together
int("5") + int("3")  # 8     ← converts to numbers first
str(443)             # "443"
float("2.5")         # 2.5
round(3.14159, 2)    # 3.14
```

**Why this matters:** anything that comes from outside your program, such as user input, a file or a web request, arrives as **text**. Converting it is often the first thing you do.

---

## Part F: Input, output and f-strings

```python
name = input("Username: ")   # pauses, waits for typing, ALWAYS returns a str
print("Hello", name)
```

An **f-string** puts variables straight into text. Put an `f` before the quotes and the variable inside `{ }`:
```python
user = "bob"
attempts = 5
print(f"User {user} failed {attempts} times")
# User bob failed 5 times
```

You can also format numbers inside the braces:
```python
f"{3.14159:.2f}"   # "3.14"   → 2 decimal places
f"{7:02d}"         # "07"     → at least 2 digits, padded with zeros
```

---

## Part G: Today's pattern: building a string step by step

Strings can't be changed in place (they're *immutable*). Instead you build a **new** string:

```python
ip = "10.0.0.1"
safe = ip.replace(".", "[.]")    # creates a new string
print(safe)                      # 10[.]0[.]0[.]1
print(ip)                        # 10.0.0.1  ← original unchanged
```

`.replace(old, new)` is a **method**: a function that belongs to a value, called with a dot. You'll meet many more on Day 6.

---

## Part H: Functions (just enough for today)

The exercises are written as **functions**. For now, think of one as a **machine**: values go in (the *parameters*), and `return` sends the answer out.

```python
def double(number):
    return number * 2

double(4)   # 8
```

Write your code where it says `# YOUR CODE HERE`, and make sure you **`return`** the answer rather than `print` it. Day 3 covers functions properly.

---

## Now do

1. `exercises.py`: 3 exercises. Check them with:
   ```
   python -m pytest day01
   ```
   Green `passed` = correct. Red `FAILED` = read the message: it shows what your code returned and what was expected.
   (Always name the day folder like this. Each day has a file called `exercises.py`, so running every day at once would mix them up.)
2. `leetcode.md`: today's LeetCode problem.
3. Commit and push (Part B).

**Stuck?** Give it 20 minutes, then ask me for **Hint 1**.

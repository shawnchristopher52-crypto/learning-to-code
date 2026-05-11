# Week 1 — How Computers Think + Your First Programs

> **Estimated time:** 6–10 hours, spread over the week.
> **Difficulty:** Beginner. No prior knowledge assumed.

---

## What You'll Learn This Week

By Friday, you will:

1. Understand what code actually *is* and how computers run it
2. Have your tools fully set up (VS Code, Python, Git, GitHub)
3. Have written and run multiple Python programs
4. Have made your first GitHub repository and pushed code to it
5. Know how to use the terminal/command line for basic tasks

This is the most "setup-heavy" week of the entire curriculum. Push through it — it gets dramatically more fun once your environment works smoothly.

---

# Part 1: How Computers Actually Think

Before we write any code, let's demystify what's happening inside your computer. Most beginners skip this and pay for it later. We won't.

## The Core Idea

A computer is, at heart, a machine that does **simple things very fast and very repeatedly**.

The CPU (the "brain" of your computer) can really only do a small set of things:

- Move a piece of data from one place to another
- Do simple math (add, subtract, multiply, compare)
- Make a decision based on a comparison ("if this is true, jump to that instruction")

That's basically it. Everything else — opening Chrome, playing a video, running a video game — is built out of *billions* of those simple operations chained together.

The trick is: a CPU does this **very, very fast.** A modern CPU performs **billions of simple operations per second**. So even though each step is tiny, the *combination* of those steps creates the experience of a working computer.

### A Helpful Mental Model

Imagine the CPU as a chef who can only follow extremely simple instructions:

- "Pick up that pan."
- "Put it on the stove."
- "Turn the stove to setting 3."
- "Wait 30 seconds."
- "If the timer rings, do the next step."

The chef can't think creatively. But if you write detailed enough instructions, you can guide the chef through making a 5-course meal. **A program is a recipe for the CPU.**

## What Is "Code," Then?

Code is **a recipe written in a language the computer can eventually understand.**

Why "eventually"? Because the CPU doesn't actually speak Python or JavaScript. It speaks **machine code** — sequences of 1s and 0s that map to those tiny operations.

But writing 1s and 0s would be miserable. So we use **programming languages** that look more like English, and a separate program (called a *compiler* or *interpreter*) translates our code into machine code for us.

When you write Python code like this:

```python
print("Hello, world!")
```

What happens behind the scenes (very simplified):

1. The Python interpreter reads your line of code.
2. It translates `print("Hello, world!")` into a sequence of CPU instructions.
3. Those instructions tell the CPU to find the right place in memory, fetch the text "Hello, world!", and send it to the screen.
4. You see the words appear.

You don't need to understand each step in detail yet. The takeaway is: **code is your way of giving the CPU very precise instructions, in a language friendlier than 1s and 0s.**

## Why Computers Are So Picky

Computers are unforgiving in a way humans aren't. If you say to a friend, *"hand me the bok"*, they'll figure out you mean "book." A computer? It will refuse to run.

This is because the CPU executes instructions exactly. There's no "approximate" matching. A missing comma, a misspelled name, an extra space in the wrong place — any of these can stop your program cold.

**This isn't because computers are dumb. It's because they're literal.**

In your first weeks of coding, you will spend **a lot** of time staring at error messages caused by tiny mistakes — a missing parenthesis, a typo in a variable name, the wrong kind of quote mark. This is normal. Every developer, at every level, deals with this. The skill you're building is not "writing code without mistakes" (impossible). It's "noticing and fixing mistakes quickly."

## Programs vs. Programming Languages

A quick vocabulary tour:

| Term | What it means |
|---|---|
| **Programming language** | The notation you write code in (e.g., Python, JavaScript). Different languages have different rules and strengths. |
| **Source code** | The text *you* write (e.g., a `.py` file you save). Humans read this. |
| **Program** | The thing that runs on your computer when source code is executed. |
| **Interpreter / Compiler** | The translator that turns source code into machine code. Python uses an *interpreter*; some languages (C, Rust) use a *compiler*. |
| **Bug** | A mistake in the code that causes wrong behavior. |
| **Debug** | The process of finding and fixing bugs. |

You'll meet more terms as we go. Don't try to memorize this table — just refer back when you forget.

---

# Part 2: Setting Up Your Environment

Time to set up your tools. Take this slowly. Skipping setup steps causes pain later.

## What You're Installing

| Tool | What it does | Why you need it |
|---|---|---|
| **VS Code** | A code editor — a word processor for code | Where you'll write your programs |
| **Python** | A programming language + interpreter | The language you'll learn first |
| **Git** | Version control — tracks changes to your code | Saves your project history; lets you undo mistakes |
| **GitHub account** | A website that stores Git repositories online | Your public portfolio + cloud backup |

## Step 1: Verify (or Install) Python

You mentioned you might already have Python. Let's check.

### On Windows:

1. Press `Windows key` + `R`, type `cmd`, press Enter. This opens **Command Prompt** (a.k.a. the terminal).
2. In the black window, type:

   ```
   python --version
   ```

3. Press Enter.

You'll see one of three results:

- **`Python 3.10.something` or higher** — ✅ You're set. Move to Step 2.
- **`Python 2.something`** — You have an old version. Install fresh Python 3 (instructions below).
- **An error like "command not found"** — Python isn't installed (or isn't on your PATH). Install it now.

### To install Python (Windows):

1. Go to **https://www.python.org/downloads/**
2. Click the big yellow "Download Python 3.x.x" button.
3. Run the installer. **Important:** On the first screen of the installer, **check the box that says "Add Python to PATH"**. This is critical. If you miss it, Python won't work from the terminal.
4. Click "Install Now" and wait.
5. Close and reopen Command Prompt. Run `python --version` again. You should see your version number.

> **The "Add to PATH" thing — what's that about?** PATH is a list of folders your computer checks when you type a command. If Python isn't on that list, your computer won't know where to find it when you type `python`. That checkbox saves you from a confusing manual fix later.

## Step 2: Install VS Code

1. Go to **https://code.visualstudio.com/**
2. Download the installer for Windows.
3. Run it. Accept defaults — but on the "Select Additional Tasks" screen, **check these boxes**:
   - "Add 'Open with Code' action to Windows Explorer file context menu"
   - "Add 'Open with Code' action to Windows Explorer directory context menu"
   - "Add to PATH"
4. Click Install, then Finish.
5. Launch VS Code. You should see a welcome screen.

### Install the Python extension for VS Code:

1. In VS Code, click the Extensions icon on the left sidebar (looks like four squares with one floating away).
2. In the search box, type `Python`.
3. Find the one published by **Microsoft** (it'll be the first result, usually has 100M+ downloads).
4. Click "Install".

That's it for VS Code setup for now.

## Step 3: Install Git

1. Go to **https://git-scm.com/download/win**
2. The download starts automatically.
3. Run the installer. Accept defaults all the way through. (There are a *lot* of options — defaults are fine for now. We can tune them later if needed.)
4. After install, open Command Prompt and run:

   ```
   git --version
   ```

   You should see something like `git version 2.40.x`.

## Step 4: Set Up GitHub

You said you have a GitHub account — great. Let's connect Git on your computer to it.

1. Open Command Prompt.
2. Run these two commands, replacing the values with **your** info:

   ```
   git config --global user.name "Chris Christy"
   git config --global user.email "chrischristy52@gmail.com"
   ```

   (Use the same email you signed up to GitHub with.)

3. To verify, run:

   ```
   git config --global --list
   ```

   You should see your name and email listed.

We'll connect your local Git to GitHub more deeply later in the week when you make your first repository. The credentials will be requested then; on Windows, this is usually handled by a small popup that signs you in via your browser. Easy.

---

# Part 3: Your First Program

Time to actually write code.

## Hello, World

There's a tradition: when you learn a new programming language, your very first program prints "Hello, world!" to the screen. We honor it now.

### Step 1: Create a project folder

In your `Learn Code` folder (the one you're in now), notice the `Phase_1_Foundations/Week_01_Setup_and_First_Steps/project/` folder. That's where this week's code lives.

### Step 2: Open VS Code in that folder

Two ways:

- **Right-click the `Week_01_Setup_and_First_Steps` folder in File Explorer → "Open with Code"**
- Or open VS Code, go to **File → Open Folder...**, and pick the `Week_01_Setup_and_First_Steps` folder.

You should see the folder name in VS Code's left sidebar.

### Step 3: Create your first Python file

In VS Code:

1. Click into the **`project`** folder in the left sidebar.
2. Click the "New File" icon (a tiny page with a + on it, hovering over the project folder).
3. Name the file **`hello.py`**. The `.py` extension tells your computer this is a Python file.
4. Press Enter. A blank file opens.

### Step 4: Type your first line of code

Type this **exactly**, including the quotes and parentheses:

```python
print("Hello, world!")
```

Save the file (`Ctrl+S`).

### Step 5: Run it

In VS Code, open the **terminal** by pressing `` Ctrl+` `` (Ctrl + the backtick key, top-left of your keyboard, below Esc). A terminal panel appears at the bottom.

In that terminal, type:

```
python hello.py
```

Press Enter.

You should see:

```
Hello, world!
```

🎉 **You just ran your first program.** The Python interpreter read your file, translated `print("Hello, world!")` into machine instructions, and the CPU told the screen to display those words.

> **If it didn't work**, don't panic. Run `python --version` first — if that doesn't work either, Python isn't on your PATH. Reinstall and check the "Add to PATH" box. If `python --version` works but `python hello.py` doesn't, make sure your terminal is in the right folder (the path shown before the `>` should end with `project`). You can change folders with `cd` (change directory). Come back to chat with me if stuck.

## Understanding What You Wrote

Let's pull apart that one line, because it teaches you things you'll use forever.

```python
print("Hello, world!")
```

- **`print`** is a *function* — a built-in piece of Python that performs an action. The `print` function's job is to display text on the screen.
- **`(` and `)`** — these parentheses are how you *call* the function. Calling a function means "run it." You're saying: "Hey Python, run the `print` function, and here's what to print."
- **`"Hello, world!"`** — this is a *string*, the technical name for a piece of text. The double quotes mark the start and end of the text. Without quotes, Python would think you meant something else.

Try changing it:

```python
print("Coding is going to be fun.")
```

Save, run again. New message appears.

Try this:

```python
print("Line 1")
print("Line 2")
print("Line 3")
```

Each `print` call puts text on its own line.

**You're already programming.** It feels small, but you've grasped the core loop: write code, save, run, see result. Every program in the world — from a website to a video game — is just a much bigger version of this.

## Comments — Notes to Humans

One more tool before we move on. In Python, anything after a `#` symbol is a **comment** — text that Python ignores completely. Comments are how you leave notes for yourself or other developers reading your code.

```python
# This whole line is a comment. Python skips it.
print("Hello")  # You can also put a comment after code on the same line.
```

For multi-line notes, just use multiple `#` lines:

```python
# This is part one of a longer note.
# This is part two.
# Each line needs its own #.
```

**Why comments matter:** Code tells the computer *what* to do; comments explain *why* you did it that way. Six months from now, re-reading your own code, you'll be glad past-you left notes. Don't overuse them — `# add 1 to x` next to `x = x + 1` is noise — but use them to explain reasoning that isn't obvious from the code alone.

You'll use comments in Exercise 1E to record your predictions before running code.

---

# Part 4: Your First GitHub Repository

You're going to put your "Hello, world!" file on GitHub. This builds a habit you'll use weekly: write code → save it → push to GitHub.

## What Is Git, Really?

Imagine you're writing a long essay. Every so often, you save a copy with a name like `essay_v1.docx`, `essay_v2.docx`, `essay_final.docx`, `essay_FINAL_FOR_REAL.docx`. You've made your own messy version control system.

**Git is a tool that does this for you, professionally.** It tracks every change to every file in a project, lets you label important moments ("commits"), and lets you go back to any earlier version any time.

**GitHub is a website where Git repositories live online.** It's where you push your local Git history to so it's backed up, shareable, and viewable.

Together: Git tracks history locally; GitHub stores it online.

## Step 1: Create a Repository on GitHub

1. Go to **https://github.com/** and log in.
2. Click the **"+"** in the top right → **"New repository"**.
3. Repository name: **`learning-to-code`**
4. Description (optional but good): "My journey from beginner to developer."
5. Set it to **Public**. (Your work being public is a feature, not a bug — it builds your portfolio.)
6. **Do NOT** check "Add a README file" — we'll handle that locally.
7. Click **"Create repository"**.

You'll land on a page with setup instructions. Keep that tab open.

## Step 2: Initialize Git in Your Project Folder

In VS Code's terminal (still in the `Week_01_Setup_and_First_Steps/project` folder), run these commands one at a time. I'll explain each.

```
git init
```

> **What this does:** Tells Git "start tracking changes in this folder." A hidden `.git` folder is created. You don't see it, but Git's bookkeeping lives there.

```
git add hello.py
```

> **What this does:** "Stage" your file — tell Git that this file is one you want to include in your next commit.

```
git commit -m "First commit: hello world"
```

> **What this does:** Create a commit — a labeled snapshot of the staged files. The `-m` part is the *message* that describes this snapshot. Always write meaningful messages.

```
git branch -M main
```

> **What this does:** Renames your default branch to `main`. (A "branch" is a line of development. We'll cover branches deeply in Phase 5; for now, just know `main` is the standard name.)

Now connect to your GitHub repo. Go to your GitHub repo page. Copy the URL that looks like `https://github.com/your-username/learning-to-code.git`. Then run:

```
git remote add origin https://github.com/your-username/learning-to-code.git
```

(Replace with your actual URL.)

> **What this does:** Tells Git "the online home of this project is at that URL." `origin` is just a nickname for that remote location.

Finally, push:

```
git push -u origin main
```

> **What this does:** Uploads your commit to GitHub. The `-u origin main` part sets the default upstream — so future pushes can just be `git push`.

The first time you push, a browser window may pop up asking you to log into GitHub. Sign in. Once authorized, the push completes.

## Step 3: See Your Code on GitHub

Refresh your GitHub repository page in the browser. **You should see `hello.py` listed.** Click it. You'll see your code right there, in the cloud.

🎉 **You now have a public portfolio of your work.** It has one file. Soon it'll have dozens.

---

# Part 5: A Tour of the Terminal (Brief)

The terminal is intimidating but it's a vital tool. Here's a survival guide. We'll deepen this over time.

## Common Commands

| Command | What it does |
|---|---|
| `cd folder_name` | Change directory (move into a folder) |
| `cd ..` | Move up one folder |
| `dir` (Windows) or `ls` (Mac/Linux) | List files in current folder |
| `python filename.py` | Run a Python file |
| `git status` | See what Git thinks is going on with your files |

If you ever feel lost, type `cd` with no arguments on Windows and it shows your current folder.

## When You Make a Typo

Just retype the command. The terminal isn't sensitive. You haven't broken anything. **You cannot easily destroy your computer with terminal commands at the level you're working at.** (There are dangerous commands, but you won't encounter them in this curriculum unless I warn you first.)

---

# Your Week 1 Tasks (In Order)

Work through these in order. Some are reading, some are doing.

1. **Read this entire README** (you're doing this now — well done).
2. **Verify or install Python** (Part 2, Step 1).
3. **Install VS Code and the Python extension** (Part 2, Step 2).
4. **Install Git and configure your name/email** (Part 2, Steps 3 & 4).
5. **Create `hello.py` and run it** (Part 3).
6. **Complete the exercises** in `exercises/exercise_01.md`.
7. **Build the project** described in `project/PROJECT.md`.
8. **Push everything to GitHub** (Part 4).
9. **Update `progress_log.md`** with what you did this week and any sticking points.
10. **Come back to chat** when you're done — tell me you finished, and I'll review your code and build out Week 2.

---

# Common First-Week Pitfalls (and Fixes)

These are the things that trip up almost every beginner. Skim them now; come back when you hit one.

| Pitfall | Symptom | Fix |
|---|---|---|
| Python not on PATH | `python` command not recognized | Reinstall Python; check "Add to PATH" |
| Wrong quote characters | `SyntaxError: invalid character` | Don't use "smart quotes" from a word processor — type quotes directly in VS Code |
| Wrong indentation | `IndentationError` | Python is picky about spaces — VS Code helps, but watch for mixing tabs/spaces |
| Running file from wrong folder | `python: can't open file 'hello.py'` | Use `cd` to navigate to the file's folder, or open the right folder in VS Code |
| Forgot to save before running | Code runs but you don't see your changes | Always `Ctrl+S` before running |
| Git asks for login repeatedly | Browser popup keeps appearing | Use the same browser for GitHub. Sometimes credential storage needs a reset — ask me if persistent |

---

# What's Next

Week 2 covers **variables, data types, and getting input from users.** You'll build a unit converter that takes input and gives back useful answers.

When you're done with Week 1, message me with: "Done with Week 1." I'll review your progress, answer any questions, and create Week 2.

You're off the starting line, Chris. Let's keep moving. 🚀

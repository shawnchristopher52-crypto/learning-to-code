# Git Cheat Sheet

> Your quick reference for everyday Git use. Bookmark this.

---

## The Everyday Loop (Use This 99% of the Time)

After you've made changes to your code, run these four commands in order:

```
git status                          # See what changed
git add .                           # Stage all changes
git commit -m "Describe the change" # Snapshot them
git push                            # Upload to GitHub
```

That's the whole flow.

---

## First-Time Setup (Once per New Project)

You only run these when **starting a brand-new project** that doesn't have Git yet:

```
git init
git branch -M main
git remote add origin https://github.com/your-username/your-repo.git
git add .
git commit -m "Initial commit"
git push -u origin main
```

After this, switch to the everyday loop above. The `-u origin main` part sets up a default upstream, so future pushes are just `git push`.

---

## Cloning an Existing Repo (Working on Someone Else's Code, or a Repo You Made on GitHub First)

```
git clone https://github.com/user/repo.git
cd repo
```

Now you can use the everyday loop.

---

## Useful Commands

| Command | What it does |
|---|---|
| `git status` | Show changed/staged files |
| `git add filename` | Stage one specific file |
| `git add .` | Stage everything that changed |
| `git commit -m "message"` | Save a snapshot with a message |
| `git push` | Send commits to GitHub |
| `git pull` | Get latest changes from GitHub (we'll need this when you work from multiple computers) |
| `git log` | Show commit history |
| `git log --oneline` | Show commit history, one line per commit |
| `git diff` | Show what's changed since the last commit |
| `git diff --staged` | Show what's staged (about to be committed) |

---

## Mental Model: The Three Areas

Files in a Git project move through three areas:

```
[edit file]  →  [git add]  →  [git commit]  →  [git push]
working dir     staging       repository       GitHub
```

- **Working directory** = the files in your folder
- **Staging area** = the "ready to commit" zone
- **Repository** = your local commit history
- **GitHub** = the online copy of your repo

`git status` shows you what's in working dir vs. staged. Always run it when you're not sure.

---

## Good Commit Messages

Aim for: *short, specific, in present-tense imperative form.*

| Good | Bad |
|---|---|
| `Add Week 2 exercises` | `update` |
| `Fix typo in greeting` | `asdf` |
| `Refactor about_me.py for clarity` | `fixed it` |
| `Add input validation to converter` | `did some stuff` |

A trick: the message should fit the sentence "If applied, this commit will ___." So `"Add user login"` (✓) vs `"Added user login"` (acceptable but less standard).

---

## Common "Oh No" Situations and Fixes

### "I committed but forgot to add a file"

Stage the missing file, then add it to your last commit:

```
git add forgotten_file.py
git commit --amend --no-edit
```

(Only do this if you haven't pushed yet. Once pushed, prefer a new commit.)

### "I want to undo my last commit but keep the changes"

```
git reset --soft HEAD~1
```

### "I want to throw away all changes since last commit"

```
git checkout .
```

⚠️ This permanently deletes uncommitted changes. Be sure.

### "git push is being rejected"

Usually means GitHub has commits you don't have locally. Run:

```
git pull
```

Then try pushing again.

---

## The Three Commands You'll Use Most

If you remember nothing else, remember these:

```
git add .
git commit -m "your message"
git push
```

Welcome to ~80% of professional Git use.

## This Repo is created to check the Git commands

> - Link to [servicenowDevRepo](https://github.com/ServiceNowDevProgram/code-snippets)

## Git cheatsheet

### **Basic Git Workflow**

```bash
git init                     # Initialize a new Git repository
git clone <url>             # Clone a repository
git status                  # Show the working directory status
git add <file>              # Stage a file
git add .                   # Stage all changes
git commit -m "message"     # Commit staged changes
git push                    # Push changes to remote
git pull                    # Fetch and merge changes from remote
```

---

### **Branching & Merging**

```bash
git branch                  # List branches
git branch <name>           # Create a new branch
git checkout <name>         # Switch to a branch
git checkout -b <name>      # Create and switch to a new branch
git merge <branch>          # Merge a branch into current
git branch -d <name>        # Delete a branch
```

---

### **Viewing History**

```bash
git log                     # View commit history
git log --oneline           # Condensed log
git diff                    # Show changes not staged
git diff --staged           # Show staged changes
git show <commit>           # Show details of a specific commit
```

---

### **Undoing Changes**

```bash
git reset <file>            # Unstage a file
git checkout -- <file>      # Discard changes in a file
git revert <commit>         # Create a new commit that undoes a previous one
git reset --hard <commit>   # Reset to a specific commit (dangerous!)
```

---

### **Remote Repositories**

```bash
git remote -v               # List remotes
git remote add origin <url> # Add a remote
git push -u origin <branch> # Push and set upstream
git fetch                   # Fetch changes from remote
```

---

### **Stashing Changes**

```bash
git stash                   # Stash current changes
git stash list              # List stashes
git stash apply             # Apply latest stash
git stash drop              # Delete a stash
```

---
